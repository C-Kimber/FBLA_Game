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

        self.x = x
        self.y = y
        self.width = width
        self.height = 32

        self.image = ss.image_at((0, 0, self.width, 32), (255, 255, 255)).convert_alpha()
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

        self.image = ss.image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha()
        #self.image.fill((255, 20, 0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        return

#chooses random level, and clears walls from the stage
def randomLevel(thing):

    n =random.randint(0,6)
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
        thing.wall_list.add(longWall(0, 286, 220))
        thing.all_sprites.add(longWall(0, 286, 220))

        thing.wall_list.add(longWall(600, 286, 256))
        thing.all_sprites.add(longWall(600, 286, 256))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))
    elif number == 3:

        thing.wall_list.add(Wall(160, 300))
        thing.all_sprites.add(Wall(160, 300))

        thing.wall_list.add(Wall(590, 300))
        thing.all_sprites.add(Wall(580, 300))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(0, x*32))
            thing.all_sprites.add(deathWall(0, x*32))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(thing.width-32, x*32))
            thing.all_sprites.add(deathWall(thing.width-32, x*32))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))
    elif number == 4:
        for x in range(0, 4):
            thing.deathwalls.add(deathWall(thing.width/2-16, x*32+thing.height - 128))
            thing.all_sprites.add(deathWall(thing.width/2-16 , x*32+thing.height - 128))


        thing.wall_list.add(longWall(192, thing.height-32,224))
        thing.all_sprites.add(longWall(160, thing.height - 32,224))

        thing.wall_list.add(longWall(416, thing.height - 32,192))
        thing.all_sprites.add(longWall(416, thing.height - 32,224))


        for x in range(0, 7):
            thing.deathwalls.add(deathWall((x * 32)+640, thing.height - 32))
            thing.all_sprites.add(deathWall((x * 32)+640, thing.height - 32))
        for x in range(0, 5):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))

    elif number == 5:
        thing.wall_list.add(longWall(128, thing.height - 192,512))
        thing.all_sprites.add(longWall(128, thing.height - 192,512))

        for x in range(0,10):
            thing.deathwalls.add(deathWall(thing.width / 2-32, 64+x*32))
            thing.all_sprites.add(deathWall(thing.width / 2-32,64+x*32))
        for x in range(0, 12):
            thing.deathwalls.add(deathWall(96, 96+x*32))
            thing.all_sprites.add(deathWall(96, 96+x*32))
        for x in range(0, 12):
            thing.deathwalls.add(deathWall(640, 96+x*32))
            thing.all_sprites.add(deathWall(640,  96+x*32))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x * 32, thing.height - 32))
            thing.all_sprites.add(deathWall(x * 32, thing.height - 32))

    else:

        thing.wall_list.add(longWall(120+(40), 286))
        thing.all_sprites.add(longWall(120+(40), 286))

        for x in range(0, 32):
            thing.deathwalls.add(deathWall(x*32, thing.height - 32))
            thing.all_sprites.add(deathWall(x*32, thing.height - 32))

