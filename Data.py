from player import *
import wall
from item import Base
import item
from fragment import *
import fragment
import other
from level import Level
import os
from camera import Camera
import camera
import audio
import spritesheet



class Data():
    #intitialisez sprites, and other data
    rs = (0,0,800,640)
    allwalls = None


    def __init__(self, width, height, frame_rate):
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.font2 = pygame.font.SysFont("Times New Roman", 72)
        self.font = pygame.font.Font("./assets/emulogic.ttf", 21)
        self.frame_rate = frame_rate
        self.width = width
        self.height = height
        self.sprite_library = other.load_images()
        self.sound_library = audio.load_sounds()
        self.channel_1 = pygame.mixer.Channel(1)


        self.img = spritesheet.spritesheet('./assets/images/f1.png').image_at((0, 0, 896, 792),
                                                                                (254, 254, 254,)).convert(),
        self.mengif = pygame.image.load("./assets/images/particles.gif").convert_alpha()

        self.num_files = (len([f for f in os.listdir("./assets/levels")
                         if os.path.isfile(os.path.join("./assets/levels", f))])-1)/2


        self.emptysprite = Empty()
        self.player = Player(self.sprite_library["player1"])
        self.player.data = self
        #self.playersprite = pygame.sprite.GroupSingle()
        #self.player2sprite = pygame.sprite.GroupSingle()

        self.player2 = Player2(self.sprite_library["player2"])
        self.player2.data = self
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
        self.hitwalls = pygame.sprite.Group()
        self.back_sprites = pygame.sprite.Group()
        self.displayTiles = pygame.sprite.Group()

        self.hashedwalls = ""
        self.displayhaswall = []

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        #self.playersprite.add(self.player)
        #self.player2sprite.add(self.player2)
        self.players.add(self.player, self.player2, self.player3, self.player4)

        self.resetLists()

        self.mouse_position = [0,0]

        self.current_level = other.STARTING_LEVEL
        self.diedfirst = 0
        self.p1score = 0
        self.p1win = 0
        self.p2score = 0
        self.p2win = 0
        self.p1vic = False
        self.p2vic = False
        self.lives = 3
        self.alph_1 = 255
        self.boola = True

        self.time = 0
        self.overtime = -1
        self.level_time = other.LEVEL_TIME
        self.l_t_increment = 0

        self.fragmentgroup = fragment.fragmentgroup
        Fragment.groups = self.fragmentgroup, self.all_sprites
        custFrag.groups = self.fragmentgroup


        self.isLoaded = False


        other.level_surface.fill((0,0,0))
        #pygame.draw.circle(other.disp_filter, (255, 0, 0), (other.WIDTH / 2, 120), 20, 2)


        self.camera = Camera(camera.complex_camera, 200, 200)




    #active stuff
    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.newbuttons = newbuttons
        self.mouse_position = mouse_position


        if self.time > 0:
            self.time -= 1

        a = 0
        a += 1

        if self.time == 0 and other.MINISTATE == 0:


            if self.l_t_increment > 60 :
                self.l_t_increment = 0
                self.level_time -= 1

            #controls
            if self.p2vic or self.p1vic:
                if pygame.K_SPACE in newkeys:

                    other.MINISTATE = 0
                    other.GAMESTATE = 1
                    self.p1score = 0
                    self.p2score = 0
                    self.l_t_increment = 0
                    self.level_time = other.LEVEL_TIME
                    self.p1vic = False
                    self.p2vic = False
                    self.newRound()

            else:
                self.l_t_increment += 1

                if pygame.K_6 in newkeys:
                    self.channel_1.play(self.sound_library["stone_1"])

                if pygame.K_w in keys:
                    self.player.jump()
                else:
                    self.player.jump_cut()

                if pygame.K_s in keys:
                    self.player.moveDown()

                if pygame.K_a in keys:
                    self.player.moveLeft()

                if pygame.K_7 in newkeys:
                    self.player.image = self.sprite_library["player1_bad"]


                elif pygame.K_d in keys:
                    self.player.moveRight()


                if pygame.K_i in keys:
                    self.player2.jump()
                else:
                    self.player2.jump_cut()

                if pygame.K_k in keys:
                    self.player2.moveDown()

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


                self.all_sprites.update()

        elif other.MINISTATE == 1:
            return
        self.fragmentgroup.update(a)

        return
    #wipes sprite lists, and puts in players + adding new level



    def draw(self, surface):




        #pygame.display.flip()
        surface.blit(other.level_surface, (0, 0))




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

        self.drawTextLeft(surface, str(self.p1score), (0,0, 255), 20, 50, self.font)
        self.drawTextLeft(surface, str(self.p2score), (255, 0,0), self.width - 40, 50, self.font)
        if self.level_time >= 0:
            self.drawTextCenter(surface, str(self.level_time), (255, 255, 255), other.WIDTH / 2, 30, self.font)

        else:
            self.drawTextCenter(surface, str(abs(self.level_time)), (155, 0, 0), other.WIDTH / 2, 30, self.font)
            if self.boola:
                self.player.image = self.sprite_library["player1_bad"]
                self.player2.image = self.sprite_library["player2_bad"]
                self.sound_library["thunder"].play()
                self.boola = False

        self.fragmentgroup.draw(surface)

        if self.p2vic or self.p1vic:



            self.drawTextCenter(surface, "Press SPACE Play again!", (255, 255, 255), other.WIDTH/2, 200, self.font)



        if self.p1vic :

            self.drawTextCenter(surface, "PLAYER 1 WON!", (0, 0, 255), other.WIDTH/2, 150, self.font2)
        elif self.p2vic:
            self.drawTextCenter(surface, "PLAYER 2 WON", (255, 0, 0), other.WIDTH/2, 150, self.font2)

        if self.p1win > 0 and not self.p1vic and not self.p2vic:
            self.drawTextCenter(surface, "PLAYER 1 SCORED", (0, 0, 255), other.WIDTH/2, 50, self.font)
            self.p1win -= 1
        elif self.p2win > 0 and not self.p2vic and not self.p1vic:
            self.drawTextCenter(surface, "PLAYER 2 SCORED", (255,0,0), other.WIDTH/2, 50, self.font)
            self.p2win -= 1



        ### menu
        if other.MINISTATE == 1:
            self.pauseMenu(surface)
        #self.level.display(surface)
        self.drawTextLeft(surface, str(other.FPS), (255, 255, 255), other.WIDTH - 50, other.HEIGHT - 50, self.font)


        return

    def menuve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mouse_position = mouse_position
        self.newbuttons = newbuttons

        if pygame.K_SPACE in newkeys:
            self.sound_library["open_1"].play()
            print "FIGHT!"
            self.current_level = other.STARTING_LEVEL
            other.GAMESTATE = 1
            self.initLevel()
            self.overtime = -1


        return
    #menu drawing
    def menuDraw(self,surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((0, 0, 0), rect)  # back

        self.drawTextCenter(surface, "WELCOME TO THE GAME", (255, 255, 255), other.WIDTH/2, 150, self.font)
        self.drawTextCenter(surface, "Press SPACE to play!", (255, 255, 255), other.WIDTH/2, 200, self.font)

        return
    #text function
    def drawTextLeft(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextCenter(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)
        return
    #text fuunction
    def drawTextRight(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return

    def initLevel(self):
        print "initializing level"
        self.emptyLists()
        self.level = Level("level_" + str(self.current_level), "./assets/levels/")
        self.player.state = "NORMAL"
        self.emptyLists()
        self.level.gameLev(self)
        self.allwalls.add(self.wall_list)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        self.drawLev()
        self.isLoaded = True


    def newLevel(self):
        self.emptyLists()
        self.l_t_increment = 0
        self.boola = True
        self.level_time = other.LEVEL_TIME
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        n = str(random.randint(1, int((self.num_files))))
        self.level = Level("level_" + str(n))
        self.player.image = self.sprite_library["player1"]
        self.player2.image = self.sprite_library["player2"]
        self.back_sprites.empty()
        self.level.gameLev(self)
        self.drawLev()

        for e in self.all_sprites:
            if isinstance(e, item.Base) == True:
                self.player.items.add(e)
                self.player2.items.add(e)

    # end of a single battle
    def endRound(self, surface):
        if self.player.alive and not self.player2.alive:
            self.diedfirst = 2
        elif self.player2.alive and not self.player.alive:
            self.diedfirst = 1
        else:
            self.diedfirst = 0
            self.newRound()

        if self.diedfirst == 1:
            self.p2score += 1
            self.p2win = 60
        elif self.diedfirst == 2:
            self.p1score += 1
            self.p1win = 60
        else:
            return

        self.diedfirst = 0
        #wall.clearwalls(self)
        #wall.cleartel(self)
        self.newRound()

        return

    # begins new battle
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

        #self.level.gameLev(self)

    # draws all the stuff, also button functionality



    def emptyLists(self):
        self.deathwalls.empty()
        self.wall_list.empty()
        self.telewalls.empty()
        self.telewalls2.empty()
        self.all_sprites.empty()
        self.back_sprites.empty
        self.upwalls.empty()
        self.finish.empty()
        self.players.empty()
        self.hitwalls.empty()
        self.allwalls.empty()

    def resetLists(self):
        self.emptyLists()
        self.players.add(self.player, self.player2, self.player3, self.player4)
        self.allwalls.add(self.hitwalls)
        self.allwalls.add(self.wall_list)
        for x in self.players:
            if x != self.emptysprite:
                self.player.otherplayers.add(x)
                self.player2.otherplayers.add(x)
                if x == self.player:

                    self.player.otherplayers.remove(self.player)
                elif x == self.player2:

                    self.player2.otherplayers.remove(self.player2)


        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)

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
                , self.sprite_library["frag2_2"], self.sprite_library["frag3_2"]),
            (
                self.sprite_library["sfrag_1"], self.sprite_library["sfrag_2"]  )
        )

        self.player.getSounds(
            (self.sound_library["stone_1"], self.sound_library["stone_2"],self.sound_library["stone_3"],
             self.sound_library["bloop_1"],self.sound_library["bloop_2"],self.sound_library["bloop_3"],
             self.sound_library["fall_1"],self.sound_library["fall_2"]

             )
        )

        self.player2.getfimage(
            (  # self.sprite_library["frag1"], self.sprite_library["frag2"], self.sprite_library["frag3"],
                self.sprite_library["frag1_2"]
                , self.sprite_library["frag2_1"], self.sprite_library["frag3_1"]
                , self.sprite_library["frag2_2"], self.sprite_library["frag3_2"]),

            ( self.sprite_library["sfrag_1"]  , self.sprite_library["sfrag_2"] )
        )

        self.player2.getSounds(
            (self.sound_library["stone_1"], self.sound_library["stone_2"], self.sound_library["stone_3"],
             self.sound_library["bloop_1"], self.sound_library["bloop_2"], self.sound_library["bloop_3"],
             self.sound_library["fall_1"], self.sound_library["fall_2"]

             )
        )

    def getCollidables(self, obj, region=(0.0, 1.0)):
        obj.collidables.empty()
        for w in self.wall_list:
            distance = math.sqrt((obj.rect.x - w.rect.x) ** 2 + (obj.rect.y - w.rect.y) ** 2)
            if distance < 50:
                if isinstance(w,wall.Wall)or isinstance(w, wall.upWall):
                    if w.type != 4:#if is surrounded by tiles
                            obj.collidables.add(w)
                            continue

    def drawLev(self):
        for i in range(0, 28):
            for j in range(0, 30):
                other.level_surface.blit(self.sprite_library["far_back_lava"], (i * 32 + other.WIDTH / 8 + 64, j * 32))
        self.back_sprites.draw(other.level_surface)
        self.wall_list.draw(other.level_surface)










