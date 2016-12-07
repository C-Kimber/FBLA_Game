import spritesheet

GAMESTATE = 1
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




def load_images():
    images = {
        "frag1" :spritesheet.spritesheet('./assets/images/frag_1.png').image_at((0, 0, 64, 64), (0, 0, 0,)).convert_alpha(),#0
        "frag2":spritesheet.spritesheet('./assets/images/frag_2.png').image_at((0, 0, 64, 64), (0, 0, 0,)).convert_alpha(),#1
        "frag3":spritesheet.spritesheet('./assets/images/frag_3.png').image_at((0, 0, 64, 64), (0, 0, 0,)).convert_alpha(),#3
        "frag1_1":spritesheet.spritesheet('./assets/images/frag_1_2.png').image_at((0, 0, 32, 32),    (0, 0, 0,)).convert_alpha(),#4
        "frag1_2": spritesheet.spritesheet('./assets/images/frag_1_3.png').image_at((0, 0, 32, 32),                                                                        (0, 0, 0,)).convert_alpha(),  # 4
        "frag2_1": spritesheet.spritesheet('./assets/images/frag_2_1.png').image_at((0, 0, 32, 32),(0, 0, 0,)).convert_alpha(),  # %
        "frag3_1": spritesheet.spritesheet('./assets/images/frag_3_1.png').image_at((0, 0, 32, 32),(0, 0, 0,)).convert_alpha(),  # 6
        "frag2_2":spritesheet.spritesheet('./assets/images/frag_2_2.png').image_at((0, 0, 16, 16),      (0, 0, 0,)).convert_alpha(),#%
        "frag3_2":spritesheet.spritesheet('./assets/images/frag_3_2.png').image_at((0, 0, 16, 16),    (0, 0, 0,)).convert_alpha(),#6
        "player1":spritesheet.spritesheet('./assets/images/Player1_small.png').image_at((0, 0, 32, 32),  (255, 255, 255)).convert_alpha(),#8
        "player2":spritesheet.spritesheet('./assets/images/Player2_small.png').image_at((0, 0, 32, 32),(255, 255, 255)).convert_alpha(),#9
        "wall_1":spritesheet.spritesheet('./assets/images/wall1_small.png').image_at((0, 0, 32, 32),(255, 255, 255)).convert_alpha(),#10
        "wall_1_tall": spritesheet.spritesheet('./assets/images/wall1_small_tall.png').image_at((0, 0, 32, 32),(255, 255, 255)).convert_alpha(),#11
        "wall_1_long": spritesheet.spritesheet('./assets/images/wall1_small_long.png').image_at((0, 0, 32, 32),(255, 255, 255)).convert_alpha(),#12
        "up_wall": spritesheet.spritesheet('./assets/images/upwall.png').image_at((0, 0, 32, 32), (254, 254, 254)).convert_alpha(),#13
        "t_wall_1": spritesheet.spritesheet('./assets/images/telewall_sheet.png').image_at((0, 0, 32, 32),(255,255, 255)).convert_alpha(),#14
        "t_wall_2": spritesheet.spritesheet('./assets/images/telewall2_sheet.png').image_at((0, 0, 32, 32), (255, 255,255)).convert_alpha(),#15
        "lava": spritesheet.spritesheet('./assets/images/deathwall1_small.png').image_at((0, 0, 32, 32),(255, 255, 255)).convert_alpha(),#16
        "finish": spritesheet.spritesheet('./assets/images/finish.png').image_at((0, 0, 32, 32), (255, 255, 255)).convert_alpha(),
    }
    return images

