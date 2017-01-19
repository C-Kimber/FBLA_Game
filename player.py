import math

import fragment
import other
import wall
from fragment import *


# Player 1 Class
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.state = "NORMAL"  # STATE INCLUDE: NORMAL, DYING, WINNING, STARTING
        self.xvel = 0
        self.yvel = 0

        self.hitHeightVel = False
        self.onGround = False
        self.dir = "right"
        self.name = "1"

        self.width = 32
        self.height = 32
        self.color = (255, 255, 255)
        self.region = (0.0, 1.0)
        self.oldregion = (0.0, 1.0)

        self.image = image
        self.imageH = image
        self.sounds = None
        # self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.spawnx = 288
        self.spawny = 128
        self.rect.y = self.spawny
        self.rect.x = self.spawnx

        self.walls = None
        self.deaths = None
        self.teles = None
        self.teles2 = None
        self.upwalls = None
        self.finish = None
        self.items = pygame.sprite.Group()
        self.otherplayers = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()

        self.down = False

        self.jumps = 1

        self.stunting = False
        self.mass = 100  # at mass 190, goes down through walls
        self.xmom = 0
        self.ymom = 0
        self.current_chunk  = (0,1)
        self.prev_chunk = self.current_chunk

        self.maxyvel = 15  # * (self.mass / 100)
        self.maxxvel = 10
        self.fimgs = None
        self.f2imgs = None

        self.alive = True

        self.dietime = 0
        self.teletime = 0
        self.data = None

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

    def jump_cut(self):
        # print "JUMP CUTTING"
        if self.yvel > 3:
            self.yvel = 3

    def jump(self):
        if self.jumps > 0:
             if self.onGround == True:
                self.onGround = False
                self.dir = "up"
                self.rect.y -= 1
                self.yvel = 15
                self.jumps = 0

        return


    def update(self):
        if self.state != "DYING":
            highbound, lowbound, leftbound, rightbound = -33, other.TOTAL_LEVEL_HEIGHT, 32+other.WIDTH/8+32, other.TOTAL_LEVEL_WIDTH +96+ other.WIDTH/8
            self.xmom = self.xvel * self.mass / 64
            self.ymom = self.yvel * self.mass / 64
            # self.playerCollisions()


            # teleportion time
            if self.teletime > 0:
                self.teletime -= 1

            self.applyDrag("air")

            # movement control

            # x velocity control
            if self.xvel > self.maxxvel:
                self.xvel = self.maxxvel
            if self.xvel < -self.maxxvel:
                self.xvel = -self.maxxvel
            if 0.21 > self.xvel > -0.21:
                self.xvel = 0.0

            # y velocity control
            if self.yvel > self.maxyvel:
                self.yvel = self.maxyvel
                self.hitHeightVel = True
            elif self.yvel < -self.maxyvel:
                self.yvel = -self.maxyvel

            if self.dir == "up":
                if self.yvel < 0:
                    self.dir = "down"

            self.newfnction()
            self.rect.x += self.xvel
            self.wallColl(self.xvel, 0, self.collidables)
            self.rect.y -= self.yvel
            self.onGround = False
            self.wallColl(0, self.yvel, self.collidables)

            self.wallCollisions()

            if self.otherplayers is not None and other.GAMESTATE != 2: self.playerCollisions()

            # gravity
            if not self.onGround:
                self.yvel -= .0066 * self.mass

            self.boundries(highbound, lowbound, leftbound, rightbound)
            #self.getChunk()
            self.current_chunk = math.floor((self.rect.x) / (256)), math.floor(
                (self.rect.y) / 256)

            self.down = False
        else:
            self.slowdie()
            if not self.onGround:
                self.yvel -= .0066 * self.mass
            self.rect.y -= self.yvel
            self.onGround = False
            self.wallColl(0, self.yvel, self.collidables)
        return

    # stays onscreen
    def boundries(self, highbound, lowbound, leftbound, rightbound):
        if self.rect.x - 33 + self.width >= rightbound:
            self.rect.x = rightbound - self.width + 32
            self.xvel = 0
        elif self.rect.x <= leftbound:
            self.rect.x = leftbound + 1
            self.xvel = 0
        if self.rect.y >= lowbound + 128:
            self.rect.y -= 3
            random.choice((self.sounds[6], self.sounds[7])).play()
            self.die()


            # self.yvel = 0
        elif self.rect.y <= highbound:
            self.yvel = 0
            self.rect.y += 1

        return

    def playerCollisions(self):
        if self.otherplayers is not None:
            hit_bros = pygame.sprite.spritecollide(self, self.otherplayers, False)
            for bro in hit_bros:
                if bro.state != "DYING":
                    random.choice((self.sounds[0],self.sounds[1],self.sounds[2])).play()
                    for _ in range(random.randint(5, 15)):
                        fragment.fragmentgroup.add(custFrag((self.rect.centerx, self.rect.centery), (1, 3), random.choice(self.f2imgs) ))

                    if bro.rect.y - self.rect.y >= 1:  # if p1 is above p2
                        self.rect.bottom = bro.rect.top
                        if not self.onGround:
                            bro.yvel = self.ymom + 2
                        else:
                            bro.yvel = .2
                        self.yvel = 12
                        if bro.yvel > bro.maxyvel:
                            bro.yvel = bro.maxyvel / 3
                        elif bro.yvel < -bro.maxyvel:
                            bro.yvel = -bro.maxyvel / 3
                        if self.data.level_time < 0:
                            bro.image = self.data.sprite_library["rubble"]
                            bro.state = "DYING"

                    bro.xvel = self.xmom
                    self.xvel = -random.randint(3,6)* other.unitNum(self.xmom)

                    # else:
                    #    self.onGround = False

    # Collisions with walls
    def wallColl(self, xvel, yvel, colliders):
        for collider in colliders:
            if pygame.sprite.collide_rect(self, collider):
                if not isinstance(collider, wall.upWall):


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

                if not isinstance(collider, wall.deathWall):
                        if collider.type < 3:
                            if self.down:
                                # self.rect.top = up.rect.bottom-4
                                continue


                            elif self.dir != "up" and round(self.rect.centery) < collider.rect.top:
                                self.onGround = True
                                self.yvel = 0
                                self.rect.bottom = collider.rect.top
                                self.jumps = 1
                else:
                    random.choice((self.sounds[3], self.sounds[4], self.sounds[5])).play()
                    for _ in range(random.randint(8, 24)):
                        fragment.fragmentgroup.add(Fragment((self.rect.x, self.rect.y), random.choice(self.fimgs)))
                    self.die()
        return

    def wallCollisions(self):



        hit_teles2 = pygame.sprite.spritecollide(self, self.teles2, False)
        hit_teles = pygame.sprite.spritecollide(self, self.teles, False)
        if self.teletime == 0:
            for _ in hit_teles2:
                for tell in self.teles:
                    self.rect.x = tell.rect.x
                    self.rect.y = tell.rect.y
                    self.teletime = 10
                    break
            for _ in hit_teles:
                for tell2 in self.teles2:
                    self.rect.x = tell2.rect.x
                    self.rect.y = tell2.rect.y
                    self.teletime = 10
                    break
        hit_items = pygame.sprite.spritecollide(self, self.items, False)
        for item in hit_items:
            print "D"
            for _ in range(random.randint(8, 24)):
                fragment.fragmentgroup.add(Fragment((self.rect.x, self.rect.y), random.choice(self.fimgs)))
            #item.kill()



    # death by explosion
    def getfimage(self, images, imgs):
        self.fimgs = images
        self.f2imgs = imgs

    def getSounds(self, sounds):
        self.sounds = sounds

    def die(self):

            self.alive = False
        #self.rect.x = self.spawnx
        #self.rect.y = self.spawny
    def slowdie(self):
        self.dietime += 1
        if self.dietime > 60:
            self.alive = False
            self.dietime = 0
            self.state = "NORMAL"

    def dying(self, a):
        self.rect.y -= self.yvel
        self.yvel -= .0066 * self.mass
        self.image = pygame.transform.rotate(self.imageH, math.floor(self.yvel * 10))

        if self.rect.top > other.TOTAL_LEVEL_WIDTH - 96:
            self.alive = False
            self.yvel = 0
            self.xvel = 0
            self.rect.x = self.spawnx
            self.rect.y = self.spawny
            self.state = "STARTING_B"
            self.image = self.imageH
            print "PLAYER HAS DIED"
        return


    def applyDrag(self, medium):
        a = 0.003
        n = self.xvel * -1.0
        if self.xvel > 0.0:
            drag = math.floor(n * a) / 5
        else:
            drag = math.ceil(n * a) / 5

        self.xvel += drag



    def newfnction(self):
        #if other.GAMESTATE > 1:
        self.data.getCollidables(self)


