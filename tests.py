import pygame, sys
import audio
white = (255, 255, 255)

pygame.init()
pygame.display.set_caption('Basic Sound Example')
size = [640, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
sound_lib = audio.load_sounds()
pygame.mixer.set_num_channels(8)
music_chan = pygame.mixer.Channel(5)
# load sound file
sound = pygame.mixer.Sound('assets/sounds/fanfare.ogg')
print 'the sound file is',sound.get_length(),'seconds long.'

print 'press 1 - play sound'
print 'press 2 - play sound continuously in a loop'
print 'press 3 - play sound but start with 3 seconds fade-in effect'
print 'press 4 - play sound for 5 seconds'
print 'press 5 - play sound 3 more times'
print 'press 9 - stop playing with 3 seconds fadeout effect'
print 'press 0 - stop playing instantly'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:

                if not music_chan.get_busy():
                    music_chan.play(sound)
            if event.key == pygame.K_2:
                sound.play(-1)
            if event.key == pygame.K_3:
                sound.play(-1, fade_ms=3000)
            if event.key == pygame.K_4:
                sound.play(-1, 5000)
            if event.key == pygame.K_5:
                sound.play(3)
            if event.key == pygame.K_6:
                sound.set_volume(.05)
            if event.key == pygame.K_9:
                sound.fadeout(3000)
            if event.key == pygame.K_0:
                sound.stop()
            if event.key == pygame.K_8:
                sound_lib["uh_oh"].play()
    screen.fill(white)
    pygame.display.update()
    clock.tick(20)
