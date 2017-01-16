import random
import other
import pygame

fragmentgroup = pygame.sprite.Group()


# sprites that fly every which-way
class Fragment(pygame.sprite.Sprite):
    gravity = True

    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)

        self.pos = [0.0, 0.0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.image = image  # pygame.Surface((50,50))
        # self.image = pygame.transform.scale(self.image, (n,n)  )
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.lifetime = 60 + random.random() * 5
        self.time = 0.0
        self.fragmentmaxspeed = 5
        self.dx = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)
        self.dy = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)

    def update(self, seconds):
        self.time += seconds
        if self.rect.x < other.WIDTH / 8 + 64:
            self.kill()
        elif self.rect.x > other.TOTAL_LEVEL_WIDTH + 96 + other.WIDTH / 8:
            self.kill()
        if self.time > self.lifetime:
            self.kill()
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds
        if Fragment.gravity:
            self.dy += .66
        self.rect.centerx = round(self.pos[0], 0)
        self.rect.centery = round(self.pos[1], 1)


# more custom fragments
class custFrag(Fragment):
    gravity = True

    def __init__(self, pos, size, img):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [0.0, 0.0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        s = random.randint(3,9)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.lifetime = 60 + random.random() * 5
        self.time = 0.0
        self.fragmentmaxspeed = 10
        self.dx = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)
        self.dy = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)

    def update(self, seconds):
        self.time += seconds
        if self.rect.x < other.WIDTH/8+70:
            self.kill()
        elif self.rect.x > other.TOTAL_LEVEL_WIDTH +96+ other.WIDTH/8:
            self.kill()
        if self.time > self.lifetime:
            self.kill()
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds
        if Fragment.gravity:
            self.dy += .46
        self.rect.centerx = round(self.pos[0], 0)
        self.rect.centery = round(self.pos[1], 1)
