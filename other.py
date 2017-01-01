import math

import spritesheet
import pygame

GAMESTATE = 2
MINISTATE = 0
FPS = 0
WIDTH = 1366
HEIGHT = 768
ISFULLSCREEN = False
EDITING = False
ON = True

# CONSTANTS

FRAMES = 60
HALF_WIDTH = int(WIDTH / 2)
HALF_HEIGHT = int(HEIGHT / 2)
CAMERA_SLACK = 30
TOTAL_LEVEL_WIDTH = 0
TOTAL_LEVEL_HEIGHT = 0


# Store useful variables




def load_images():
    images = {
        "frag1": spritesheet.spritesheet('./assets/images/frag_1.png').image_at((0, 0, 64, 64),
                                                                                (0, 0, 0,)).convert_alpha(),  # 0
        "frag2": spritesheet.spritesheet('./assets/images/frag_2.png').image_at((0, 0, 64, 64),
                                                                                (0, 0, 0,)).convert_alpha(),  # 1
        "frag3": spritesheet.spritesheet('./assets/images/frag_3.png').image_at((0, 0, 64, 64),
                                                                                (0, 0, 0,)).convert_alpha(),  # 3
        "frag1_1": spritesheet.spritesheet('./assets/images/frag_1_2.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert_alpha(),  # 4
        "frag1_2": spritesheet.spritesheet('./assets/images/frag_1_3.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert_alpha(),  # 4
        "frag2_1": spritesheet.spritesheet('./assets/images/frag_2_1.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert_alpha(),  # %
        "frag3_1": spritesheet.spritesheet('./assets/images/frag_3_1.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert_alpha(),  # 6
        "frag2_2": spritesheet.spritesheet('./assets/images/frag_2_2.png').image_at((0, 0, 16, 16),
                                                                                    (0, 0, 0,)).convert_alpha(),  # %
        "frag3_2": spritesheet.spritesheet('./assets/images/frag_3_2.png').image_at((0, 0, 16, 16),
                                                                                    (0, 0, 0,)).convert_alpha(),  # 6

        "player1": spritesheet.spritesheet('./assets/images/Player1.png').image_at((0, 0, 32, 32),
                                                                                   (254, 254, 254)).convert_alpha(),
        # 8
        "player2": spritesheet.spritesheet('./assets/images/Player2_small.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert_alpha(),  # 9

        "wall_1": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 0, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        # 10
        "wall_2": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 1, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        "wall_3": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 2, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        "wall_4": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 0, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        "wall_5": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 1, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        "wall_6": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 2, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        # 10
        "wall_7": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 0, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        "wall_8": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 1, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        "wall_9": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 2, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)).convert_alpha(),
        "wall_10": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 0, 32 * 0, 32, 32), (
            254, 254, 254)).convert_alpha(),
        "wall_11": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 0, 32 * 1, 32, 32), (
            254, 254, 254)).convert_alpha(),
        "wall_12": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 0, 32 * 2, 32, 32), (
            254, 254, 254)).convert_alpha(),
        "wall_13": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 1, 32 * 0, 32, 32), (
            254, 254, 254)).convert_alpha(),
        "wall_14": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 1, 32 * 1, 32, 32), (
            254, 254, 254)).convert_alpha(),
        "wall_15": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 2, 32 * 0, 32, 32), (
            254, 254, 254)).convert_alpha(),
        "wall_16": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 1, 32 * 2, 32, 32), (
            254, 254, 254)).convert_alpha(),

        "back_wall_1": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 0, 32 * 0, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_2": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 1, 32 * 0, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_3": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 2, 32 * 0, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_4": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 0, 32 * 1, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_5": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 1, 32 * 1, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_6": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 2, 32 * 1, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_7": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 0, 32 * 2, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_8": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 1, 32 * 2, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_9": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 2, 32 * 2, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_10": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 0, 32 * 0, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_11": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 0, 32 * 1, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_12": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 0, 32 * 2, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_13": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 1, 32 * 0, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_14": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 1, 32 * 1, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_15": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 2, 32 * 0, 32, 32), (254, 254, 254)).convert_alpha(),
        "back_wall_16": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 1, 32 * 2, 32, 32), (254, 254, 254)).convert_alpha(),

        "wall_1_tall": spritesheet.spritesheet('./assets/images/wall1_small_tall.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert_alpha(),  # 11
        "wall_1_long": spritesheet.spritesheet('./assets/images/fallenPillar.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert_alpha(),  # 12
        "up_wall": spritesheet.spritesheet('./assets/images/upwall.png').image_at((0, 0, 32, 32),
                                                                                  (254, 254, 254)).convert_alpha(),
        # 13
        "t_wall_1": spritesheet.spritesheet('./assets/images/telewall_sheet.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert_alpha(),  # 14
        "t_wall_2": spritesheet.spritesheet('./assets/images/telewall2_sheet.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert_alpha(),  # 15
        "lava": spritesheet.spritesheet('./assets/images/lava.png').image_at((0, 0, 32, 32),
                                                                             (255, 255, 255)).convert_alpha(),  # 16
        "finish": spritesheet.spritesheet('./assets/images/crystal_1.png').image_at((0, 0, 32, 32),
                                                                                    (254, 254, 254)).convert_alpha(),
        "enemy": spritesheet.spritesheet('./assets/images/enemy.png').image_at((0, 0, 32, 32),
                                                                               (254, 254, 254)).convert_alpha(),
        "hitwall": spritesheet.spritesheet('./assets/images/crate.png').image_at((0, 0, 32, 32),
                                                                                 (254, 254, 254)).convert_alpha(),

        "circle_1": pygame.image.load('./assets/images/circle.png').convert_alpha()
        # spritesheet.spritesheet('./assets/images/circle.png').image_at((0, 0, 96, 96))#.convert_alpha(),

    }
    return images

def unitNum(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

def getRes():
    pygame.init()
    import other
    infoObject = pygame.display.Info()
    print "SCREEN RESOLUTION: " + str(infoObject.current_w)+" X "+ str(infoObject.current_h)
    other.WIDTH, other.HEIGHT = infoObject.current_w, infoObject.current_h


def button(mp,rect):
    mx = mp[0]
    my = mp[1]
    rx, ry, rw, rh = rect
    if ((mx >= rx and mx <= rx + rw) and ( my >= ry and my <= ry + rh)):  # If mouse is in the rectangle

        return True
    else:
        return False

def buttonClick(mp, rect, newbuttons):
    if button(mp, rect):
        if 1 in newbuttons:
            return True
        else:
            return False

def constrain(num, minm, maxm):
    """Takes number and constrains it to the given numbers
    It does set the num equal to the maxm when over
    """
    if num > maxm:
        num = maxm
    elif num < minm:
        num = minm
    return num

def resetNum(num ,minm, maxm):
    if num > maxm:
        num = minm
    elif num < minm:
        num = maxm
    return num

def distance(X, Y):
    """ both X and Y are tuples"""
    x = (X[0]-X[1])**2
    y = (Y[0]-Y[1])**2
    return math.sqrt(x+y)





