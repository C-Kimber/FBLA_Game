import pygame
from Adventure import Adventure
import other
import cProfile as profile




def main():
    pygame.font.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    other.getRes()
    other.FLAG = pygame.FULLSCREEN
    c = Adventure(other.WIDTH, other.HEIGHT, other.FRAMES)
    # in 32 chunks it is 25X20
    c.main_loop()
    "doing things"
    return

if __name__ == "__main__":
    print "RUNNING GAME"
    #profile.run('main()')
    main()
    print "SHUTTING DOWN GAME"

