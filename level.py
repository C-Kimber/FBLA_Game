import pygame
import os

import sys
from wall import *

import other


class Level():

    def __init__(self,  file="level_00",dir="./assets/levels/"):
        self.dir = dir
        self.file = file

        if os.path.isfile(self.dir+file):
            self.file = self.dir+file

        else:
            self.file = open(self.dir+file, 'w')
            self.file.write("X---X")
            self.file.close()

        self.levelSize = 32




    def new(self, f):
        b = open(self.dir+"level_00")
        file = open(self.dir+f, 'w')
        for x in b:
            for y in x:
                file.write(y)
        b.close()
        file.close()
        print "FILE " + f +" HAS BEEN CREATED"
        sys.exit(0)
    def clear(self):
        b = open(self.dir + "level_00")
        file = open(self.file, 'w')
        for x in b:
            for y in x:
                file.write(y)

        b.close()
        file.close()



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
        multi = 32
        if other.GAMESTATE == 2:
            multi = 8

        print multi
        n = -1
        m = -1
        for x in txt:
            n += 1
            for y in x:
                m += 1
                if y == "X" or y == "x":#deathwalls
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (255, 255, 0), r)

                elif y == "-":# one unit walls
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "_":#long walls
                    r = pygame.Rect(m * multi, n * multi, 16*multi, multi)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "[":  # medium walls
                    r = pygame.Rect(m * multi, n * multi, 8*multi, multi)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "=":  # small walls
                    r = pygame.Rect(m * multi, n * multi, 4*multi, multi)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "|": #Tall wall
                    r = pygame.Rect(m*multi,n*multi,multi,512)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "/":  # Tall wall mid
                    r = pygame.Rect(m * multi, n * multi, multi, 256)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == ";":  # Tall wall small
                    r = pygame.Rect(m * multi, n * multi, multi, 128)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "+":
                    r = pygame.Rect(m * multi, n * multi, multi, 16)
                    pygame.draw.rect(surface, (155, 155, 155), r)

                elif y == "1":#player 1 spawn
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (255, 0, 0), r)
                elif y == "2":  # player 2 spawn
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (0, 255, 0), r)
                elif y == "3":  # player 3 spawn
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (0, 0, 255), r)
                elif y == "4":  # player 4 spawn
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (255, 0, 255), r)
                elif y == "T":#Tele wall
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (255, 0, 255), r)
                    r = pygame.Rect((m * multi)+8, (n * multi)+8, 16, 16)
                    pygame.draw.rect(surface, (155, 0, 155), r)
                elif y == "t":
                    r = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (155, 0, 155), r)
                    r = pygame.Rect((m * multi) + 8, (n * multi) + 8, 16, 16)
                    pygame.draw.rect(surface, (255, 0, 255), r)
                else:#empty
                    l = pygame.Rect(m * multi, n * multi, multi, multi)
                    pygame.draw.rect(surface, (0, 0, 0), l, 1)
            m=-1


    def gameLev(self,thing):
        txt = open(self.file)
        n = -1
        m = -1
        for x in txt:
            n += 1
            for y in x:
                m += 1
                if y == "X" or y == "x":
                    thing.deathwalls.add(deathWall(m*32, n*32))
                    thing.all_sprites.add(deathWall(m*32, n*32))
                elif y == "-":
                    thing.wall_list.add(Wall(m * 32, n * 32))
                    thing.all_sprites.add(Wall(m * 32, n * 32))
                elif y == "1":  # player 1 spawn
                    thing.player.rect.x = m* 32
                    thing.player.rect.y = n*32
                elif y == "2":  # player 2 spawn
                    thing.player2.rect.x = m * 32
                    thing.player2.rect.y = n * 32

                elif y == "_":  # long walls
                    thing.wall_list.add(longWall(m*32, n*32, 512))
                    thing.all_sprites.add(longWall(m*32, n*32, 512))
                elif y == "[":  # medium walls
                    thing.wall_list.add(longWall(m * 32, n * 32, 256))
                    thing.all_sprites.add(longWall(m * 32, n * 32, 256))

                elif y == "=":  # small walls
                    thing.wall_list.add(longWall(m * 32, n * 32, 128))
                    thing.all_sprites.add(longWall(m * 32, n * 32, 128))
                elif y == "|":  # Tall wall
                    thing.wall_list.add(Pillar(m * 32, n * 32, 512))
                    thing.all_sprites.add(Pillar(m * 32, n * 32, 512))
                elif y == "/":  # Tall wall mid
                    thing.wall_list.add(Pillar(m * 32, n * 32, 256))
                    thing.all_sprites.add(Pillar(m * 32, n * 32, 256))
                elif y == ";":  # Tall wall small
                    thing.wall_list.add(Pillar(m * 32, n * 32, 128))
                    thing.all_sprites.add(Pillar(m * 32, n * 32, 128))
                elif y == "+":
                    thing.upwalls.add(upWall(m*32, n*32))
                    thing.all_sprites.add(upWall(m * 32, n * 32))

                elif y == "T":  # Tele walls
                    thing.telewalls.add(teleWall(m * 32, n * 32))
                elif y == "t": #Tele Walls group 2
                    thing. telewalls2.add(teleWall2(m*32, n*32))

                """elif y == "3":  # player 3 spawn
                    thing.player.x = m * 32
                    thing.player.y = n * 32

                    elif y == "4":  # player 4 spawn
                    thing.player.x = m * 32
                    thing.player.y = n * 32"""


            self.levelSize= n,m
            other.TOTAL_LEVEL_WIDTH = n * 32
            other.TOTAL_LEVEL_HEIGHT = m * 32
            m = -1
