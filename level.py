import pygame
import os
import sys
from wall import *


class Level():

    def __init__(self, file="base_level"):
        self.dir = "./assets/levels/"

        if os.path.isfile(self.dir+file):
            self.file = self.dir+file

        else:
            self.file = open(self.dir+file, 'w')
            self.file.write("X---X")
            self.file.close()



    def new(self, f):
        b = open(self.dir+"base_level")
        file = open(self.dir+f, 'w')
        for x in b:
            for y in x:
                file.write(y)
        b.close()
        file.close()
        print "FILE " + f +" HAS BEEN CREATED"
        sys.exit(0)



    def write(self,pos=(0,0),char="."):

        txt = open(self.file, 'r+')
        str = ""
        n=-1
        m=-1
        for x in txt:
            n += 1
            for y in x:
                m += 1
                if n == pos[0] and m == pos[1]:
                    str += char
                else:
                    str +=y
            m = -1

        txt.seek(0)
        txt.truncate()
        txt.write(str)

        txt.close()
        return

    def display(self, surface):
        txt = open(self.file)
        n = -1
        m = -1
        for x in txt:
            n += 1
            for y in x:
                m += 1
                if y == "X" or y == "x":
                    r = pygame.Rect(m * 32, n * 32, 32, 32)
                    pygame.draw.rect(surface, (255, 0, 0), r)
                if y == "-":
                    r = pygame.Rect(m * 32, n * 32, 32, 32)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                else:
                    l = pygame.Rect(m * 32, n * 32, 32, 32)
                    pygame.draw.rect(surface, (0, 0, 0), l, 1)
            m=-1


    def gameLev(self,thing):
        txt = open(self.file)
        n = -1
        m = -1
        for x in txt:
            n += 1
            print x
            for y in x:
                print y
                m += 1
                if y == "X" or y == "x":
                    print "deathwalls!"
                    thing.deathwalls.add(deathWall(m*32, n*32))
                    thing.all_sprites.add(deathWall(m*32, n*32))
                elif y == "-":
                    print "walls"
                    thing.wall_list.add(Wall(m * 32, n * 32))
                    thing.all_sprites.add(Wall(m * 32, n * 32))



            m = -1
