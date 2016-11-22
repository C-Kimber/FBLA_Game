import pygame
from fragment import Fragment
import fragment
import spritesheet

#Player 1 Class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/Player1_small.png')


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

        self.jumps = 1

        self.stunting = False

        self.pushing = 0
        self.pushfactor = 1.25

        self.alive = True


    def update(self):
        highbound, lowbound, leftbound, rightbound = 0, 800, 0, 800
        self.boundries(highbound, lowbound, leftbound, rightbound)

        self.pushing = self.yvel * self.pushfactor

        self.wallCollisions()

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
            if self.rect.right == block.rect.left:
                self.rect.right = block.rect.left
                self.xvel = 0
            if self.rect.left == block.rect.right:
                self.rect.left = block.rect.right
                self.xvel = 0

            if self.yvel < 0:
                self.rect.bottom = block.rect.top
                self.onGround = True
                self.jumps = 1
                self.yvel = 0
            else:
                self.rect.top = block.rect.bottom
                self.yvel = 0

        if pygame.sprite.spritecollide(self, self.deaths, False):
            self.die()
    #death by explosion
    def die(self):
        for _ in range(35):
            fragment.fragmentgroup.add(Fragment((self.rect.x, self.rect.y)))
        self.alive = False


    def moveLeft(self):
        if self.xvel > 3:
            self.xvel += .3
        self.xvel -= .5

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
        ss = spritesheet.spritesheet('./assets/Player2_small.png')

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

        self.jumps = 1

        self.stunting = False

        self.pushfactor = 1.25
        self.pushing = 0
        self.alive = True


        return




