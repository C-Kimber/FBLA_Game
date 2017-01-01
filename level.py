import os
import sys

from enemy import *
from wall import *


class Level:
    def __init__(self, file="level_00", dir="./assets/levels/"):
        self.dir = dir
        self.file = self.filename = file
        self.bfile = self.bfilename = file + "B"


        if os.path.isfile(self.dir + file):
            if os.path.isfile(self.dir + self.bfile):
                self.bfile = self.dir + self.bfile
            else:
                clear = open(self.dir + "level_!")
                txt = clear.read()
                self.bfile = open(self.dir + file + "B", 'w')
                self.bfile.write(txt)
                self.bfile.close()
                clear.close()
            self.file = self.dir + file

        else:
            clear = open(self.dir + "level_!")
            txt = clear.read()
            self.file = open(self.dir + file, 'w')
            self.bfile = open(self.dir + file + "B", 'w')
            self.file.write(txt)
            self.bfile.write(txt)
            self.file.close()
            self.bfile.close()
            clear.close()

        self.levelSize = 32
        self.levelMeasured = False

    def new(self, f):
        b = open(self.dir + "level_00")
        file = open(self.dir + f, 'w')
        for x in b:
            for y in x:
                file.write(y)
        b.close()
        file.close()
        print "FILE " + f + " HAS BEEN CREATED"
        sys.exit(0)

    def clear(self):
        b = open(self.dir + "level_00")
        file = open(self.file, 'w')
        for x in b:
            for y in x:
                file.write(y)

        b.close()
        file.close()

    def write(self, pos=(0, 0), char=".", is_back=False):
        if is_back:
            txt = open(self.bfile, 'r+')
        else:
            txt = open(self.file, 'r+')
        str = ""
        n = -1
        m = -1
        for x in txt:
            n += 1
            for y in x:
                m += 1
                if n == pos[0] and m == pos[1]:
                    str += char
                else:
                    str += y
            m = -1

        txt.seek(0)
        txt.truncate()
        txt.write(str)

        txt.close()
        return

    def display(self, surface, data, is_back=False):
        txt = open(self.file)
        b_txt = open(self.bfile)
        camx, camy = data

        multi = 32
        # if other.GAMESTATE == 2:
        #    multi = 8
        w = -1
        h = -1
        n = -1
        m = -1
        if is_back:
            ftint = 50
            btint = 0
        else:
            btint = 50
            ftint = 0

        for x in b_txt:  # BACKGROUND
            n += 1
            h += 1
            for y in x:
                m += 1
                w += 1
                r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                line = 0

                if y == "X" or y == "x":  # deathwalls
                    color = (255 - btint, 255 - btint, 0)

                elif y == "-":  # one unit walls
                    color = (55 - btint, 55 - btint, 0)
                    # surface.blit(imgs["wall_2"], pygame.Rect(m * multi+camx, n * multi+camy, multi, multi))
                elif y == "_":  # long walls
                    color = (155 - btint, 155 - btint, 155 - btint)
                elif y == "[":  # medium walls
                    color = (155 - btint, 155 - btint, 155 - btint)
                elif y == "=":  # small walls
                    color = (155 - btint, 155 - btint, 155 - btint)
                elif y == "|":  # Tall wall
                    color = (155 - btint, 155 - btint, 155 - btint)
                elif y == "/":  # Tall wall mid
                    color = (155 - btint, 155 - btint, 155 - btint)
                elif y == ";":  # Tall wall small
                    color = (155 - btint, 155 - btint, 155 - btint)
                elif y == "+":
                    color = (155 - btint, 155 - btint, 155 - btint)

                elif y == "1":  # player 1 spawn
                    color = (255 - btint, 0, 0)
                elif y == "2":  # player 2 spawn
                    color = (0, 255 - btint, 0)
                elif y == "3":  # player 3 spawn
                    color = (0, 0, 255 - btint)
                elif y == "4":  # player 4 spawn
                    color = (255 - btint, 0, 255 - btint)
                elif y == "T":  # Tele wall
                    r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                    pygame.draw.rect(surface, (255 - btint, 0, 255 - btint), r)
                    r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                    pygame.draw.rect(surface, (155 - btint, 0, 155 - btint), r)
                    continue
                elif y == "t":
                    r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                    pygame.draw.rect(surface, (155 - btint, 0, 155 - btint), r)
                    r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                    pygame.draw.rect(surface, (255 - btint, 0, 255 - btint), r)
                    continue
                elif y == 'E':
                    color = (0, 255 - btint, 155 - btint)
                elif y == "b":
                    color = (255 - btint, 185 - btint, 55 - btint)

                elif y == "h":
                    color = (155 - btint, 155 - btint, 55 - btint)

                else:  # empty
                    color = (200, 200, 200)
                    line = 1

                pygame.draw.rect(surface, color, r, line)
            m = -1
        w = -1
        h = -1
        n = -1
        m = -1

        for x in txt:
            n += 1
            h += 1
            for y in x:
                m += 1
                w += 1
                if y == ".":
                    continue

                r = pygame.Rect(m * multi + ftint / 10 + camx, n * multi + ftint / 10 + camy, multi - ftint / 5,
                                multi - ftint / 5)

                if y == "X" or y == "x":  # deathwalls
                    color = (255 - ftint, 255 - ftint, 0)

                elif y == "-":  # one unit walls
                    color = (55 - ftint, 55 - ftint, 0)
                    # surface.blit(imgs["wall_2"], pygame.Rect(m * multi+camx, n * multi+camy, multi, multi))
                elif y == "_":  # long walls
                    color = (155 - ftint, 155 - ftint, 155 - ftint)
                elif y == "[":  # medium walls
                    color = (155 - ftint, 155 - ftint, 155 - ftint)
                elif y == "=":  # small walls
                    color = (155 - ftint, 155 - ftint, 155 - ftint)
                elif y == "|":  # Tall wall
                    color = (155 - ftint, 155 - ftint, 155 - ftint)
                elif y == "/":  # Tall wall mid
                    color = (155 - ftint, 155 - ftint, 155 - ftint)
                elif y == ";":  # Tall wall small
                    color = (155 - ftint, 155 - ftint, 155 - ftint)
                elif y == "+":
                    color = (155 - ftint, 155 - ftint, 155 - ftint)

                elif y == "1":  # player 1 spawn
                    color = (255 - ftint, 0, 0)
                elif y == "2":  # player 2 spawn
                    color = (0, 255 - ftint, 0)
                elif y == "3":  # player 3 spawn
                    color = (0, 0, 255 - ftint)
                elif y == "4":  # player 4 spawn
                    color = (255 - ftint, 0, 255 - ftint)
                elif y == "T":  # Tele wall
                    r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                    pygame.draw.rect(surface, (255 - ftint, 0, 255 - ftint), r)
                    r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                    pygame.draw.rect(surface, (155 - ftint, 0, 155 - ftint), r)
                    continue
                elif y == "t":
                    r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                    pygame.draw.rect(surface, (155 - ftint, 0, 155 - ftint), r)
                    r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                    pygame.draw.rect(surface, (255 - ftint, 0, 255 - ftint), r)
                    continue
                elif y == 'E':
                    color = (0, 255 - ftint, 155 - ftint)
                elif y == "b":
                    color = (255 - ftint, 185 - ftint, 55 - ftint)

                elif y == "h":
                    color = (155 - ftint, 155 - ftint, 55 - ftint)

                if y != ".":
                    pygame.draw.rect(surface, color, r)

                """l = pygame.Rect(430 + m * 3, 520 + n * 3, 5, 5)
                if y != ".":

                    pygame.draw.rect(surface, (0, 0, 0), l)
                pygame.draw.rect(surface, (0, 0, 0), (pygame.Rect(430-camx/9, 520-camy/9, 50, 40)), 2)"""
            m = -1

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

        if not self.levelMeasured:
            other.TOTAL_LEVEL_WIDTH = w
            other.TOTAL_LEVEL_HEIGHT = h
            self.levelMeasured = True

    def gameLev(self, thing):
        txt = open(self.file)
        btxt = open(self.bfile)
        self.connectBackTextures(thing, btxt)
        self.connectTextures(thing, txt)
        txt.close()
        btxt.close()
        print "LEVEL LOADED"

    @staticmethod
    def connectTextures(data, txt):
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

                if m - 1 >= 0 and m + 1 <= 38:
                    if n - 1 >= 0 and n + 1 < 245:  #
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
                                        f = 7
                                    else:
                                        f = 13
                                elif top == "-":
                                    if bot == "-":
                                        f = 5
                                    else:
                                        f = 8
                                elif bot == "-":
                                    f = 2
                                else:
                                    f = 14
                                    # elif:
                            elif right == "-":  # NO LEFT
                                if top == '-':
                                    if bot == "-":
                                        f = 3
                                    else:
                                        f = 6
                                elif bot == "-":
                                    f = 0
                                else:
                                    f = 12
                            elif top == "-":  # NO LEFT OR RIGHT
                                if bot == "-":
                                    f = 10
                                else:
                                    f = 11
                            elif bot == "-":  # NO LEFT, RIGHT, OR UP
                                f = 9

                            else:
                                f = 15
                            data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_" + str(f + 1)],
                                                    f, (math.floor(n * 32 / 864), math.floor(m * 32 / 864))))

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
                            data.enemies.add(Base(data,(n * 32, m * 32), data.sprite_library["enemy"]))
                            data.all_sprites.add(Base(data,(n * 32, m * 32), data.sprite_library["enemy"]))
                        elif x == "h":
                            data.hitwalls.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))
                            data.all_sprites.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))

                else:

                    if x == '-':
                        data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_8"], 7))
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
            print "LVL DIMENSIONS: ", other.TOTAL_LEVEL_WIDTH, other.TOTAL_LEVEL_HEIGHT

            n = 0

    @staticmethod
    def connectBackTextures(data, txt):
        txt = txt
        text = []
        col = []
        walllist = []
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
            for _ in y:
                if m - 1 >= 0 and m + 1 <= 37:

                    if n - 1 >= 0 and n + 1 < 245:  #
                        cur = y[n]  # current AKA Middle
                        left = y[n - 1]
                        right = y[n + 1]
                        top = text[m - 1][n]
                        bot = text[m + 1][n]

                        if cur == "-":

                            if left == "-":
                                if right == "-":
                                    if bot == "-":
                                        if top == "-":
                                            f = 4

                                        else:
                                            f = 1
                                    elif top == "-":
                                        f = 7
                                    else:
                                        f = 13
                                elif top == "-":
                                    if bot == "-":
                                        f = 5
                                    else:
                                        f = 8
                                elif bot == "-":
                                    f = 2
                                else:
                                    f = 14
                                    # elif:
                            elif right == "-":  # NO LEFT
                                if top == '-':
                                    if bot == "-":
                                        f = 3
                                    else:
                                        f = 6
                                elif bot == "-":
                                    f = 0
                                else:
                                    f = 12
                            elif top == "-":  # NO LEFT OR RIGHT
                                if bot == "-":
                                    f = 10
                                else:
                                    f = 11
                            elif bot == "-":  # NO LEFT, RIGHT, OR UP
                                f = 9

                            else:
                                f = 15
                            data.back_sprites.add( Wall(n * 32, m * 32, data.sprite_library["back_wall_" + str(f + 1)],
                                                   f, (math.floor(n * 32 / 864), math.floor(m * 32 / 864))))
                            #walllist.append ( Wall(n * 32, m * 32, data.sprite_library["back_wall_" + str(f + 1)],
                             #                          f, (math.floor(n * 32 / 864), math.floor(m * 32 / 864))))
                        #else:
                            #walllist.append(None)


                n += 1
            #data.back_sprites.append(walllist) #in 2D array
            #walllist = []
            m += 1
            n = 0

    def foo(self, data):
        """EDIT TO SEE IF FILE IS ALRADY OPEN"""
        txt = open(self.file)
        btxt = open(self.bfile)
        playerIndex = [math.floor(data.player.rect.x), math.floor(data.player.rect.y)]
        for y in range(-20,22):
            for x in range(-12,12):

                i = math.floor(playerIndex[0]/32)
                j = math.floor(playerIndex[1]/32)
                n = i + y
                m = j + x
                n = int(other.constrain(n, 1, 12))
                m = int(other.constrain(m, 1, 12))
                print n, m

                if data.back_sprites[m][n] is not None:
                    print data.back_sprites[m][n].rect
                    data.displayTiles.add(data.back_sprites[m][n])
                #data.displayTiles.add(Wall(playerIndex[0]-n, playerIndex[1]-m, data.sprite_library["back_wall_" + str(5 + 1)],
                #                   5, (math.fwwwloor(y * 32 / 864), math.floor(x * 32 / 864))))

        txt.close()
        btxt.close()


        #if not fileobj.closed:
        #    print("file is already opened")


    def is_open(self, file_name):
        if os.path.exists(file_name):
            try:
                os.rename(file_name, file_name)  # can't rename an open file so an error will be thrown
                return False
            except:
                return True
        raise NameError
