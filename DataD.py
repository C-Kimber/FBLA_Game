import pygame
from level import Level
import os


class DataD:
    #intitialisez sprites, and other data
    def __init__(self, width, height, frame_rate):
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        self.level = Level("level_01")
        self.num_files = len([f for f in os.listdir("./assets/levels")
                              if os.path.isfile(os.path.join("./assets/levels", f))])
        self.l = 1
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mp = mouse_position
        block = self.mp[1] / 32, self.mp[0] / 32

        if 1 in buttons:
            self.level.write(block,"-")
        elif 2 in buttons:
            self.level.write(block,"X")
        elif 3 in buttons :
            self.level.write(block)
        elif pygame.K_1 in keys:
            self.level.write(block, '1')
        elif pygame.K_2 in keys:
            self.level.write(block, '2')
        elif pygame.K_3 in keys:
            self.level.write(block, '3')
        elif pygame.K_4 in keys:
            self.level.write(block, '4')
        elif pygame.K_j in keys:
            self.level.write(block, '=')
        elif pygame.K_k in keys:
            self.level.write(block, '[')
        elif pygame.K_l in keys:
            self.level.write(block, '_')

        if pygame.K_n in newkeys:
            self.level.new("level_0"+str(self.num_files))


        if pygame.K_RIGHT in newkeys:
            self.l += 1
            self.changeLevel()

        if pygame.K_LEFT in newkeys:
            self.l -= 1
            self.changeLevel()

        if self.l > self.num_files-1:
            self.l = self.num_files-1
        elif self.l < 0:
            self.l = 0

        return
    def changeLevel(self):
        print self.l
        if os.path.isfile("./assets/levels/level_0"+str(self.l)):
            print "It exists"
            self.level = Level("level_0"+str(self.l))


    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((255, 255, 255), rect)  # back
        self.level.display(surface)
        r = pygame.Rect(800,0,180, 640)
        pygame.draw.rect(surface, (255, 255, 255), r)
        pygame.draw.rect(surface, (25, 25, 25), r,5)
        pygame.draw.rect(surface, (155, 155, 155), pygame.Rect(832,32,32, 32))
        pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(832, 96, 32, 32))
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(832, 160, 32, 32))
        pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(832, 224, 32, 32))
        pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(832, 288, 32, 32))
        pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(832, 352, 32, 32))

        self.drawTextLeft(surface, "Level "+ str(self.l), (55,0,55), 832, 35, self.font)

        return

    def drawTextLeft(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return