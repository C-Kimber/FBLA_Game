import math

import pygame
import pygame.locals

import other
from data import Data
x = 3
y = 30
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


class Game:
    background = (0, 0, 800, 640)

    def __init__(self, name, width, height, frames_per_second):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True
        self.isFull = False
        flags = pygame.locals.DOUBLEBUF | pygame.locals.SRCALPHA
        if other.EDITING == False:
            flags = pygame.locals.DOUBLEBUF | pygame.locals.SRCALPHA | pygame.locals.RESIZABLE


        self.screen = pygame.display.set_mode(

            (other.WIDTH, other.HEIGHT),

            flags
            , 8)

        pygame.display.set_caption(name)
        #pygame.display.toggle_fullscreen()

    def game_logic(self, keys, newkyes, buttons, newbuttons, mouse_position):
        raise NotImplementedError()

    def paint(self, survace):
        raise NotImplementedError()

    def main_loop(self):
        clock = pygame.time.Clock()
        keys = set()
        buttons = set()
        mouse_position = (1, 1)

        while self.on:
            clock.tick(self.frames_per_second)
            other.FPS = int(math.floor(clock.get_fps()))
            other.ISFULLSCREEN = self.isFull
            self.on = other.ON
            newkeys = set()
            newbuttons = set()
            for e in pygame.event.get():

                if e.type == pygame.QUIT:
                    self.on = False
                    # sys.exit(0)

                #if e.type == pygame.

                if e.type == pygame.MOUSEBUTTONDOWN:
                    buttons.add(e.button)
                    newbuttons.add(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEBUTTONUP:
                    buttons.discard(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEMOTION:
                    mouse_position = e.pos

                if e.type == pygame.locals.VIDEORESIZE:
                    new_width = e.dict['size'][0]
                    new_height = e.dict['size'][1]
                    other.WIDTH, other.HEIGHT = new_width, new_height

                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)

                    if e.key == pygame.K_F10:
                       if self.isFull:
                            self.screen = pygame.display.set_mode(

                                (self.width, self.height-64),

                                pygame.locals.DOUBLEBUF |

                                pygame.locals.SRCALPHA | pygame.locals.RESIZABLE
                                , 32)
                            other.WIDTH, other.HEIGHT = self.width, self.height

                       else:
                            self.screen = pygame.display.set_mode(

                                (self.width, self.height),

                                pygame.locals.DOUBLEBUF |

                                pygame.locals.SRCALPHA | pygame.locals.FULLSCREEN
                                , 32)
                            other.WIDTH, other.HEIGHT = pygame.display.list_modes()[0]
                       self.isFull = not self.isFull

                if e.type == pygame.KEYUP:
                    keys.discard(e.key)

                """elif e.type == pygame.ACTIVEEVENT:
                    print 'state:', e.state, '| gain:', e.gain,
                    if e.state == 1:
                        print e.
                        if self.screen.get_flags() & e.gain == 0:
                            self.screen = pygame.display.set_mode(

                                (self.width, self.height),

                                pygame.locals.DOUBLEBUF |

                                pygame.locals.SRCALPHA | pygame.locals.RESIZABLE
                                , 32)
                            print "| mouse out",
                        elif e.gain == 1:
                            print "| mouse in",
                    elif e.state == 2:
                        if e.gain == 0:
                            print "| titlebar pressed",
                        elif e.gain == 1:
                            print "| titlebar unpressed",
                    elif e.state == 6:
                        if e.gain == 0:
                            print "| window minimized",
                    elif e.state == 4:
                        if e.gain == 1:
                            print "| window normal","""

            if self.on:
                self.game_logic(keys, newkeys, buttons, newbuttons, mouse_position)
                self.paint(self.screen)
            rects = ((0, 0, 1000, 500), (0, 500, 1000, 500))
            pygame.display.flip()
            """if hasattr(Data, "rs"):
                pygame.display.update(Data.rs)
            else:
                pygame.display.flip()
                #pygame.display.update(rects)
            if Data.allwalls is not None:
                Data.allwalls.clear(self.screen, Game.background)"""
