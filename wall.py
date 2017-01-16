import pygame

import spriteanim
import spritesheet


# WAll class, I.E. platforms
class Wall(pygame.sprite.DirtySprite):
    def __init__(self, x, y, image, type=5, region=(0, 0)):
        pygame.sprite.DirtySprite.__init__(self)

        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.type = type
        self.region = region
        self.aroundregions = (region[0] - 1, region[0]), (region[0] - 1, region[0] - 1), (
            region[0] - 1, region[0] - 1), (region[0] - 1, region[0] - 1)

        self.image = image  # ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        # self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

class TWall(pygame.sprite.DirtySprite):
    def __init__(self, x, y,):
        pygame.sprite.DirtySprite.__init__(self)
        self.rect = (x,y,32,32)
        return


# Must be longer than 0, but shorter than 512
class longWall(pygame.sprite.Sprite):
    def __init__(self, x, y, width=512):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/FallenPillar.png')

        self.width = width
        self.height = 32

        self.image = ss.image_at((0, 0, self.width, 32), (254, 254, 254)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return


# walls that kill on impact
class deathWall(Wall):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.type = 0

        self.image = image
        # self.image = pygame.transform.rotate(self.image, random.randrange(0,360, 90))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return


# walls that teleport
class teleWall(Wall):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.n = 0
        self.strips = [
            spriteanim.SpriteStripAnim('./assets/images/telewall_sheet.png', (0, 0, 32, 32), 8, 1, True, 60)
        ]
        # self.strips[self.n].iter()
        # self.image = self.strips[self.n].next()

        self.image = image  # ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        # self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

    def iterate(self):
        self.image = self.strips[self.n].next()


class teleWall2(teleWall):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
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

        self.image = image  # ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        # self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return


class upWall(Wall):
    def __init__(self, x, y, image, type= 12):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.type = type
        self.image = image  # ss.image_at((0, 0, 32, 32), (254, 254, 254)).convert_alpha()
        # self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return


class Pillar(Wall):
    def __init__(self, x, y, height=512):
        pygame.sprite.Sprite.__init__(self)
        ss = spritesheet.spritesheet('./assets/images/Pillar.png')

        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

        self.image = ss.image_at((0, 0, 32, height), (254, 254, 254)).convert_alpha()
        # self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return


class invWall(Wall):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)

        self.width = 32
        self.height = 32

        self.image = image  # ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        # self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = pos[0]
        self.rect.x = pos[1]
        return


class Finish(Wall):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

        self.image = image  # ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        # self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return


# clears wall from stage
def clearwalls(thing):
    for _ in thing.deathwalls:
        if thing.deathwalls.has(_):
            thing.deathwalls.remove(_)
    for _ in thing.upwalls:
        if thing.upwalls.has(_):
            thing.upwalls.remove(_)
    for _ in thing.hitwalls:
        if thing.hitwalls.has(_):
            thing.hitwalls.remove(_)


def cleartel(thing):
    for _ in thing.telewalls:
        if thing.telewalls.has(_):
            thing.telewalls.remove(_)
    for _ in thing.telewalls2:
        if thing.telewalls2.has(_):
            thing.telewalls2.remove(_)
