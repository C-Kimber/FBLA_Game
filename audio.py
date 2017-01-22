import pygame
import os

dir = "./assets/sounds"

def load_sounds():
    try:
        sound_library ={
            "stone_1": pygame.mixer.Sound("stone_impact.ogg"),
            "stone_2": pygame.mixer.Sound("stone_impact_2.ogg"),
            "stone_3": pygame.mixer.Sound("stone_impact_3.ogg"),
            "bloop_1": pygame.mixer.Sound("lava_boom_1.ogg"),
            "bloop_2": pygame.mixer.Sound("lava_boom_1.ogg"),
            "bloop_3": pygame.mixer.Sound("lava_boom_1.ogg"),
            "coins_1": pygame.mixer.Sound("getcoins1.ogg"),
            "coins_2": pygame.mixer.Sound("getcoins2.ogg"),
            "coins_3": pygame.mixer.Sound("getcoins3.ogg"),
            "fall_1":  pygame.mixer.Sound("falling_1.ogg"),
            "fall_2":  pygame.mixer.Sound("falling_2.ogg"),
            "open_1":  pygame.mixer.Sound("opening_3.ogg"),
            "thunder": pygame.mixer.Sound("thunder_1.ogg"),
            "music":   pygame.mixer.Sound('music.ogg'),
            "uh_oh":   pygame.mixer.Sound('uh_oh.ogg'),
            "fanfare": pygame.mixer.Sound('fanfare.ogg'),
        }
        sound_library["music"].set_volume(.05)
    except pygame.error, message:
        print "cannot load sounds"
        sound_library = None

    return sound_library



def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

  #effect = pygame.mixer.Sound('beep.wav')
  #effect.play()