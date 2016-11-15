import pygame
import random


fragmentgroup = pygame.sprite.Group()
#sprites that fly every which-way
class Fragment(pygame.sprite.Sprite):
    gravity = True
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [0.0,0.0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.image = pygame.Surface((50,50))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image,(random.randint(100,155),0,random.randint(0,55)),
                           (25,25),
                           random.randint(10,75))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center =self.pos
        self.lifetime = 60 +random.random()*5
        self.time = 0.0
        self.fragmentmaxspeed= 20
        self.dx = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)
        self.dy =random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)

    def update(self, seconds):
        self.time += seconds
        if self.time > self.lifetime:
            self.kill()
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds
        if Fragment.gravity:
            self.dy -= .66
        self.rect.centerx = round(self.pos[0],0)
        self.rect.centery = round(self.pos[1],1)

#more custom fragments
class custFrag(Fragment):
    gravity = True

    def __init__(self, pos, size,color):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [0.0, 0.0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]

        self.image = pygame.Surface((50, 50))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, color,
                           (25, 25),
                           random.randint(size[0], size[1]))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.lifetime = 60 + random.random() * 5
        self.time = 0.0
        self.fragmentmaxspeed = 20
        self.dx = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)
        self.dy = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)

    def update(self, seconds):
        self.time += seconds
        if self.time > self.lifetime:
            self.kill()
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds
        if Fragment.gravity:
            self.dy += .66
        self.rect.centerx = round(self.pos[0], 0)
        self.rect.centery = round(self.pos[1], 1)