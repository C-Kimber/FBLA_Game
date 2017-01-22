import os
import sys

from item import *
from wall import *


class Level:
    def __init__(self, file="level_0", dir="./assets/levels/"):
        self.dir = ""
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
        b = open(self.dir + "level_0")
        file = open(self.dir + f, 'w')
        for x in b:
            for y in x:
                file.write(y)
        b.close()
        file.close()
        print "FILE " + f + " HAS BEEN CREATED"
        sys.exit(0)

    def clear(self):
        b = open(self.dir + "level_0")
        file = open(self.file, 'w')
        for x in b:
            for y in x:
                file.write(y)

        b.close()
        file.close()



    def write(self, pos=(0, 0), char="0", is_back=False):
        print char
        if is_back:
            txt = open(self.bfile, 'r+')
        else:
            txt = open(self.file, 'r+')
        n = 0
        m = 0
        str =""
        tile = ""
        for x in txt:
            for y in x:

                    # print m, n
                    if y != ",":
                        tile += y
                    else:

                        if x != ",":
                            if m == pos[0] and n == pos[1]:
                                if x != "\n":
                                    str += char + ","
                                else:
                                    str += char
                            else:
                                if x != "\n":
                                    str += tile + ","
                                else:
                                    str += tile

                        tile = ""
                        m += 1

            n += 1
            m = 0
            # print str
        #print str
        txt.seek(0)
        txt.truncate()
        txt.write(str)
        #txt.close()



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
        tile = ""
        #color = (255,255,255)
        if is_back:
            ftint = 50
            btint = 0
        else:
            btint = 50
            ftint = 0


        color = (255, 255, 255)
        for x in b_txt:
            # print x
            n += 1
            h += 1
            for y in x:
                # print m, n
                if m > -2 - camx / 32:

                    if m < 30 - camx / 32:
                        if y != ",":
                            tile += y

                        else:
                            if tile == "n":
                                tile = ""
                                m = -1

                                break

                            m += 1
                            w += 1

                            l = 0
                            r = pygame.Rect(m * multi + btint / 10 + camx, n * multi + btint / 10 + camy,
                                            multi - 5 - btint / 5,
                                            multi - 5 - btint / 5)

                            if tile == "3":  # deathwalls
                                color = (255 - btint, 255 - btint, 0)

                            elif tile == "1":  # one unit walls
                                color = (55 - btint, 55 - btint, 0)


                                # surface.blit(imgs["wall_2"], pygame.Rect(m * multi+camx, n * multi+camy, multi, multi))
                            elif tile == "_":  # long walls
                                color = (155 - btint, 155 - btint, 155 - btint)
                            elif tile == "[":  # medium walls
                                color = (155 - btint, 155 - btint, 155 - btint)
                            elif tile == "=":  # small walls
                                color = (155 - btint, 155 - btint, 155 - btint)
                            elif tile == "|":  # Tall wall
                                color = (155 - btint, 155 - btint, 155 - btint)
                            elif tile == "/":  # Tall wall mid
                                color = (155 - btint, 155 - btint, 155 - btint)
                            elif tile == ";":  # Tall wall small
                                color = (155 - btint, 155 - btint, 155 - btint)

                            elif tile == "2":
                                color = (155 - btint, 155 - btint, 155 - btint)
                                pygame.draw.rect(surface, color, r)

                            elif tile == "5":  # player 1 spawn
                                color = (255 - btint, 0, 0)
                            elif tile == "6":  # player 2 spawn
                                color = (0, 255 - btint, 0)

                            elif tile == "4a":  # Tele wall
                                r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                                pygame.draw.rect(surface, (255 - btint, 0, 255 - btint), r)
                                r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                                pygame.draw.rect(surface, (155 - btint, 0, 155 - btint), r)
                                continue
                            elif tile == "4b":
                                r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                                pygame.draw.rect(surface, (155 - btint, 0, 155 - btint), r)
                                r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                                pygame.draw.rect(surface, (255 - btint, 0, 255 - btint), r)
                                continue
                            elif tile == '7':
                                color = (0, 255 - btint, 155 - btint)
                            elif tile == "8":
                                color = (255 - btint, 185 - btint, 55 - btint)

                            elif tile == "9":
                                color = (155 - btint, 155 - btint, 55 - btint)



                            else:
                                color = (0, 0, 0)
                                l = 1

                            pygame.draw.rect(surface, color, r, l)

                            tile = ""



                            # pygame.draw.rect(surface, (0, 0, 0), (pygame.Rect(430-camx/9, 520-camy/9, 50, 40)), 2)
                    else:
                        m = -1
                        break
                else:
                    m += 1

        w = -1
        h = -1
        n = -1
        m = -1
        color = (255,255,255)
        for x in txt:
            n += 1
            h += 1
            for y in x:
                if m > -2-camx / 32:

                    if m < 30-camx/32:
                        if y != ",":
                            tile += y

                        else:
                            if tile == "n":
                                tile = ""
                                m = -1

                                break

                            m += 1
                            w += 1

                            l = 0
                            r = pygame.Rect(m * multi + ftint / 10 + camx, n * multi + ftint / 10 + camy, multi - 5 - ftint / 5,
                                            multi - 5 - ftint / 5)

                            if tile == "3":  # deathwalls
                                color = (255 - ftint, 255 - ftint, 0)

                            elif tile == "1":  # one unit walls
                                color = (55-ftint,55-ftint,0)


                                # surface.blit(imgs["wall_2"], pygame.Rect(m * multi+camx, n * multi+camy, multi, multi))
                            elif tile == "_":  # long walls
                                color = (155 - ftint, 155 - ftint, 155 - ftint)
                            elif tile == "[":  # medium walls
                                color = (155 - ftint, 155 - ftint, 155 - ftint)
                            elif tile == "=":  # small walls
                                color = (155 - ftint, 155 - ftint, 155 - ftint)
                            elif tile == "|":  # Tall wall
                                color = (155 - ftint, 155 - ftint, 155 - ftint)
                            elif tile == "/":  # Tall wall mid
                                color = (155 - ftint, 155 - ftint, 155 - ftint)
                            elif tile == ";":  # Tall wall small
                                color = (155 - ftint, 155 - ftint, 155 - ftint)

                            elif tile == "2":
                                color = (155 - ftint, 155 - ftint, 155 - ftint)
                                pygame.draw.rect(surface, color, r)

                            elif tile == "5":  # player 1 spawn
                                color = (255 - ftint, 0, 0)
                            elif tile == "6":  # player 2 spawn
                                color = (0, 255 - ftint, 0)

                            elif tile == "4a":  # Tele wall
                                r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                                pygame.draw.rect(surface, (255 - ftint, 0, 255 - ftint), r)
                                r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                                pygame.draw.rect(surface, (155 - ftint, 0, 155 - ftint), r)
                                continue
                            elif tile == "4b":
                                r = pygame.Rect(m * multi + camx, n * multi + camy, multi, multi)
                                pygame.draw.rect(surface, (155 - ftint, 0, 155 - ftint), r)
                                r = pygame.Rect((m * multi) + 8 + camx, (n * multi) + 8 + camy, 16, 16)
                                pygame.draw.rect(surface, (255 - ftint, 0, 255 - ftint), r)
                                continue
                            elif tile == '7':
                                color = (0, 255 - ftint, 155 - ftint)
                            elif tile == "8":
                                color = (255 - ftint, 185 - ftint, 55 - ftint)

                            elif tile == "9":
                                color = (155 - ftint, 155 - ftint, 55 - ftint)



                            else:
                                color = (0,0,0)
                                l = 1

                            pygame.draw.rect(surface, color, r, l)

                            tile = ""



                            #pygame.draw.rect(surface, (0, 0, 0), (pygame.Rect(430-camx/9, 520-camy/9, 50, 40)), 2)
                    else:
                        m = -1
                        break
                else:
                    m+= 1

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
        buf = other.WIDTH / 8 + 32
        txt = txt
        text = []
        col = []
        if other.GAMESTATE > 1:
            e1,e2 = 0,40
            f1,f2 = 0,240
        else:
            e1, e2 = 0, 24
            f1, f2 = 0, 30
        tile = ""
        for x in txt:  # Rows
            for y in x:  # Collums
                if y == "\n":
                    continue
                if y != ",":
                    tile += y
                else:
                    col.append(tile)
                    tile = ""
            text.append(col)
            col = []
        m = 0
        n = 0
        for y in text:
            for x in y:

                if m - 1 >= e1 and m + 1 <= e2:

                    if n - 1 >= f1 and n + 1 < f2:
                        cur = y[n]  # current AKA Middle
                        left = y[n - 1]
                        right = y[n + 1]
                        top = text[m - 1][n]
                        bot = text[m + 1][n]
                        if cur == "1":
                            f = other.getTileState(left, right, top, bot, "1")
                            data.wall_list.add(Wall(n * 32+buf, m * 32, data.sprite_library["wall_" + str(f + 1)],
                                                    f, (math.floor(n * 32 / 864), math.floor(m * 32 / 864))))

                        if cur == "5":  # player 1 spawn

                            data.player.spawnx = n * 32+buf
                            data.player.spawny = m * 32
                            data.player.rect.x = n * 32+buf
                            data.player.rect.y = m * 32
                            print data.player.spawnx, data.player.spawny


                        if x == "3":
                            f = other.getTileState(left, right, top, bot, "3")
                            data.wall_list.add(deathWall(n * 32+buf, m * 32, data.sprite_library["lava_"+str(f+1)]))


                        elif x == "6":  # player 2 spawn
                                data.player2.spawnx = n * 32 + buf
                                data.player2.spawny = m * 32
                                data.player2.rect.x = n * 32 + buf
                                data.player2.rect.y = m * 32

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
                        elif y[n] == "2":
                            f = other.getTileState(left, right, top, bot, "2")
                            data.wall_list.add(upWall(n * 32+buf, m * 32, data.sprite_library["up_wall_"+str(f+1)],f))
                        elif x == "^":
                            f = other.getTileState(left, right, top, bot, "^")
                            data.wall_list.add(upWall(n * 32, m * 32, data.sprite_library["up_wall_" + str(f + 1)], f))
                        elif x == "T":  # Tele walls
                            data.telewalls.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                            data.all_sprites.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                        elif x == "t":  # Tele Walls group 2
                            data.telewalls2.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                            data.all_sprites.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                        elif x == 'E':
                            data.finish.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                            data.all_sprites.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                        elif x == "8":
                            data.items.add(Base(data, (n * 32, m * 32), data.sprite_library["gem1"]))
                        elif x == "h":
                            data.hitwalls.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))
                            data.all_sprites.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))

                else:

                    if y[n] == '1':
                        data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_8"], 7))
                    if x == "5":  # player 1 spawn
                        data.player.spawnx = n * 32
                        data.player.spawny = m * 32
                        data.player.rect.x = n * 32
                        data.player.rect.y = m * 32
                    if x == "3":
                        data.deathwalls.add(deathWall(n * 32, m * 32, data.sprite_library["lava_5"]))
                        #data.all_sprites.add(deathWall(n * 32, m * 32, data.sprite_library["lava"]))
                        # elif x == "-":

                        # data.wall_list.add(Wall(n * 32, m * 32, data.sprite_library["wall_2"]))
                    elif x == "6":  # player 2 spawn
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
                        data.wall_list.add(upWall(n * 32, m * 32, data.sprite_library["up_wall_" + str(4)], 4))
                    elif x == "T":  # Tele walls
                        data.telewalls.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                        data.all_sprites.add(teleWall(n * 32, m * 32, data.sprite_library["t_wall_1"]))
                    elif x == "t":  # Tele Walls group 2
                        data.telewalls2.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                        data.all_sprites.add(teleWall2(n * 32, m * 32, data.sprite_library["t_wall_2"]))
                    elif x == 'E':
                        data.finish.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                        data.all_sprites.add(Finish(n * 32, m * 32, data.sprite_library["finish"]))
                    elif x == "8":
                        data.items.add(Base(data, (n * 32, m * 32), data.sprite_library["item"]))
                    elif x == "h":
                        data.hitwalls.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))
                        data.all_sprites.add(invWall((n * 32, m * 32), data.sprite_library["hitwall"]))
                n += 1

            m += 1
            other.TOTAL_LEVEL_WIDTH = n * 32 - 128
            other.TOTAL_LEVEL_HEIGHT = m * 32


            n = 0

        print "LVL DIMENSIONS: ", other.TOTAL_LEVEL_WIDTH, other.TOTAL_LEVEL_HEIGHT

    @staticmethod
    def connectBackTextures(data, txt):
        buf = other.WIDTH / 8 + 32
        txt = txt
        text = []
        col = []
        tile = ""
        if other.GAMESTATE > 1:
            e1,e2 = 0, 40
            f1,f2 = 0, 240
        else:
            e1,e2 = 0,26
            f1,f2 = 0,30


        for x in txt:  # Rows
            for y in x:  # Collums
                if y != ",":
                    tile += y
                else:
                    col.append(tile)
                    tile = ""
            text.append(col)
            col = []
        m = 0
        n = 0
        for y in text:
            for _ in y:

                if m - 1 >= e1 and m + 1 <= e2:

                    if n - 1 >= f1 and n + 1 < f2:  #
                        cur = y[n]  # current AKA Middle
                        left = y[n - 1]
                        right = y[n + 1]
                        top = text[m - 1][n]
                        bot = text[m + 1][n]

                        if cur == "1":

                            f = other.getTileState(left,right,top,bot,"1")
                            data.back_sprites.add( Wall(n * 32+buf, m * 32-32, data.sprite_library["back_wall_" + str(f + 1)],
                                                   f, (math.floor(n * 32 / 864), math.floor(m * 32 / 864))))
                            #walllist.append ( Wall(n * 32, m * 32, data.sprite_library["back_wall_" + str(f + 1)],
                             #                          f, (math.floor(n * 32 / 864), math.floor(m * 32 / 864))))
                        #else:
                            #walllist.append(None)
                        elif cur == "2":
                            f = other.getTileState(left, right, top, bot, "2")
                            data.wall_list.add(upWall(n * 32+buf, m * 32-32, data.sprite_library["up_wall_" + str(f + 1)], f))


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
                #print n, m

                if data.back_sprites[m][n] is not None:
                    #print data.back_sprites[m][n].rect
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
