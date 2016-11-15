import pygame
import pygame.locals

class Game:
    def __init__(self, name, width, height, frames_per_second):
        self.width =width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True


        self.screen = pygame.display.set_mode(

            (width, height),

            pygame.locals.DOUBLEBUF |

            pygame.locals.SRCALPHA)

        pygame.display.set_caption(name)


    def game_logic(self, keys, newkyes, buttons, newbuttons, mouse_position):
        raise NotImplementedError()

    def paint(self, survace):
        raise NotImplementedError()

    def main_loop(self):
        clock = pygame.time.Clock()
        keys = set()
        buttons = set()
        mouse_position = (1,1)

        while True:
            clock.tick(self.frames_per_second)


            newkeys = set()
            newbuttons = set()
            for e in pygame.event.get():

                if e.type == pygame.QUIT:
                    pygame.quit()

                if e.type == pygame.MOUSEBUTTONDOWN:
                    buttons.add(e.button)
                    newbuttons.add(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEBUTTONUP:
                    buttons.discard(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEMOTION:
                    mouse_position = e.pos

                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)
                if e.type == pygame.KEYUP:
                    keys.discard(e.key)

            if self.on:
                self.game_logic(keys, newkeys, buttons, newbuttons, mouse_position)
                self.paint(self.screen)

            pygame.display.flip()






