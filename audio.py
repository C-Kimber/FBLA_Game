import pygame
import os

dir = "./assets/sounds"

def load_sounds():
    try:
        sound_library ={
            "stone_1": pygame.mixer.Sound("./assets/sounds/stone_impact.ogg"),
            "stone_2": pygame.mixer.Sound("./assets/sounds/stone_impact_2.ogg"),
            "stone_3": pygame.mixer.Sound("./assets/sounds/stone_impact_3.ogg"),
            "bloop_1": pygame.mixer.Sound("./assets/sounds/lava_boom_1.ogg"),
            "bloop_2": pygame.mixer.Sound("./assets/sounds/lava_boom_1.ogg"),
            "bloop_3": pygame.mixer.Sound("./assets/sounds/lava_boom_1.ogg"),
            "fall_1": pygame.mixer.Sound("./assets/sounds/falling_1.ogg"),
            "fall_2": pygame.mixer.Sound("./assets/sounds/falling_2.ogg"),
            "open_1": pygame.mixer.Sound("./assets/sounds/opening_3.ogg"),
            "thunder": pygame.mixer.Sound("./assets/sounds/thunder_1.ogg"),
        }

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