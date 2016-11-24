import pygame
from fragment import Fragment
import fragment
import spritesheet
import random
import other

#Player 1 Class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/Player1_small.png')


        self.xvel = 0
        self.yvel = 0
        self.maxyvel = 15
        self.maxxvel = 11
        self.hitHeightVel = False
        self.onGround = False

        self.width = 32
        self.height = 32
        self.color = (255,255,255)

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()


        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.rect.x = 400

        self.walls = None
        self.deaths = None
        self.teles = None
        self.teles2 = None
        self.upwalls = None

        self.down = False

        self.jumps = 1

        self.stunting = False

        self.pushing = 0
        self.pushfactor = 1.25

        self.alive = True

        self.teletime = 0


    def update(self):
        highbound, lowbound, leftbound, rightbound = 0, other.TOTAL_LEVEL_WIDTH, 0, other.TOTAL_LEVEL_HEIGHT
        self.boundries(highbound, lowbound, leftbound, rightbound)

        self.pushing = self.yvel * self.pushfactor
        self.jumps = 1
        self.onGround = True


        self.wallCollisions()
        self.down = False

        #teleportion time
        if self.teletime > 0:
            self.teletime -= 1

        #movement control
        self.rect.x += self.xvel
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
        self.yvel-=.66
        #if self.yvel != 0:
         #   self.onGround = False
        return
    #stays onscreen
    def boundries(self, highbound, lowbound, leftbound, rightbound):
        if self.rect.x + self.width >= rightbound:
            self.rect.x = rightbound - self.width - 1
            self.xvel = 0
        elif self.rect.x <= leftbound:
            self.rect.x = leftbound + 1
            self.xvel = 0
        if self.rect.y >= lowbound:
            self.alive = False

            self.yvel = 0
        return

    #Collisions with walls
    def wallCollisions(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            block.t = False
            block.d = False

            if self.yvel < 0:  # falling down
                if self.rect.bottom >= block.rect.top:  # from top of block down
                    if self.rect.bottom <= block.rect.top + 15:  # from top of block + 10 up
                        self.yvel = 0
                        self.rect.bottom = block.rect.top + 1
                        self.onGround = True
                        self.jumps = 1
                        block.t = True

            elif self.yvel > 0:#going up
                if self.rect.top <= block.rect.bottom: #from bottom of block up
                    if self.rect.top >= block.rect.bottom-15:#from bottom of bock -10 down
                        self.rect.top = block.rect.bottom
                        self.yvel = 0
                        block.d = True


            if self.xvel <0 and block.t==False and block.d == False:#
                if self.rect.right >= block.rect.left:# and self.rect.right <= block.rect.left+5:
                    if self.rect.bottom < block.rect.bottom or self.rect.top > block.rect.top:
                        self.rect.left -= -2
                        self.xvel = 0

            elif self.xvel > 0 and block.t==False and block.d ==False:
                if self.rect.left <= block.rect.right:
                    #if self.rect.right >= block.rect.left-5:
                    self.rect.right -= 2
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
    def die(self):
        for _ in range(random.randint(8,24)):
            fragment.fragmentgroup.add(Fragment((self.rect.x, self.rect.y)))
        self.alive = False


    def moveLeft(self):
        if self.xvel > 3:
            self.xvel += .3
        self.xvel -= .5

    def moveDown(self):
        self.down = True

    def moveRight(self):
        if self.xvel < -3:
            self.xvel -= .3
        self.xvel += .5

    def jump(self):
        if self.jumps >0:
            if self.onGround:
                if not self.hitHeightVel:
                    self.rect.y -=5
                    self.yvel = 15
                    self.jumps = 0
        return

    def stunt(self):
        #if not self.onGround:
        self.yvel -= 3
        return


class Player2(Player):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/Player2_small.png')

        self.xvel = 0
        self.yvel = 0
        self.maxyvel = 15
        self.maxxvel = 11
        self.hitHeightVel = False
        self.onGround = False

        self.width = 32
        self.height = 32
        self.color = (255,255,255)

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()


        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.rect.x =400

        self.walls = None
        self.deaths = None
        self.teles = None
        self.teles2 = None

        self.jumps = 1

        self.stunting = False

        self.pushfactor = 1.25
        self.pushing = 0
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



