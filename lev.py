import pygame
import main
from Adventure import Design

def editor():
    pygame.font.init()
    c = Design(980, 640, 60)
    #in 32 chunks it is 25X20
    c.main_loop()
    return




if __name__ == "__main__":
    print "RUNNING LEVEL EDITOR"
    editor()
    print "CLOSE EDITOR"
    main.main()
