import pygame
from Adventure import Design

def main():
    pygame.font.init()
    c = Design(800, 640, 60)
    #in 32 chunks it is 25X20
    c.main_loop()
    return




if __name__ == "__main__":
    main()