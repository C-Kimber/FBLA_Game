import math
import pygame
from fragment import *
import fragment
import spritesheet
import random
import other

#Player 1 Class
class Player(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.state = "NORMAL" #STATE INCLUDE: NORMAL, DYING, WINNING, STARTING
        self.xvel = 0
        self.yvel = 0

        self.hitHeightVel = False
        self.onGround = False
        self.dir = "right"
        self.name = "p1"

        self.width = 32
        self.height = 32
        self.color = (255,255,255)
        self.region = (0.0, 1.0)
        self.oldregion =(0.0, 1.0)

        self.image = image
        self.imageH = image
        #self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.spawnx =  288
        self.spawny = 128
        self.rect.y = self.spawny
        self.rect.x = self.spawnx

        self.walls = None
        self.deaths = None
        self.teles = None
        self.teles2 = None
        self.upwalls = None
        self.finish = None
        self.otherplayers = pygame.sprite.Group()

        self.down = False

        self.jumps = 1

        self.stunting = False
        self.mass = 100 #at mass 190, goes down through walls
        self.xmom = 0
        self.ymom = 0

        self.maxyvel = 15 #* (self.mass / 100)
        self.maxxvel = 11
        self.fimgs = None

        self.alive = True

        self.teletime = 0
        self.data = None

    def moveLeft(self):
        self.dir = "left"
        if self.xvel > 3:
            self.xvel += .3
        self.xvel -= .5

    def moveDown(self):
        self.down = True

    def moveRight(self):
        self.dir = "right"
        if self.xvel < -3:
            self.xvel -= .3
        self.xvel += .5

    def jump(self):
        if self.jumps > 0:

            #if self.onGround == True:
            self.onGround = False
            self.dir = "up"
            self.rect.y -= 1
            self.yvel = 15
            self.jumps = 0

        return

    def stunt(self):
        self.down = True
        #if self.onGround == True:

        self.yvel -= 13

        return

    def update(self):

        highbound, lowbound, leftbound, rightbound = -33, other.TOTAL_LEVEL_HEIGHT, 32, other.TOTAL_LEVEL_WIDTH
        self.xmom = self.xvel * self.mass/64
        self.ymom = self.yvel * self.mass/64
        #self.playerCollisions()


        #teleportion time
        if self.teletime > 0:
            self.teletime -= 1

        self.applyDrag("air")

        #movement control

        #x velocity control
        if self.xvel > self.maxxvel:
            self.xvel = self.maxxvel
        if self.xvel < -self.maxxvel:
            self.xvel = -self.maxxvel
        if self.xvel < 0.21 and self.xvel > -0.21:
            self.xvel = 0.0

        #y velocity control
        if self.yvel > self.maxyvel:
            self.yvel = self.maxyvel
            self.hitHeightVel = True
        elif self.yvel < -self.maxyvel:
            self.yvel = -self.maxyvel

        self.getRegion()
        self.rect.x += self.xvel
        self.wallColl(self.xvel, 0, self.walls)
        self.rect.y -= self.yvel
        self.onGround = False
        self.wallColl(0, self.yvel, self.walls)


        self.wallCollisions()
        if self.otherplayers!= None:self.playerCollisions()

        #gravity
        if self.onGround == False:
            self.yvel-=.0066*self.mass

        self.boundries(highbound, lowbound, leftbound, rightbound)

        self.down = False
        return
    #stays onscreen
    def boundries(self, highbound, lowbound, leftbound, rightbound):
        if self.rect.x - 33 + self.width >= rightbound:
            self.rect.x = rightbound - self.width + 32
            self.xvel = 0
        elif self.rect.x <= leftbound:
            self.rect.x = leftbound + 1
            self.xvel = 0
        if self.rect.y >= lowbound+32:
            self.rect.y -= 3
            self.state = "DYING"


            #self.yvel = 0
        elif self.rect.y <= highbound:
            self.yvel = 0
            self.rect.y += 1


        return

    def playerCollisions(self):
        if self.otherplayers != None:
            hit_bros =  pygame.sprite.spritecollide(self, self.otherplayers, False)
            for bro in hit_bros:

                for _ in range(random.randint(5,20)):
                    fragment.fragmentgroup.add(custFrag((self.rect.centerx, self.rect.centery), (1, 3), (255, 255, 0)))


                if bro.rect.y - self.rect.y >= 1:  # if p1 is above p2
                        self.rect.bottom = bro.rect.top
                        if self.onGround == False:
                            bro.yvel = self.ymom
                        else:
                            bro.yvel = .2
                        self.yvel = 12
                        if bro.yvel > bro.maxyvel:
                            bro.yvel = bro.maxyvel/3
                        elif bro.yvel < -bro.maxyvel:
                            bro.yvel = -bro.maxyvel/3



                bro.xvel = self.xmom
                bro.rect.x +=1

                self.xvel = 0
            #else:
            #    self.onGround = False

    #Collisions with walls
    def wallColl(self, xvel, yvel, colliders):
        for collider in colliders:
            distance = math.sqrt((self.rect.x - collider.x) ** 2 + (self.rect.y - collider.rect.y) ** 2)
            if distance < 160:
                if pygame.sprite.collide_rect(self, collider):
                    if xvel > 0:
                        self.rect.right = collider.rect.left
                        self.xvel = 0
                    if xvel < 0:
                        self.rect.left = collider.rect.right
                        self.xvel = 0
                    if yvel < 0:
                        self.rect.bottom = collider.rect.top
                        self.onGround = True
                        self.jumps = 3
                        self.yvel = 0
                    if yvel > 0:
                        self.yvel = 0
                        self.rect.top = collider.rect.bottom
        return


    def wallCollisions(self):

        if pygame.sprite.spritecollide(self, self.deaths, False):

            self.die()

        hit_teles2 = pygame.sprite.spritecollide(self, self.teles2, False)
        hit_teles = pygame.sprite.spritecollide(self, self.teles, False)
        if self.teletime == 0:
            for tell2 in hit_teles2:
                for tell in self.teles:
                    self.rect.x = tell.rect.x
                    self.rect.y = tell.rect.y
                    self.teletime = 10
                    break
            for tell in hit_teles:
                for tell2 in self.teles2:
                    self.rect.x =  tell2.rect.x
                    self.rect.y = tell2.rect.y
                    self.teletime = 10
                    break

        hit_ups = pygame.sprite.spritecollide(self, self.upwalls, False)
        for up in hit_ups:
            if self.down == True:
                #self.rect.top = up.rect.bottom-4
                continue


            elif self.rect.bottom > up.rect.top and self.rect.bottom < up.rect.top+10 and self.yvel < 0:
                self.yvel = 0
                self.rect.bottom = up.rect.top+1
                self.onGround = True
                self.jumps = 1

    #death by explosion
    def getfimage(self, images):
        self.fimgs = images

    def die(self):
        for _ in range(random.randint(8,24)):
            fragment.fragmentgroup.add(Fragment((self.rect.x, self.rect.y), random.choice(self.fimgs)))
        if other.GAMESTATE == 2:
            self.state = "DYING"
            self.yvel = 15
        else:
            self.alive = False
            self.rect.x = self.spawnx
            self.rect.y = self.spawny


    def dying(self, a):
        self.rect.y -= self.yvel
        self.yvel -= .0066 * self.mass
        self.image = pygame.transform.rotate(self.imageH, math.floor(self.yvel*10))

        if self.rect.top > other.TOTAL_LEVEL_WIDTH+96:
            self.alive = False
            self.yvel = 0
            self.xvel = 0
            self.rect.x = self.spawnx
            self.rect.y = self.spawny
            self.state = "STARTING_B"
            self.image = self.imageH
            print "PLAYER HAS DIED"
        return

    def beatLvl(self, data):
        self.rect.y += self.yvel
        self.rect.x += self.xvel
        self.yvel -= .0066 * self.mass
        self.image = pygame.transform.rotozoom(self.image, math.floor(self.yvel*.25), .97)
        if self.yvel < -30:
            print "LEVEL COMPLETE"
            self.yvel = 0
            self.xvel = 0
            self.rect.x = self.spawnx
            self.rect.y = self.spawny
            self.state = "STARTING_G"
            self.image = self.imageH
            data.newMainLev()


    def applyDrag(self, medium):
        a = 0.003
        n = self.xvel * -1.0
        if self.xvel > 0.0:
            drag = math.floor(n* a)/ 5
        else:
            drag = math.ceil(n * a)/5


        self.xvel += drag

    def getRegion(self):
        self.region = math.floor((self.rect.right+self.rect.left)/(864*2)),math.floor((self.rect.top+self.rect.bottom)/(864*2))
        print self.region
        if self.region != self.oldregion:
            print "NEW REGION: " + str(self.region)
            self.data.getCollidables(self.region)
            self.oldregion = self.region

        return





class Player2(Player):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.xvel = 0
        self.yvel = 0
        self.maxyvel = 15
        self.maxxvel = 11
        self.hitHeightVel = False
        self.onGround = False
        self.dir = "left"
        self.name = "p2"

        self.width = 32
        self.height = 32
        self.color = (255,255,255)

        self.image = image#ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        self.fimgs = None

        self.rect = self.image.get_rect()
        self.spanwx = 400
        self.spawny = 400
        self.rect.y = self.spawny
        self.rect.x = self.spanwx

        self.walls = None
        self.deaths = None
        self.teles = None
        self.teles2 = None
        self.otherplayers = pygame.sprite.Group()


        self.jumps = 1

        self.stunting = False
        self.xmom = 0
        self.ymom = 0
        self.mass = 100
        self.alive = True

        self.teletime = 0

        return

#goes on underside, and stays
"""
for up in hit_ups:
            if self.down == True:
                self.rect.top = up.rect.bottom-8
                self.yvel = 3

            elif self.yvel < 0:
                self.yvel = 0
                self.rect.bottom = up.rect.top + 8
                self.onGround = True
                self.jumps = 1"""




class Empty(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        return

