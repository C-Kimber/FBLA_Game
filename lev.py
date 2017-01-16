import pygame
import main
import other
from Adventure import Design


def editor():
    pygame.font.init()
    other.FLAG = pygame.RESIZABLE
    other.WIDTH = 980
    other.HEIGHT = 640
    c = Design(980, 640, 60)

    # in 32 chunks it is 25X20
    c.main_loop()
    return


if __name__ == "__main__":
    print "RUNNING LEVEL EDITOR"
    editor()
    print "CLOSE EDITOR"
    #main.main()
