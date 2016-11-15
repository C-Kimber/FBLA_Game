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
        self.width =32
        self.height = 32

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255))
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

        self.x = x
        self.y = y
        self.width = width
        self.height = 32

        self.image = ss.image_at((0, 0, self.width, 32), (255, 255, 255))
        # self.image.fill((255,255,0))

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

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255))
        #self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

#chooses random level, and clears walls from the stage
def randomLevel(thing):

    n = 2#random.randint(0,6)
    for _ in thing.deathwalls:
        if thing.deathwalls.has(_):
            thing.deathwalls.remove(_)

    return levels(thing, n)


#each number is a different level
def levels(thing, number):
    if number == 1:
        thing.wall_list.add(longWall(0, 200, 256))
        thing.all_sprites.add(longWall(0, 200, 256))

        thing.wall_list.add(longWall(600, 400, 256))
        thing.all_sprites.add(longWall(600, 400,256))

        thing.wall_list.add(Wall(400, 300))
        thing.all_sprites.add(Wall(400, 300))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))
    elif number == 2:
        thing.wall_list.add(Wall(0, 286))
        thing.all_sprites.add(Wall(0, 286))

        thing.wall_list.add(Wall(600, 286))
        thing.all_sprites.add(Wall(600, 286))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))
    elif number == 3:

        thing.wall_list.add(Wall(200, 300))
        thing.all_sprites.add(Wall(200, 300))

        thing.wall_list.add(Wall(590, 300))
        thing.all_sprites.add(Wall(580, 300))

        thing.deathwalls.add(deathWall(thing.width-10, 0))
        thing.all_sprites.add(deathWall(thing.width-10, 0))

        thing.deathwalls.add(deathWall(0, 0))
        thing.all_sprites.add(deathWall(0, 0))

        thing.deathwalls.add(deathWall(0, 0))
        thing.all_sprites.add(deathWall(0, 0))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))
    elif number == 4:
        thing.deathwalls.add(deathWall(0, thing.height - 10))
        thing.all_sprites.add(deathWall(0, thing.height - 10))

        thing.wall_list.add(Wall(100, thing.height-11))
        thing.all_sprites.add(Wall(100, thing.height-11))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))
    elif number == 5:
        thing.wall_list.add(Wall(100, thing.height - 200))
        thing.all_sprites.add(Wall(100, thing.height - 200))

        thing.deathwalls.add(deathWall(thing.width / 2, 57))
        thing.all_sprites.add(deathWall(thing.width / 2,57))

        thing.deathwalls.add(deathWall(100, 100))
        thing.all_sprites.add(deathWall(100, 100))

        thing.deathwalls.add(deathWall(700, 100))
        thing.all_sprites.add(deathWall(700, 100))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))

    else:

        thing.wall_list.add(longWall(120+(40), 286))
        thing.all_sprites.add(longWall(120+(40), 286))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x*32, thing.height - 32))
            thing.all_sprites.add(deathWall(x*32, thing.height - 32))

