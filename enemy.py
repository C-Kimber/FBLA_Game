import random

import pygame
import math
import other



class Base(pygame.sprite.Sprite):

    def __init__(self, pos, image=pygame.Surface((32,32))):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.xvel = 0
        self.yvel = 0
        self.state = "NORMAL"

        self.hitHeightVel = False
        self.onGround = False
        self.dir = "right"
        self.name = "p1"
        self.zed = 0

        self.width = 32
        self.height = 32
        self.color = (255, 255, 255)

        self.image = image
        self.imageH = image

        #self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.spanwx = pos[0]
        self.spawny = pos[1]
        self.rect.y = self.spawny
        self.rect.x = self.spanwx

        self.walls = None
        self.deaths = None

        self.otherplayers = pygame.sprite.Group()

        self.down = False

        self.jumps = 1



        self.maxyvel = 15  # * (self.mass / 100)
        self.maxxvel = 11

        self.alive = True

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
            # if self.onGround == True:
            self.onGround = False
            self.dir = "up"
            self.rect.y -= 1
            self.yvel = 15
            self.jumps = 0

        return

    def stunt(self):
        self.down = True
        # if self.onGround == True:

        self.yvel -= 13

        return

    def update(self):
        highbound, lowbound, leftbound, rightbound = -33, other.TOTAL_LEVEL_WIDTH, 0, other.TOTAL_LEVEL_HEIGHT
        if self.state == 'NORMAL':
            self.applyDrag("air")
            # movement control

            # x velocity control
            if self.xvel > self.maxxvel:
                self.xvel = self.maxxvel
            if self.xvel < -self.maxxvel:
                self.xvel = -self.maxxvel
            if self.xvel < 0.21 and self.xvel > -0.21:
                self.xvel = 0.0

            # y velocity control
            if self.yvel > self.maxyvel:
                self.yvel = self.maxyvel
                self.hitHeightVel = True
            elif self.yvel < -self.maxyvel:
                self.yvel = -self.maxyvel

            self.rect.x += self.xvel
            #self.wallColl(self.xvel, 0, self.walls)
            self.rect.y -= self.yvel
            self.onGround = False
            #self.wallColl(0, self.yvel, self.walls)

            #self.wallCollisions()
            #if self.otherplayers != None: self.playerCollisions()

            # gravity
            if self.onGround == False:
                self.yvel -= .66# * self.mass

            self.boundries(highbound, lowbound, leftbound, rightbound)
            self.down = False
        elif self.state == "DYING":
            self.die()
        return

    # stays onscreen
    def boundries(self, highbound, lowbound, leftbound, rightbound):
        if self.rect.x - 33 + self.width >= rightbound:
            self.rect.x = rightbound - self.width + 32
            self.xvel = 0
        elif self.rect.x <= leftbound:
            self.rect.x = leftbound + 1
            self.xvel = 0
        if self.rect.y >= lowbound - 96:
            self.rect.y -= 3
            self.state = "DYING"
            self.yvel = 10
            self.xvel = random.randrange(-6,6,2)


            # self.yvel = 0
        elif self.rect.y <= highbound:
            self.yvel = 0
            self.rect.y += 1

        return


    # Collisions with walls
    def wallColl(self, xvel, yvel, colliders):
        for collider in colliders:
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


    def die(self):
        self.zed += .02
        self.rect.y -= self.yvel
        self.rect.x += self.xvel

        self.yvel -= .66
        #self.image = pygame.transform.rotate(self.imageH, math.floor(self.yvel*10))
        self.image = pygame.transform.rotozoom(self.imageH, math.floor(self.yvel), 1+self.zed*self.xvel/6)
        # like throwing at player ##self.image = pygame.transform.rotozoom(self.imageH, math.floor(self.yvel), -self.yvel / 10)
        if self.rect.top > other.TOTAL_LEVEL_WIDTH + 96:
            self.alive = False
            self.yvel = 0
            self.xvel = 0

        return

    def applyDrag(self, medium):
        a = 0.003
        n = self.xvel * -1.0
        if self.xvel > 0.0:
            drag = math.floor(n * a) / 5
        else:
            drag = math.ceil(n * a) / 5

        self.xvel += drag

