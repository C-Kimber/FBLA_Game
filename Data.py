from player import *
import wall
from enemy import Base
from fragment import *
import fragment
import other
from level import Level
import os
from camera import Camera
import camera



class Data:
    #intitialisez sprites, and other data
    def __init__(self, width, height, frame_rate):
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.font2 = pygame.font.SysFont("Times New Roman", 72)
        self.frame_rate = frame_rate
        self.width = width
        self.height = height
        self.img = pygame.image.load('./assets/images/Background_1.png')
        self.sprite_library = other.load_images()
        self.bimgs = [ pygame.image.load('./assets/images/background_2.png').convert_alpha()]
        """pygame.image.load('./assets/imagas/B_04.png').convert_alpha(),
            pygame.image.load('./assets/images/B_03.png').convert_alpha(),
            pygame.image.load('./assets/images/B_02.png').convert_alpha(),
            pygame.image.load('./assets/imgaes/B_01.png').convert_alpha()"""

        #other.load_images()

        self.menimg = pygame.image.load('./assets/images/background_3.png').convert_alpha()
        self.mengif = pygame.image.load("./assets/images/particles.gif").convert_alpha()

        self.num_files = len([f for f in os.listdir("./assets/levels")
                         if os.path.isfile(os.path.join("./assets/levels", f))])


        self.emptysprite = Empty()
        self.player = Player(self.sprite_library["player1"])
        #self.playersprite = pygame.sprite.GroupSingle()
        #self.player2sprite = pygame.sprite.GroupSingle()
        self.player2 = Player2(self.sprite_library["player2"])
        self.player3 = self.emptysprite
        self.player4 = self.emptysprite



        self.all_sprites = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.allwalls = pygame.sprite.Group()
        self.deathwalls =pygame.sprite.Group()
        self.telewalls = pygame.sprite.Group()
        self.telewalls2 = pygame.sprite.Group()
        self.upwalls = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.finish = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        #self.playersprite.add(self.player)
        #self.player2sprite.add(self.player2)
        self.players.add(self.player, self.player2, self.player3, self.player4)

        self.resetLists()

        self.mouse_position = [0,0]

        self.current_level = 0
        self.diedfirst = 0
        self.p1score = 0
        self.p1win = 0
        self.p2score = 0
        self.p2win = 0
        self.p1vic = False
        self.p2vic = False
        self.lives = 3
        self.alph_1 = 255

        self.time = 0
        self.overtime = -1

        self.fragmentgroup = fragment.fragmentgroup
        Fragment.groups = self.fragmentgroup, self.all_sprites
        custFrag.groups = self.fragmentgroup


        self.isLoaded = False

        self.camera = Camera(camera.complex_camera, other.TOTAL_LEVEL_WIDTH, other.TOTAL_LEVEL_HEIGHT)


    #active stuff
    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.newbuttons = newbuttons
        self.mouse_position = mouse_position

        if self.isLoaded == False:
            self.initLevel()





        if pygame.K_ESCAPE in newkeys:
            if  other.MINISTATE == 0:
                other.MINISTATE = 1
            elif other.MINISTATE == 1:
                other.MINISTATE = 0


        if self.time > 0:
            self.time -= 1

        a = 0
        a += 1

        if self.time == 0 and other.MINISTATE == 0:


            #controls

            if pygame.K_6 in keys:
                for _ in range(30):
                    self.fragmentgroup.add(custFrag((400,400),(25,50),(255,255,255)))

            if pygame.K_w in newkeys:
                self.player.jump()
            elif pygame.K_s in keys:
                self.player.moveDown()
            """elif pygame.K_s in keys:
                self.player.stunt()
                self.player.stunting = True
            else:
                self.player.stunting = False"""

            if pygame.K_a in keys:
                self.player.moveLeft()


            elif pygame.K_d in keys:
                self.player.moveRight()


            if pygame.K_i in newkeys:
                self.player2.jump()

            elif pygame.K_k in keys:
                self.player2.moveDown()
            """elif pygame.K_k in keys:
                self.player2.stunt()

                self.player2.image.fill((255,0,0))

                self.player2.stunting = True
            else:
                self.player2.image.fill((0,0,0))
                self.player2.stunting = False"""

            if pygame.K_j in keys:
                self.player2.moveLeft()
            elif pygame.K_l in keys:
                self.player2.moveRight()
            # pygame.sprite.collide_circle(self.player, self.player2):

                #for _ in range(20):
                #    self.fragmentgroup.add(custFrag((self.player.rect.x,self.player.rect.y),(1,3),(255,255,0)))


            if self.p1score >= 5:
                self.p1vic = True
            elif self.p2score >= 5:
                self.p2vic = True




            #self.player.update(0,self.height,0, self.width)



            self.all_sprites.update()

        elif other.MINISTATE == 1:
            return
        self.fragmentgroup.update(a)

        return
    #wipes sprite lists, and puts in players + adding new level

    def mainEvolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        a = 0

        a += 1
        if self.isLoaded == False:
            self.initLevel()
            self.all_sprites.remove(self.player2)
            self.player2 = self.emptysprite
            print "LOADING "

        if pygame.K_ESCAPE in newkeys:
            if other.MINISTATE == 0:
                other.MINISTATE = 1
            elif other.MINISTATE == 1:
                other.MINISTATE = 0
        if other.MINISTATE == 0 and self.player.state == "NORMAL":




            self.camera.update(self.player)
            if self.player.alive == False:
                self.lives -= 1
                self.player.alive  = True



            #if self.player2 != self.emptysprite:
              #  self.all_sprites.remove(self.player2)
              #  self.player2 = self.emptysprite


            if pygame.K_w in newkeys:
                self.player.jump()
            elif pygame.K_s in keys:
                self.player.moveDown()

            if pygame.K_a in keys:
                self.player.moveLeft()


            elif pygame.K_d in keys:
                self.player.moveRight()

            if pygame.K_3 in newkeys:
                self.all_sprites.add(Base((self.player.rect.x, self.player.rect.y)))

            if pygame.sprite.spritecollide(self.player, self.player.finish, False):
                self.current_level += 1
                self.player.yvel = 10
                self.player.xvel = 3
                self.player.state = "WIN"
                #

            live_e = []
            for e in self.all_sprites:
                if hasattr(e, 'alive'):

                    if e.alive:

                        live_e.append(e)
                    else:
                        print "Enemy Killed"
                        self.all_sprites.remove(e)
                else:
                    live_e.append(e)
            self.enemies.add(live_e)
            self.all_sprites.add(live_e)




            self.all_sprites.update()





        elif self.player.state == "DYING":
            self.player.dying(a)
            #self.player.state = "NORMAL"
        elif self.player.state == "WIN":
            self.player.beatLvl(self)

        elif other.MINISTATE == 1:
            return
        self.fragmentgroup.update(a)

        if self.overtime > 0:
            self.overtime -= 1
        if self.overtime == 0:
            other.GAMESTATE = 0
            self.lives = 3

        if self.lives <= 0:
            other.GAMESTATE = 3
            if self.overtime == -1:
                self.overtime = 60


    def newLevel(self):
        self.emptyLists()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        n = str(random.randint(1,self.num_files-1))
        self.level = Level("level_0"+n)

    #end of a single battle
    def endRound(self,surface):
        if self.player.alive and not self.player2.alive:
            self.diedfirst = 2
        elif self.player2.alive and not self.player.alive:
            self.diedfirst = 1
        else:
            self.diedfirst = 0
            self.newRound()

        if self.diedfirst == 1:
            self.p2score +=1
            self.p2win = 60
        elif self.diedfirst == 2:
            self.p1score +=1
            self.p1win = 60
        else:
            return


        self.diedfirst = 0
        wall.clearwalls(self)
        wall.cleartel(self)
        self.newRound()

        return
    #begins new battle
    def newRound(self):
            self.newLevel()
            self.player.xvel = 0
            self.player.yvel = 0
            self.player.jumps = 1
            self.player.alive = True


            self.player2.xvel = 0
            self.player2.yvel = 0
            self.player2.jumps = 1
            self.player2.alive = True

            self.time = 60

            self.level.gameLev(self)
    #draws all the stuff, also button functionality
    def newMainLev(self):
        self.emptyLists()
        self.all_sprites.add(self.player)
        self.level = Level("level_"+str(self.current_level), "./assets/long_levels/")
        self.level.gameLev(self)
        self.walldecide()


    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((55,55,55), rect)#back

        for n in self.bimgs:
            surface.blit(n, (0,0))

        #surface.blit(self.img, (0, 0))
        #pygame.display.flip()






        #round
        if not self.player.alive or not self.player2.alive:
            self.endRound(surface)

        #draw sprites

        self.all_sprites.draw(surface)

        #draw
        self.telewalls.draw(surface)
        self.telewalls2.draw(surface)

        ###
        #END MATCH

        self.drawTextLeft(surface, str(self.p1score), (255, 255, 255), 20, 50, self.font)
        self.drawTextLeft(surface, str(self.p2score), (255, 255, 255), self.width - 40, 50, self.font)

        self.fragmentgroup.draw(surface)

        if self.p2vic or self.p1vic:


            r = pygame.Rect(200, 200, 100, 100)
            pygame.draw.rect(surface, (25, 25, 25), rect)
            pygame.draw.rect(surface, (255, 255, 255), r)
            if ((self.mouse_position[0] <= 300 and self.mouse_position[0] >= 200) and (
                            self.mouse_position[1] <= 300 and self.mouse_position[
                        1] >= 200)):  # If mouse is in the rectangle
                pygame.draw.rect(surface, (155, 155, 155), r)
                if 1 in self.newbuttons:
                    other.MINISTATE = 0
                    other.GAMESTATE = 1
                    self.p1score =0
                    self.p2score = 0
                    self.p1vic = False
                    self.p2vic = False
                    self.newRound()
            self.drawTextLeft(surface, "Play", (0, 0, 255), 220, 280, self.font)

            r = pygame.Rect(500, 200, 100, 100)
            pygame.draw.rect(surface, (255, 255, 255), r)
            if ((self.mouse_position[0] <= 600 and self.mouse_position[0] >= 500) and (
                            self.mouse_position[1] <= 300 and self.mouse_position[
                        1] >= 200)):  # If mouse is in the rectangle
                pygame.draw.rect(surface, (155, 155, 155), r)

                if 1 in self.newbuttons:
                    pygame.quit()
            self.drawTextLeft(surface, "Quit", (255, 0, 0), 520, 280, self.font)

            r = pygame.Rect(200, 400, 100, 100)
            pygame.draw.rect(surface, (255, 255, 255), r)

            if ((self.mouse_position[0] <= r[0] + r[2] and self.mouse_position[0] >= r[0]) and (
                            self.mouse_position[1] <= r[1] + r[3] and self.mouse_position[1] >= r[
                        1])):  # If mouse is in the rectangle
                pygame.draw.rect(surface, (155, 155, 155), r)
                if 1 in self.newbuttons:
                    other.GAMESTATE = 0
                    other.MINISTATE = 0
                    self.p1score = 0
                    self.p2score = 0
                    self.p1vic = False
                    self.p2vic = False
                    self.newRound()
                    self.newbuttons.remove(1)
            self.drawTextLeft(surface, "Menu", (0, 0, 255), 220, 480, self.font)

        if self.p1vic :

            self.drawTextLeft(surface, "PLAYER 1 WON!", (0, 255, 0), 150, 150, self.font2)
        elif self.p2vic:
            self.drawTextLeft(surface, "PLAYER 2 WON", (0, 255, 0), 150, 150, self.font2)

        if self.p1win > 0 and not self.p1vic and not self.p2vic:
            self.drawTextLeft(surface, "PLAYER 1 SCORED", (255, 255, 255), 240, self.height/2, self.font)
            self.p1win -= 1
        elif self.p2win > 0 and not self.p2vic and not self.p1vic:
            self.drawTextLeft(surface, "PLAYER 2 SCORED", (255, 255, 255), 240, self.height/2, self.font)
            self.p2win -= 1



        ### menu
        if other.MINISTATE == 1:
            self.pauseMenu(surface)
        #self.level.display(surface)

        return

    def pauseMenu(self, surface):
        rect = pygame.Rect(100, 50, self.width - 200, self.height - 100)
        pygame.draw.rect(surface, (25, 25, 25), rect)

        r = pygame.Rect(200, 200, 100, 100)
        pygame.draw.rect(surface, (25, 25, 25), rect)
        pygame.draw.rect(surface, (255, 255, 255), r)
        self.drawTextLeft(surface, "Menu", (255, 255, 255), 350, 150, self.font)

        if ((self.mouse_position[0] <= 300 and self.mouse_position[0] >= 200) and (
                        self.mouse_position[1] <= 300 and self.mouse_position[
                    1] >= 200)):  # If mouse is in the rectangle
            pygame.draw.rect(surface, (155, 155, 155), r)
            #if 1 in self.newbuttons:

                #other.MINISTATE = 0
        self.drawTextLeft(surface, "Play", (0, 0, 255), 220, 280, self.font)

        r = pygame.Rect(500, 200, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255), r)
        if ((self.mouse_position[0] <= 600 and self.mouse_position[0] >= 500) and (
                        self.mouse_position[1] <= 300 and self.mouse_position[
                    1] >= 200)):  # If mouse is in the rectangle
            pygame.draw.rect(surface, (155, 155, 155), r)

            if 1 in self.newbuttons:
                pygame.quit()
        self.drawTextLeft(surface, "Quit", (255, 0, 0), 520, 280, self.font)

        return

    #menu activity
    def mainDraw(self, surface):

        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((55, 55, 255), rect)  # back


        for e in self.all_sprites:
            surface.blit(e.image, self.camera.apply(e))
        for w in self.wall_list:
            surface.blit(w.image, self.camera.apply(w))


        if other.MINISTATE ==1:
            self.pauseMenu(surface)

        self.drawTextLeft(surface, "Lives  " + str(self.lives), (250, 250, 250), 2, 35, self.font)

        if self.player.state == "STARTING_B":

            s = pygame.Surface((other.TOTAL_LEVEL_HEIGHT, other.TOTAL_LEVEL_WIDTH), pygame.SRCALPHA)
            rect = pygame.Rect(0,0, other.TOTAL_LEVEL_HEIGHT, other.TOTAL_LEVEL_WIDTH)# per-pixel alpha
            surface.fill((self.alph_1,0, 0, self.alph_1), rect)  # notice the alpha value in the color
            #rect.blit(surface, (0, 0))
            self.alph_1 -= 5
            self.camera.update(self.player)
            if self.alph_1 <= 0:
                self.player.state = "NORMAL"
                self.alph_1 = 255
        elif self.player.state == "STARTING_G":
            rect = pygame.Rect(0,0, other.TOTAL_LEVEL_HEIGHT, other.TOTAL_LEVEL_WIDTH)# per-pixel alpha
            surface.fill((0,self.alph_1, 0, self.alph_1), rect)  # notice the alpha value in the color
            #rect.blit(surface, (0, 0))
            self.alph_1 -= 5
            self.camera.update(self.player)
            if self.alph_1 <= 0:
                self.player.state = "NORMAL"
                self.alph_1 = 255





        #self.all_sprites.draw(surface)

    def GameOverDraw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((0,0,0), rect)  # back
        self.drawTextLeft(surface, "GAME OVER", (250, 250, 250), 170, 250, self.font2)

    def initLevel(self):
        if other.GAMESTATE == 1:
            self.level = Level("level_01")
            self.player2 = Player2(self.sprite_library["player2"])
            self.player = Player(self.sprite_library["player1"])
            self.resetLists()

        elif other.GAMESTATE == 2:
            self.all_sprites.remove(self.player2)
            self.player2 = self.emptysprite
            self.emptyLists()
            self.all_sprites.add(self.player)
            self.player.finish = self.finish
            self.player2.finish = self.finish

            self.level =  Level("level_"+str(self.current_level), "./assets/long_levels/")
        self.level.gameLev(self)
        self.walldecide()
        self.isLoaded = True

    def menuve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mouse_position = mouse_position
        self.newbuttons = newbuttons

        return
    #menu drawing
    def menuDraw(self,surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((0, 0, 0), rect)  # back

        surface.blit(self.menimg, (0, 0))

        self.drawTextLeft(surface, "WELCOME TO THE GAME", (0, 255, 0), 200, 150, self.font)

        r = pygame.Rect(200,400, 100,100)
        pygame.draw.rect(surface,(255,255,255),r)

        if ((self.mouse_position[0] <= r[0]+r[2] and self.mouse_position[0] >= r[0]) and (
                self.mouse_position[1] <= r[1]+r[3] and self.mouse_position[1] >= r[1])):  # If mouse is in the rectangle
            pygame.draw.rect(surface, (155, 155, 155), r)
            if 1 in self.newbuttons:
                other.GAMESTATE = 1
                self.initLevel()
                self.newbuttons.remove(1)
        self.drawTextLeft(surface, "Battle", (0, 0, 255), 220, 480, self.font)

        r = pygame.Rect(200, 200, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255), r)

        if ((self.mouse_position[0] <= r[0] + r[2] and self.mouse_position[0] >= r[0]) and (
                        self.mouse_position[1] <= r[1] + r[3] and self.mouse_position[1] >= r[
                    1])):  # If mouse is in the rectangle
            pygame.draw.rect(surface, (155, 155, 155), r)
            if 1 in self.newbuttons:
                print "BEGINNING STORY MODE"
                other.GAMESTATE = 2
                self.overtime = -1
                self.current_level = 0
                self.initLevel()
                self.newbuttons.remove(1)

        self.drawTextLeft(surface, "Play", (0, 0, 255), 220, 280, self.font)

        r = pygame.Rect(500, 200, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255), r)
        if ((self.mouse_position[0] <= r[0] + r[2] and self.mouse_position[0] >= r[0]) and (
                        self.mouse_position[1] <= r[1] + r[3] and self.mouse_position[1] >= r[
                    1])):  # If mouse is in the rectangle
            pygame.draw.rect(surface, (155, 155, 155), r)

            if 1 in self.newbuttons:
                pygame.quit()
        self.drawTextLeft(surface, "Quit", (255, 0, 0), 520, 280, self.font)



        return
    #text function
    def drawTextLeft(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return
    #text fuunction
    def drawTextRight(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return

    def emptyLists(self):
        self.deathwalls.empty()
        self.wall_list.empty()
        self.telewalls.empty()
        self.telewalls2.empty()
        self.all_sprites.empty()
        self.upwalls.empty()
        self.finish.empty()
        self.players.empty()
        self.enemies.empty()
        self.allwalls.empty()

    def resetLists(self):
        self.emptyLists()
        self.players.add(self.player, self.player2, self.player3, self.player4)
        for x in self.players:
            if x != self.emptysprite:
                print x
                self.player.otherplayers.add(x)
                self.player2.otherplayers.add(x)
                if x == self.player:

                    self.player.otherplayers.remove(self.player)
                elif x == self.player2:

                    self.player2.otherplayers.remove(self.player2)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        self.allwalls.add(self.wall_list)
        self.player.walls = self.allwalls
        self.player2.walls = self.allwalls
        for e in self.enemies:
            e.walls = self.allwalls

        self.player.deaths = self.deathwalls
        self.player2.deaths = self.deathwalls

        self.player.teles = self.telewalls
        self.player2.teles = self.telewalls

        self.player.teles2 = self.telewalls2
        self.player2.teles2 = self.telewalls2

        self.player.upwalls = self.upwalls
        self.player2.upwalls = self.upwalls

        self.player.finish = self.finish
        self.player2.finish = self.finish

        self.player.getfimage(
            (  # self.sprite_library["frag1"],self.sprite_library["frag2"],self.sprite_library["frag3"],
                self.sprite_library["frag1_2"]
                , self.sprite_library["frag2_1"], self.sprite_library["frag3_1"]
                , self.sprite_library["frag2_2"], self.sprite_library["frag3_2"]))

        self.player2.getfimage(
            (  # self.sprite_library["frag1"], self.sprite_library["frag2"], self.sprite_library["frag3"],
                self.sprite_library["frag1_2"]
                , self.sprite_library["frag2_1"], self.sprite_library["frag3_1"]
                , self.sprite_library["frag2_2"], self.sprite_library["frag3_2"]))

    def walldecide(self):
        comparator = self.wall_list
        new = pygame.sprite.Group()
        i = 1
        for w in self.wall_list:
            for l in comparator:
                if isinstance(w, wall.Wall) == True and isinstance(l, wall.Wall) == True:
                    self.wall_list.remove(w)


                    if w.y-32 == l.y: #above
                        if w.y + 32 == l.y:
                            i = 5
                        i = 8
                        #w.image = self.sprite_library["wall_5"]#str(random.randint(1,9))]

                    elif w.y + 32 == l.y:#below
                        if w.y - 32 == l.y:
                            i = 5
                        else:
                            i = 2

                    elif w.x - 32 == l.x:#Left
                        if w.y -32 == l.y:#above
                            i= 6
                        if w.y + 32 == l.y:  # Below
                                i = 3

                    elif w.x + 32 == l.x:  # Right
                        if w.y - 32 == l.y:  # above
                            i = 6
                        if w.y + 32 == l.y:#Below
                            i = 3

                    w.image = self.sprite_library["wall_"+str(i)]


                    self.wall_list.add(w)
                else:
                    print "not Wall object"
        self.allwalls.add(self.wall_list)
        #m = self.allwalls + self.wall_list
        #print m
        #self.player.walls = m
        print "TILES DONE TEXTURING"

