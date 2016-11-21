import pygame
from level import Level
import os


class DataD:
    #intitialisez sprites, and other data
    def __init__(self, width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        self.level = Level("level_01")
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

        if pygame.K_n in newkeys:
            self.level.new(raw_input(">"))
        if pygame.K_RIGHT in newkeys:
            self.l += 1
            self.changeLevel()

        if pygame.K_LEFT in newkeys:
            self.l -= 1
            self.changeLevel()

        return
    def changeLevel(self):
        print self.l
        if os.path.isfile("level_0"+str(self.l)):
            self.level = Level("level_0"+str(self.l))


    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((255, 255, 255), rect)  # back
        self.level.display(surface)
        return