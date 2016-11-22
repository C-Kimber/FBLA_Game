import pygame
import random
import spritesheet


#WAll class, I.E. platforms
class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/wall1_small.png')

        self.x = x
        self.y = y
        self.width =30
        self.height = 30

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        #self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return
#Must be longer than 0, but shorter than 512
class longWall(pygame.sprite.Sprite):
    def __init__(self, x, y, width=512):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/wall1_small_long.png')

        self.width = width
        self.height = 32

        self.image = ss.image_at((0, 0, self.width, 32), (255, 255, 255)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

#walls that kill on impact
class deathWall(Wall):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/deathwall1_small.png')
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        #self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

#clears wall from stage
def clearwalls(thing):
    for _ in thing.deathwalls:
        if thing.deathwalls.has(_):
            thing.deathwalls.remove(_)



