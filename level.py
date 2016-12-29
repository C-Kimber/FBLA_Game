import pygame
import os

import sys
from wall import *
from enemy import *
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
        self.levelMeasured = False




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

    def display(self, surface, data, imgs):
        txt = open(self.file)
        camx, camy = data

        multi = 32
        #if other.GAMESTATE == 2:
        #    multi = 8
        w = -1
        h = -1
        n = -1
        m = -1
        for x in txt:
            n += 1
            h +=1
            for y in x:
                m += 1
                w += 1
                if y == "X" or y == "x":#deathwalls
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (255, 255, 0), r)

                elif y == "-":# one unit walls
                    surface.blit(imgs["wall_2"], pygame.Rect(m * multi+camx, n * multi+camy, multi, multi))
                elif y == "_":#long walls
                    r = pygame.Rect(m * multi+camx, n * multi+camy, 16*multi, multi)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "[":  # medium walls
                    r = pygame.Rect(m * multi+camx, n * multi+camy, 8*multi, multi)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "=":  # small walls
                    r = pygame.Rect(m * multi+camx, n * multi+camy, 4*multi, multi)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "|": #Tall wall
                    r = pygame.Rect(m*multi+camx,n*multi+camy,multi,512)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "/":  # Tall wall mid
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, 256)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == ";":  # Tall wall small
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, 128)
                    pygame.draw.rect(surface, (155, 155, 155), r)
                elif y == "+":
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, 16)
                    pygame.draw.rect(surface, (155, 155, 155), r)

                elif y == "1":#player 1 spawn
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (255, 0, 0), r)
                elif y == "2":  # player 2 spawn
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (0, 255, 0), r)
                elif y == "3":  # player 3 spawn
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (0, 0, 255), r)
                elif y == "4":  # player 4 spawn
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (255, 0, 255), r)
                elif y == "T":#Tele wall
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (255, 0, 255), r)
                    r = pygame.Rect((m * multi)+8+camx, (n * multi)+8+camy, 16, 16)
                    pygame.draw.rect(surface, (155, 0, 155), r)
                elif y == "t":
                    r = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (155, 0, 155), r)
                    r = pygame.Rect((m * multi) + 8+camx, (n * multi) + 8+camy, 16, 16)
                    pygame.draw.rect(surface, (255, 0, 255), r)
                elif y == 'E':
                    r = pygame.Rect((m * multi)  + camx, (n * multi)  + camy, 32, 32)
                    pygame.draw.rect(surface, (0, 255, 155), r)
                elif y == "b":
                    r = pygame.Rect((m * multi) + camx, (n * multi) + camy, 32, 32)
                    pygame.draw.rect(surface, (255, 185, 55), r)
                elif y == "h":
                    r = pygame.Rect((m * multi) + camx, (n * multi) + camy, 32, 32)
                    pygame.draw.rect(surface, (155, 155, 55), r)
                else:#empty
                    l = pygame.Rect(m * multi+camx, n * multi+camy, multi, multi)
                    pygame.draw.rect(surface, (200, 200, 200), l, 1)

                """l = pygame.Rect(430 + m * 3, 520 + n * 3, 5, 5)
                if y != ".":

                    pygame.draw.rect(surface, (0, 0, 0), l)
                pygame.draw.rect(surface, (0, 0, 0), (pygame.Rect(430-camx/9, 520-camy/9, 50, 40)), 2)"""
            m=-1

        """# BLOCK
        for i in range(0, 55):  # 5, 14, 41
            for j in range(0, 18):  # 3,5,14
                pygame.draw.rect(surface, (55, 155, 55), (pygame.Rect(camx + i * 96, camy + j * 96, 96, 96)),2)  # 96, 288, 864
        # CHUNK
        for i in range(0, 15):  # 5, 14, 41
            for j in range(0, 6):  # 3,5,14
                pygame.draw.rect(surface, (55, 55, 155), (pygame.Rect(camx + i * 288, camy + j * 288, 288, 288)),3)  # 96, 288, 864
        #REGION
        for i in range(0, 5):#5, 14, 41
            for j in range(0, 3): #3,5,14
                pygame.draw.rect(surface, (155, 55, 55), (pygame.Rect(camx + i * 864, camy+j *864, 864,864)), 5)#96, 288, 864"""



        if self.levelMeasured == False:
            other.TOTAL_LEVEL_WIDTH = w
            other.TOTAL_LEVEL_HEIGHT = h
            print other.TOTAL_LEVEL_WIDTH
            self.levelMeasured = True
            h = -1
            w = -1



    def gameLev(self,thing):
        txt = open(self.file)
        n = -1
        m = -1
        self.connectTextures(thing, txt)
        for x in txt:
            n += 1
            for y in x:
                m += 1

                


                """elif y == "3":  # player 3 spawn
                    thing.player.x = m * 32
                    thing.player.y = n * 32

                    elif y == "4":  # player 4 spawn
                    thing.player.x = m * 32
                    thing.player.y = n * 32"""


            self.levelSize= n,m
            #other.TOTAL_LEVEL_WIDTH = n * 32
            #other.TOTAL_LEVEL_HEIGHT = m * 32
            #print other.TOTAL_LEVEL_WIDTH
            m = -1



    def connectTextures(self,data, txt):
        txt = txt
        text = []
        col = []
        for x in txt:  # Rows
            for y in x:  # Collums
                if y == "\n":
                    continue
                col.append(y)
            text.append(col)
            col = []
            # print text
        m = 0
        n = 0
        for y in text:
            for x in y:


                if m - 1 >= 0 and m + 1 <= 53:
                    if n - 1 >= 0 and n + 1 < 135:  #
                        cur = y[n]  # current AKA Middle
                        left = y[n - 1]
                        right = y[n + 1]
                        top = text[m - 1][n]
                        bot = text[m + 1][n]
                        f = 7
                        if cur == "-":

                            if left == "-":
                                if right == "-":
                                    if bot == "-":
                                        if top == "-":
                                            f = 4

                                        else:
                                            f = 1
                                    elif top == "-":
                                        f= 7
                                    else:
                                        f=1
                                elif top == "-":
                                    if bot == "-":
                                        f=5
                                    else:
                                        f = 8
                                elif bot == "-":
                                    f = 2
                                else:
                                    f = 2
                                    # elif:
                            elif right == "-":  # NO LEFT
                                if top == '-':
                                    if bot == "-":
                                        f = 3
                                    else:
                                        f= 6
                                elif bot == "-":
                                    f= 0
                                else:
                                    f=0
                            elif top == "-":  # NO LEFT OR RIGHT
                                if bot == "-":
                                    f = 9
                                else:
                                    f= 7
                            elif bot == "-":  # NO LEFT, RIGHT, OR UP
                                f=10

                            else:
                                f=1
                            data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_"+str(f+1)],
                                                    f,(math.floor(n * 32/864),math.floor(m * 32/864)) ))


                        if x == "1":  # player 1 spawn
                            data.player.spawnx = n * 32
                            data.player.spawny = m * 32
                            data.player.rect.x = n * 32
                            data.player.rect.y = m * 32

                        if x == "X" or x == "x":
                            data.deathwalls.add(deathWall(n * 32, m * 32, data.sprite_library["lava"]))
                            data.all_sprites.add(deathWall(n * 32, m * 32, data.sprite_library["lava"]))
                            # elif x == "-":

                            # data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_2"]))
                        elif x == "2":  # player 2 spawn
                            data.player2.spawnx = n * 32
                            data.player2.spawny = m * 32
                            data.player2.rect.x = n * 32
                            data.player2.rect.x = m * 32

                        elif x == "_":  # long walls
                            data.allwalls.add(longWall(n * 32, m * 32, 512))
                            data.all_sprites.add(longWall(n * 32, m * 32, 512))
                        elif x == "[":  # medium walls
                            data.allwalls.add(longWall(n * 32, m * 32, 256))
                            data.all_sprites.add(longWall(n * 32, m * 32, 256))

                        elif x == "=":  # small walls
                            data.allwalls.add(longWall(n * 32, m * 32, 128))
                            data.all_sprites.add(longWall(n * 32, m * 32, 128))
                        elif x == "|":  # Tall wall
                            data.allwalls.add(Pillar(n * 32, m * 32, 512))
                            data.all_sprites.add(Pillar(n * 32, m * 32, 512))
                        elif x == "/":  # Tall wall mid
                            data.allwalls.add(Pillar(n * 32, m * 32, 256))
                            data.all_sprites.add(Pillar(n * 32, m * 32, 256))
                        elif x == ";":  # Tall wall small
                            data.allwalls.add(Pillar(n * 32, m * 32, 128))
                            data.all_sprites.add(Pillar(n * 32, m * 32, 128))
                        elif x == "+":
                            data.upwalls.add(upWall(n * 32, m * 32, data.sprite_library["up_wall"]))
                            data.all_sprites.add(upWall(n * 32, m * 32, data.sprite_library["up_wall"]))
                        elif x == "T":  # Tele walls
                            data.telewalls.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                            data.all_sprites.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                        elif x == "t":  # Tele Walls group 2
                            data.telewalls2.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                            data.all_sprites.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                        elif x == 'E':
                            data.finish.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                            data.all_sprites.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                        elif x == "b":
                            data.enemies.add(Base((n * 32, m * 32), data.sprite_library["enemy"]))
                            data.all_sprites.add(Base((n * 32, m * 32), data.sprite_library["enemy"]))
                        elif x == "h":
                            data.hitwalls.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))
                            data.all_sprites.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))

                else:

                    if x == '-':
                        data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_8"],7))
                    if x == "1":  # player 1 spawn
                        data.player.spawnx = n * 32
                        data.player.spawny = m * 32
                        data.player.rect.x = n * 32
                        data.player.rect.y = m * 32
                    if x == "X" or x == "x":
                        data.deathwalls.add(deathWall(n * 32, m * 32, data.sprite_library["lava"]))
                        data.all_sprites.add(deathWall(n * 32, m * 32, data.sprite_library["lava"]))
                        # elif x == "-":

                        # data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_2"]))
                    elif x == "2":  # player 2 spawn
                        data.player2.spawnx = n * 32
                        data.player2.spawny = m * 32
                        data.player2.rect.x = n * 32
                        data.player2.rect.x = m * 32

                    elif x == "_":  # long walls
                        data.allwalls.add(longWall(n * 32, m * 32, 512))
                        data.all_sprites.add(longWall(n * 32, m * 32, 512))
                    elif x == "[":  # medium walls
                        data.allwalls.add(longWall(n * 32, m * 32, 256))
                        data.all_sprites.add(longWall(n * 32, m * 32, 256))

                    elif x == "=":  # small walls
                        data.allwalls.add(longWall(n * 32, m * 32, 128))
                        data.all_sprites.add(longWall(n * 32, m * 32, 128))
                    elif x == "|":  # Tall wall
                        data.allwalls.add(Pillar(n * 32, m * 32, 512))
                        data.all_sprites.add(Pillar(n * 32, m * 32, 512))
                    elif x == "/":  # Tall wall mid
                        data.allwalls.add(Pillar(n * 32, m * 32, 256))
                        data.all_sprites.add(Pillar(n * 32, m * 32, 256))
                    elif x == ";":  # Tall wall small
                        data.allwalls.add(Pillar(n * 32, m * 32, 128))
                        data.all_sprites.add(Pillar(n * 32, m * 32, 128))
                    elif x == "+":
                        data.upwalls.add(upWall(n * 32, m * 32, data.sprite_library["up_wall"]))
                        data.all_sprites.add(upWall(n * 32, m * 32, data.sprite_library["up_wall"]))
                    elif x == "T":  # Tele walls
                        data.telewalls.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                        data.all_sprites.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                    elif x == "t":  # Tele Walls group 2
                        data.telewalls2.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                        data.all_sprites.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                    elif x == 'E':
                        data.finish.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                        data.all_sprites.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                    elif x == "b":
                        data.enemies.add(Base((n * 32, m * 32), data.sprite_library["enemy"]))
                        data.all_sprites.add(Base((n * 32, m * 32), data.sprite_library["enemy"]))
                    elif x == "h":
                        data.hitwalls.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))
                        data.all_sprites.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))
                n += 1
            m += 1
            other.TOTAL_LEVEL_WIDTH = n * 32 - 128
            other.TOTAL_LEVEL_HEIGHT = m * 32

            n = 0
        print "Complete"


