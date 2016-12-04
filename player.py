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


        self.xvel = 0
        self.yvel = 0

        self.hitHeightVel = False
        self.onGround = False
        self.dir = "right"

        self.width = 32
        self.height = 32
        self.color = (255,255,255)

        self.image = image
        #self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.spanwx = 400
        self.spawny = 400
        self.rect.y = self.spawny
        self.rect.x = self.spanwx

        self.walls = None
        self.deaths = None
        self.teles = None
        self.teles2 = None
        self.upwalls = None
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
            if self.onGround:
                if not self.hitHeightVel:
                    self.dir = "up"
                    self.yvel = 15
                    self.jumps = 0
        return

    def stunt(self):
        self.down = True
        #if self.onGround == True:

        self.yvel -= 13

        return

    def update(self):
        highbound, lowbound, leftbound, rightbound = -33, other.TOTAL_LEVEL_WIDTH, 0, other.TOTAL_LEVEL_HEIGHT

        self.xmom = self.xvel * self.mass/64
        self.ymom = self.yvel * self.mass/64
        #self.playerCollisions()


        #teleportion time
        if self.teletime > 0:
            self.teletime -= 1

        #movement control
        self.rect.x += self.xvel
        if self.dir == "up":
            self.rect.y -= self.yvel*1.1
        else:
            self.rect.y -= self.yvel
        #x velocity control
        if self.xvel > self.maxxvel:
            self.xvel = self.maxxvel
        if self.xvel < -self.maxxvel:
            self.xvel = -self.maxxvel
        if self.xvel >=.1:
            self.xvel -=.1
        if self.xvel <= -.1:
            self.xvel += .1

        #y velocity control
        if self.yvel > self.maxyvel:
            self.yvel = self.maxyvel
            self.hitHeightVel = True
        elif self.yvel < -self.maxyvel:
            self.yvel = -self.maxyvel

        #gravity
        self.yvel-=.0066*self.mass
        #if self.yvel != 0:
         #   self.onGround = False
        self.wallCollisions()
        self.playerCollisions()

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
        if self.rect.y >= lowbound:
            self.die()

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
                        #self.yvel = 12
                        if self.onGround == False:
                            bro.yvel = self.ymom
                        #else:s
                        self.yvel = 12
                        bro.yvel -= 3


                bro.xvel = self.xmom

                self.xvel = 0

    #Collisions with walls
    def wallCollisions(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:


            if self.rect.bottom >= block.rect.top and self.rect.bottom <= block.rect.top + 15:  # Moving down; Hit the top side of the wall
                if self.rect.right > block.rect.left:
                    self.rect.bottom = block.rect.top
                    self.yvel = 0
                    self.onGround = True
                    self.jumps = 1
            elif self.rect.top <= block.rect.bottom and self.rect.top >= block.rect.bottom - 15:  # Moving up; Hit the bottom side of the wall
                self.rect.top = block.rect.bottom
                self.yvel = 0
            elif self.rect.right >= block.rect.left and self.rect.right <= block.rect.left + 15:  # Moving right; Hit the left side of the wall
                if self.rect.bottom > block.rect.top+15:
                    self.rect.right = block.rect.left#+1
                    self.xvel = 0
            elif self.rect.left <= block.rect.right and self.rect.left >= block.rect.right - 15:  # Moving left; Hit the right side of the wall
                self.rect.left = block.rect.right#-1
                self.xvel = 0




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
        self.alive = False
        self.rect.x = self.spanwx
        self.rect.y = self.spawny






class Player2(Player):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/Player2_small.png')

        self.xvel = 0
        self.yvel = 0
        self.maxyvel = 15
        self.maxxvel = 11
        self.hitHeightVel = False
        self.onGround = False
        self.dir = "left"

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

