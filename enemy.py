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
        self.dir = "LEFT"
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
        self.player = None

        self.otherplayers = pygame.sprite.Group()

        self.down = False

        self.jumps = 1



        self.maxyvel = 15  # * (self.mass / 100)
        self.maxxvel = 3

        self.alive = True

    def moveLeft(self):

        self.xvel -= .5

    def moveDown(self):
        self.down = True

    def moveRight(self):
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


    def update(self):
        highbound, lowbound, leftbound, rightbound = -33, other.TOTAL_LEVEL_HEIGHT, 32, other.TOTAL_LEVEL_WIDTH


        if self.state == 'NORMAL':
            distance = math.sqrt((self.player.rect.x - self.rect.x) ** 2 + (self.player.rect.y - self.rect.y) ** 2)
            if distance < 500:
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
                self.wallColl(self.xvel, 0, self.walls)
                self.rect.y -= self.yvel
                self.onGround = False
                self.wallColl(0, self.yvel, self.walls)

                self.wallCollisions()
                self.playerColl()
                #if self.otherplayers != None: self.playerCollisions()

                # gravity
                if self.onGround == False:
                    self.yvel -= .66# * self.mass

                self.boundries(highbound, lowbound, leftbound, rightbound)
                self.movementAI()
                self.down = False


        elif self.state == "DYING":
            self.dying()
        return

    def wallCollisions(self):

        if pygame.sprite.spritecollide(self, self.deaths, False):
            self.rect.y -= 3
            self.state = "DYING"
            self.die(10,(2-random.randrange(-4, 8, 2)))

        """hit_teles2 = pygame.sprite.spritecollide(self, self.teles2, False)
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
                    self.rect.x = tell2.rect.x
                    self.rect.y = tell2.rect.y
                    self.teletime = 10
                    break

        hit_ups = pygame.sprite.spritecollide(self, self.upwalls, False)
        for up in hit_ups:
            if self.down == True:
                # self.rect.top = up.rect.bottom-4
                continue


            elif self.rect.bottom > up.rect.top and self.rect.bottom < up.rect.top + 10 and self.yvel < 0:
                self.yvel = 0
                self.rect.bottom = up.rect.top + 1
                self.onGround = True
                self.jumps = 1"""

    def movementAI(self):
        if self.dir == "LEFT":
            self.moveLeft()
        elif self.dir == "RIGHT":
            self.moveRight()

    def playerColl(self):
        if pygame.sprite.collide_rect(self, self.player):
            if self.player.rect.bottom < self.rect.bottom-16:
                self.player.jumps = 1
                self.player.yvel = 5

                self.die((random.randrange(-6, 6, 2)),7)
            else:
                self.player.die()
    # stays onscreen
    def boundries(self, highbound, lowbound, leftbound, rightbound):
        if self.rect.x - 33 + self.width >= rightbound:
            self.rect.x = rightbound - self.width + 32
            self.dir = "LEFT"
            self.xvel *= -1
        elif self.rect.x <= leftbound:
            self.dir = "RIGHT"
            self.rect.x = leftbound + 1
            self.xvel  *= -1
        if self.rect.y >= lowbound + 96:
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
        if self.walls != None:
            for collider in colliders:

                    if pygame.sprite.collide_rect(self, collider):
                        if xvel > 0:
                            self.rect.right = collider.rect.left
                            self.xvel = 0
                            self.dir = "LEFT"
                        if xvel < 0:
                            self.rect.left = collider.rect.right
                            self.xvel = 0
                            self.dir = "RIGHT"
                        if yvel < 0:
                            self.rect.bottom = collider.rect.top
                            self.onGround = True
                            self.jumps = 3
                            self.yvel = 0
                        if yvel > 0:
                            self.yvel = 0
                            self.rect.top = collider.rect.bottom

        return

    def die(self,xvel,yvel):
        if xvel == 0:
            xvel = -2
        self.xvel = xvel
        self.yvel = yvel
        self.state = "DYING"

    def dying(self):
        self.zed += .02
        self.rect.y -= self.yvel
        self.rect.x += self.xvel

        self.yvel -= .66
        #self.image = pygame.transform.rotate(self.imageH, math.floor(self.yvel*10))
        self.image = pygame.transform.rotozoom(self.imageH, math.floor(self.zed*-200*other.unitNum(self.xvel)), 1+self.zed*self.xvel/6)
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

