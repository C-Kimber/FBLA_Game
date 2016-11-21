from player import *
import wall
from fragment import *
import fragment
import other
from level import Level


class Data:
    #intitialisez sprites, and other data
    def __init__(self, width, height, frame_rate):
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.font2 = pygame.font.SysFont("Times New Roman", 72)
        self.frame_rate = frame_rate
        self.width = width
        self.height = height
        self.img = pygame.image.load('./assets/Background_1.png')
        self.bimgs = [pygame.image.load('./assets/B_04.png').convert_alpha(),
                      pygame.image.load('./assets/B_03.png').convert_alpha(),
                      pygame.image.load('./assets/B_02.png').convert_alpha(),
                      pygame.image.load('./assets/B_01.png').convert_alpha()
                      ]

        self.player = Player()
        self.playersprite = pygame.sprite.GroupSingle()
        self.player2sprite = pygame.sprite.GroupSingle()
        self.player2 = Player2()

        self.all_sprites = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.deathwalls =pygame.sprite.Group()

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        self.playersprite.add(self.player)
        self.player2sprite.add(self.player2)

        #wall.randomLevel(self)
        self.level = Level("level_01")
        self.level.gameLev(self)
        self.player.walls = self.wall_list
        self.player2.walls =self.wall_list
        self.player.deaths = self.deathwalls
        self.player2.deaths = self.deathwalls

        self.diedfirst = 0
        self.p1score = 0
        self.p1win = 0
        self.p2score = 0
        self.p2win = 0
        self.p1vic = False
        self.p2vic = False

        self.time = 0

        self.fragmentgroup = fragment.fragmentgroup
        Fragment.groups = self.fragmentgroup, self.all_sprites
        custFrag.groups = self.fragmentgroup
    #active stuff
    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.newbuttons = newbuttons
        self.mouse_position = mouse_position

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

            """elif pygame.K_s in keys:
                self.player.stunt()
                self.player.stunting = True
                self.player.image.fill((0,0,255))
            else:
                self.player.image.fill((255,255,255))
                self.player.stunting = False"""

            if pygame.K_a in keys:
                self.player.moveLeft()


            elif pygame.K_d in keys:
                self.player.moveRight()


            if pygame.K_i in newkeys:
                self.player2.jump()

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
            if pygame.sprite.collide_circle(self.player, self.player2):

                for _ in range(20):
                    self.fragmentgroup.add(custFrag((self.player.rect.x,self.player.rect.y),(1,3),(255,255,0)))
                if self.player.rect.x <= self.player2.rect.x:
                    self.player.xvel = -3 + self.player.xvel * -self.player2.pushfactor
                    self.player2.xvel = 3 + self.player2.xvel * -self.player.pushfactor
                if self.player2.rect.x <= self.player.rect.x:
                    self.player.xvel = 3 + self.player.xvel * -self.player2.pushfactor
                    self.player2.xvel = -3 + self.player2.xvel * -self.player.pushfactor

                if self.player.rect.y - self.player2.rect.y > 1: # if p1 is above p2
                    if self.player.stunting:
                        self.player2.yvel *= 30
                        self.player.yvel = -3
                    else:
                        self.player2.yvel = 5
                        self.player.yvel = -3

                if self.player2.rect.y - self.player.rect.y > 1:  # if p2 is above p1
                    if self.player2.stunting:
                        self.player.yvel *= 30
                        self.player2.yvel = -3
                    else:
                        self.player.yvel = 5
                        self.player2.yvel = -3

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
    def newLevel(self):
        self.wall_list.empty()
        self.all_sprites.empty()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        wall.randomLevel(self)
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
        self.newRound()

        return
    #begins new battle
    def newRound(self):
            self.newLevel()
            self.player.rect.y = 130
            self.player.rect.x = 150
            self.player.xvel = 0
            self.player.yvel = 0
            self.player.jumps = 1
            self.player.alive = True

            self.player2.rect.y = 130
            self.player2.rect.x = 575
            self.player2.xvel = 0
            self.player2.yvel = 0
            self.player2.jumps = 1
            self.player2.alive = True

            self.time = 30
    #draws all the stuff, also button functionality
    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((55,55,55), rect)#back

        for n in self.bimgs:
            surface.blit(n, (0,0))

        #surface.blit(self.img, (0, 0))
        #pygame.display.flip()

        if self.p1win >0 and not self.p1vic and not self.p2vic:
            self.drawTextLeft(surface, "PLAYER 1 SCORED", (255, 255, 255), 240, 50, self.font)
            self.p1win -=1
        elif self.p2win >0 and not self.p2vic and not self.p1vic:
            self.drawTextLeft(surface, "PLAYER 2 SCORED", (255, 255, 255), 240, 50, self.font)
            self.p2win -=1


        self.drawTextLeft(surface, str(self.p1score), (255,255,255), 20,50, self.font)
        self.drawTextLeft(surface, str(self.p2score), (255, 255, 255), self.width-40, 50, self.font)

        #round
        if not self.player.alive or not self.player2.alive:
            self.endRound(surface)

        #draw sprites
        self.all_sprites.draw(surface)

        ###
        #END MATCH



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

        if self.p1vic :

            self.drawTextLeft(surface, "PLAYER 1 WON!", (0, 255, 0), 150, 150, self.font2)
        elif self.p2vic:
            self.drawTextLeft(surface, "PLAYER 2 WON", (0, 255, 0), 150, 150, self.font2)

        self.fragmentgroup.draw(surface)

        ### menu
        if other.MINISTATE == 1:
            rect = pygame.Rect(100, 50, self.width-200, self.height-100)
            pygame.draw.rect(surface, (25, 25, 25), rect)

            r = pygame.Rect(200, 200, 100, 100)
            pygame.draw.rect(surface, (25, 25, 25), rect)
            pygame.draw.rect(surface, (255, 255, 255), r)
            self.drawTextLeft(surface, "Menu", (255, 255, 255), 350, 150, self.font)

            if ((self.mouse_position[0] <= 300 and self.mouse_position[0] >= 200) and (
                            self.mouse_position[1] <= 300 and self.mouse_position[
                        1] >= 200)):  # If mouse is in the rectangle
                pygame.draw.rect(surface, (155, 155, 155), r)
            if 1 in self.newbuttons:
                other.MINISTATE = 0
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

        #self.level.display(surface)

        return
    #menu activity
    def menuve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mouse_position = mouse_position
        self.newbuttons = newbuttons

        return
    #menu drawing
    def menuDraw(self,surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((0, 0, 0), rect)  # back

        self.drawTextLeft(surface, "WELCOME TO THE GAME", (0, 255, 0), 200, 150, self.font)

        r = pygame.Rect(200,200, 100,100)
        pygame.draw.rect(surface,(255,255,255),r)

        if ((self.mouse_position[0] <= 300 and self.mouse_position[0] >= 200) and (
                self.mouse_position[1] <= 300 and self.mouse_position[1] >= 200)):  # If mouse is in the rectangle
            pygame.draw.rect(surface, (155, 155, 155), r)
            if 1 in self.newbuttons:
                other.GAMESTATE = 1
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