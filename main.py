import pygame
from Adventure import Adventure

def main():
    pygame.font.init()
    c = Adventure(800, 640, 60)
    c.main_loop()
    return




if __name__ == "__main__":
    main()