class Player2(Player):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.state = "NORMAL"  # STATE INCLUDE: NORMAL, DYING, WINNING, STARTING
        self.xvel = 0
        self.yvel = 0

        self.hitHeightVel = False
        self.onGround = False
        self.dir = "right"
        self.name = "2"

        self.width = 32
        self.height = 32
        self.color = (255, 255, 255)
        self.region = (0.0, 1.0)
        self.oldregion = (0.0, 1.0)

        self.image = image
        self.imageH = image
        # self.image.fill((255,0,0))
        self.sounds = None

        self.rect = self.image.get_rect()
        self.spawnx = 288
        self.spawny = 128
        self.rect.y = self.spawny
        self.rect.x = self.spawnx

        self.walls = None
        self.deaths = None
        self.teles = None
        self.teles2 = None
        self.upwalls = None
        self.finish = None
        self.items = pygame.sprite.Group()
        self.otherplayers = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()

        self.down = False

        self.jumps = 1

        self.stunting = False
        self.mass = 100  # at mass 190, goes down through walls
        self.xmom = 0
        self.ymom = 0
        self.current_chunk = (0, 1)
        self.prev_chunk = self.current_chunk

        self.maxyvel = 15  # * (self.mass / 100)
        self.maxxvel = 10
        self.fimgs = None
        self.f2imgs = None

        self.alive = True
        self.dietime = 0
        self.teletime = 0
        self.data = None

        return





class Empty(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        return
