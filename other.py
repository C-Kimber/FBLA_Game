import spritesheet

GAMESTATE = 0
MINISTATE = 0

WIDTH = 800
HEIGHT = 640
FRAMES = 60
HALF_WIDTH = int(WIDTH/2)
HALF_HEIGHT = int(HEIGHT/2)
CAMERA_SLACK = 30
TOTAL_LEVEL_WIDTH = 0
TOTAL_LEVEL_HEIGHT = 0

#Store useful variables

fragss = None
def load_images():
    fragss = [spritesheet.spritesheet('./assets/images/frag_1.png'),
              spritesheet.spritesheet('./assets/images/frag_2.png'),
              spritesheet.spritesheet('./assets/images/frag_3.png'),
              spritesheet.spritesheet('./assets/images/frag_1_1.png'),
              spritesheet.spritesheet('./assets/images/frag_2_2.png'),
              spritesheet.spritesheet('./assets/images/frag_3_2.png'),
              spritesheet.spritesheet('./assets/images/frag_1_3.png'),
              spritesheet.spritesheet('./assets/images/frag_2_3.png'),
              spritesheet.spritesheet('./assets/images/frag_3_3.png')
              ]


