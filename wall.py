import pygame
import random
import spritesheet
import spriteanim

#WAll class, I.E. platforms
class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/wall1_small.png')

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
        ss = spritesheet.spritesheet('./assets/images/wall1_small_long.png')

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
        ss = spritesheet.spritesheet('./assets/images/deathwall1_small.png')
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        self.image = pygame.transform.rotate(self.image, random.randrange(0,360, 90))
        #self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return
#walls that teleport
class teleWall(Wall):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/telewall_sheet.png')
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.n = 0
        self.strips = [
            spriteanim.SpriteStripAnim('./assets/images/telewall_sheet.png', (0, 0, 32, 32), 8, 1, True, 60)
        ]
        #self.strips[self.n].iter()
        #self.image = self.strips[self.n].next()

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        # self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

    def iterate(self):
        self.image = self.strips[self.n].next()


class teleWall2(teleWall):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/telewall2_sheet.png')
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.n = 0
        self.strips = [
            spriteanim.SpriteStripAnim('./assets/images/telewall2_sheet.png', (0, 0, 32, 32), 8, 1, True, 60)
        ]
        # self.strips[self.n].iter()
        # self.image = self.strips[self.n].next()

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        # self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

class upWall(Wall):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/upwall.png')

        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

        self.image = ss.image_at((0, 0, 32, 32), (254, 254, 254)).convert_alpha()
        #self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

class Pillar(Wall):
    def __init__(self,x,y,height=512):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/wall1_small_tall.png')

        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

        self.image = ss.image_at((0, 0, 32, height), (255, 255, 255)).convert_alpha()
        # self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return



#clears wall from stage
def clearwalls(thing):
    for _ in thing.deathwalls:
        if thing.deathwalls.has(_):
            thing.deathwalls.remove(_)
    for _ in thing.upwalls:
        if thing.upwalls.has(_):
            thing.upwalls.remove(_)

def cleartel(thing):
    for _ in thing.telewalls:
        if thing.telewalls.has(_):
            thing.telewalls.remove(_)
    for _ in thing.telewalls2:
        if thing.telewalls2.has(_):
            thing.telewalls2.remove(_)




