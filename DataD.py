import pygame
from level import Level
import os
import sys
import other


class DataD:
    #intitialisez sprites, and other data
    def __init__(self, width, height, frame_rate):
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        self.level = Level("level_0",'./assets/long_levels/')
        #self.level = Level("level_01")
        self.num_files = len([f for f in os.listdir("./assets/levels")
                              if os.path.isfile(os.path.join("./assets/levels", f))])
        self.l = 1
        self.selected = "."
        self.multi  =32

        self.cameraX = 0
        self.cameraY = 0
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mp = mouse_position

        block = [(self.mp[1]-self.cameraY) / 32, (self.mp[0]-self.cameraX) / 32]
        self.b = block
        #if other.GAMESTATE == 2:
            #block = [self.mp[1] / 8+self.cameraX, self.mp[0] / 8+self.cameraY]
            #self.multi = 8
        #print block

        if self.level.dir == './assets/long_levels/':
            other.GAMESTATE = 2

        if other.GAMESTATE != 2:
            if block[0] > 19:
                block[0]= 19
            if block[1] > 24:
                block[1] = 24

        if pygame.K_a in keys:
            self.cameraX += 32
        if pygame.K_d in keys:
            self.cameraX -= 32
        if pygame.K_w in keys:
            self.cameraY += 32
        if pygame.K_s in keys:
            self.cameraY -= 32

        if self.cameraY > 0:
            self.cameraY = 0
        if self.cameraY < -608:
            self.cameraY = -608
        if self.cameraX > 0:
            self.cameraX = 0
        if self.cameraX < -1*other.TOTAL_LEVEL_WIDTH/1.5:
            self.cameraX = -1*other.TOTAL_LEVEL_WIDTH/1.5


        if 1 in buttons:
            self.button(mouse_position,(self.width-37, self.height-37, 32, 32),".")#clear selected
            #self.clearbutton(mouse_position, (self.width - 69, self.height - 37, 32, 32))  # clear
            self.button(mouse_position, (832,32,32, 32),'-') #wall
            self.button(mouse_position, (832, 96, 32, 32),"X")  # lava
            self.button(mouse_position,(832, 160, 32, 32),"1")  #p1
            self.button(mouse_position,(832, 224, 32, 32),"2")  #p2
            self.button(mouse_position,(832, 288, 32, 32),"3")  #p3
            self.button(mouse_position,(832, 352, 32, 32),"4")  #p4
            self.button(mouse_position,(832, 416, 32, 32),"T")   #telewall 1
            self.button(mouse_position,(832, 480, 32, 32), "t")   #telewall 2
            self.button(mouse_position,(832 + 49, 32, 16, 16),"=") #longwall small
            self.button(mouse_position,(832 + 81, 32, 16, 16),"[") #longwall medium
            self.button(mouse_position, (832 +113, 32, 16, 16),"_") #longwall large
            self.button(mouse_position, (832 + 49, 49, 16, 16), ";")  # longwall small
            self.button(mouse_position, (832 + 81, 49, 16, 16), "/")  # longwall medium
            self.button(mouse_position, (832 + 113, 49, 16, 16), "|")  # longwall large
            self.button(mouse_position, ((832 + 113, 67, 32, 16)),'+')
            self.button(mouse_position, ((880, 96, 32, 32)), 'E') #Finish block
            self.button(mouse_position, ((880, 160, 32, 32)), 'b')  # Finish block
            if mouse_position[0] > 0 and mouse_position[0] < 800:
                self.level.write(block,self.selected)

        elif 2 in buttons:
            self.level.clear()
        elif 3 in buttons :
            self.level.write(block)




        if pygame.K_n in newkeys:
            self.level.new("level_0"+str(self.num_files))
        elif pygame.K_DELETE in newkeys:
            os.remove("./assets/levels/level_0"+str(self.l))
            print 'FILE  level_0'+str(self.l) +" HAS BEEN DELETED"
            pygame.quit()
            sys.exit(0)


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
        if os.path.isfile("./assets/levels/level_0"+str(self.l)):
            self.level = Level("level_0"+str(self.l))
            print "LEVEL_0"+str(self.l)

    def button(self,mp,rect,char='.'):
        mx,my = mp
        x,y,w,h = rect
        if mx > x and mx < x+w:
            if my > y and my < y+h:
                self.selected = char
    def clearbutton(self,mp,rect):
        mx, my = mp
        x, y, w, h = rect
        if mx > x and mx < x + w:
            if my > y and my < y + h:
                print "clear"
                self.level.clear()

    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill((255, 255, 255), rect)  # back

        self.level.display(surface,(self.cameraX,self.cameraY))


        r = pygame.Rect(800,0,180, 640)
        pygame.draw.rect(surface, (255, 255, 255), r)
        pygame.draw.rect(surface, (25, 25, 25), r,5)
        pygame.draw.rect(surface, (155, 155, 155), pygame.Rect(832,32,32, 32))#wall
        pygame.draw.rect(surface, (125, 125, 125), pygame.Rect(832+49, 32, 16, 16))  # Lwall s
        pygame.draw.rect(surface, (125, 125, 125), pygame.Rect(832+81, 32, 16, 16))  # lwall m
        pygame.draw.rect(surface, (125, 125, 125), pygame.Rect(832+113, 32, 16, 16))  # lwall l
        pygame.draw.rect(surface, (125, 125, 125), pygame.Rect(832 + 49, 49, 16, 16))  # Twall s
        pygame.draw.rect(surface, (125, 125, 125), pygame.Rect(832 + 81, 49, 16, 16))  # Twall m
        pygame.draw.rect(surface, (125, 125, 125), pygame.Rect(832 + 113, 49, 16, 16))  # Twall l
        pygame.draw.rect(surface, (125, 125, 125), pygame.Rect(832 + 113, 67, 32, 16))


        pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(832, 96, 32, 32))#lava
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(832, 160, 32, 32))#p1
        pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(832, 224, 32, 32))#p2
        pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(832, 288, 32, 32))#p3
        pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(832, 352, 32, 32))#p4

        pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(832, 416, 32, 32))#Telewall 1
        pygame.draw.rect(surface, (155, 0, 155), pygame.Rect((832) + 8, (416) + 8, 16, 16))

        pygame.draw.rect(surface, (155, 0, 155), pygame.Rect(832, 480, 32, 32))# Telewall 2
        pygame.draw.rect(surface, (255, 0, 255), pygame.Rect((832) + 8, (480) + 8, 16, 16))

        pygame.draw.rect(surface, (255, 0,0), pygame.Rect(self.width-37, self.height-37, 32, 32),4)  # clear selected
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.width - 70, self.height - 37, 32, 32), 4)  # clear

        pygame.draw.rect(surface, (0, 255, 155), pygame.Rect(880, 96, 32, 32)) # finish
        pygame.draw.rect(surface, (255, 185, 55), pygame.Rect(880, 160, 32, 32)) # enemy

        self.drawTextLeft(surface, "Level "+ str(self.l), (55,0,55), 832, 35, self.font)


        #follow mouse
        if self.mp[0] < 800:
            pygame.draw.rect(surface, (55, 55, 255), pygame.Rect(self.b[1] * 32+ self.cameraX, self.b[0] * 32+self.cameraY, 32, 32), 3)
            if self.selected != ".":
                if self.selected == "-":
                    pygame.draw.rect(surface, (155, 155, 155), pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32))  # wall
                elif self.selected == "X":
                    pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32))  # lava
                elif self.selected == "1":
                    pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32))  # p1
                elif self.selected == "2":
                    pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32))  # p2
                elif self.selected == "3":
                    pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32))  # p3
                elif self.selected == "4":
                    pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32))  # p4
                elif self.selected == "T":
                    pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32)))  # Telewall 1
                    pygame.draw.rect(surface, (155, 0, 155), pygame.Rect(pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 16, 16)))
                elif self.selected == "t":
                    pygame.draw.rect(surface, (155, 0, 155), pygame.Rect(pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32)))  # Telewall 2
                    pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 16, 16)))
                elif self.selected == "=":
                    pygame.draw.rect(surface, (155, 155, 155),
                                     pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32*4, 32))  # longWall short

                elif self.selected == "[":
                    pygame.draw.rect(surface, (155, 155, 155),
                                     pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32 * 8, 32))  # longWall medium

                elif self.selected == "_":
                    pygame.draw.rect(surface, (155, 155, 155),
                                     pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32 * 16, 32))  # longWall long
                elif self.selected == ";":
                    pygame.draw.rect(surface, (155, 155, 155),
                                     pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32*4))  # tallWall short

                elif self.selected == "/":
                    pygame.draw.rect(surface, (155, 155, 155),
                                     pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32*8))  # tallWall medium

                elif self.selected == "|":
                    pygame.draw.rect(surface, (155, 155, 155),
                                     pygame.Rect(self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 32*16))  # ltallWall long

                elif self.selected == "-":
                    pygame.draw.rect(surface, (155, 155, 155), (self.b[1]*32+self.cameraX,self.b[0]*32+self.cameraY, 32, 16))

                elif self.selected == "+":
                    pygame.draw.rect(surface, (155, 155, 155), (self.b[1] *32+self.cameraX, self.b[0] *32+self.cameraY, 32, 16))
                    pygame.draw.rect(surface, (55, 55, 55), pygame.Rect(self.b[1] *32+self.cameraX, self.b[0] *32+self.cameraY, 32, 32), 3)
                elif self.selected == "E":
                    pygame.draw.rect(surface, (0, 255, 155), (self.b[1] *32+self.cameraX, self.b[0] *32+self.cameraY, 32, 32))
                elif self.selected == "b":
                    pygame.draw.rect(surface, (255, 185, 55),
                                     (self.b[1] * 32 + self.cameraX, self.b[0] * 32 + self.cameraY, 32, 32))

        return

    def drawTextLeft(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return