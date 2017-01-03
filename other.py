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
off_screen = pygame.Surface((WIDTH, HEIGHT))

# CONSTANTS

FRAMES = 60
HALF_WIDTH = int(WIDTH / 2)
HALF_HEIGHT = int(HEIGHT / 2)
CAMERA_SLACK = 30
TOTAL_LEVEL_WIDTH = 0
TOTAL_LEVEL_HEIGHT = 0
LEVEL_TIME = 200
STARTING_LEVEL = 0


# Store useful variables




def load_images():
    images = {
        "frag1": spritesheet.spritesheet('./assets/images/frag_1.png').image_at((0, 0, 64, 64),
                                                                                (0, 0, 0,)).convert(),  # 0
        "frag2": spritesheet.spritesheet('./assets/images/frag_2.png').image_at((0, 0, 64, 64),
                                                                                (0, 0, 0,)).convert(),  # 1
        "frag3": spritesheet.spritesheet('./assets/images/frag_3.png').image_at((0, 0, 64, 64),
                                                                                (0, 0, 0,)).convert(),  # 3
        "frag1_1": spritesheet.spritesheet('./assets/images/frag_1_2.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert(),  # 4
        "frag1_2": spritesheet.spritesheet('./assets/images/frag_1_3.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert(),  # 4
        "frag2_1": spritesheet.spritesheet('./assets/images/frag_2_1.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert(),  # %
        "frag3_1": spritesheet.spritesheet('./assets/images/frag_3_1.png').image_at((0, 0, 32, 32),
                                                                                    (0, 0, 0,)).convert(),  # 6
        "frag2_2": spritesheet.spritesheet('./assets/images/frag_2_2.png').image_at((0, 0, 16, 16),
                                                                                    (0, 0, 0,)).convert(),  # %
        "frag3_2": spritesheet.spritesheet('./assets/images/frag_3_2.png').image_at((0, 0, 16, 16),
                                                                                    (0, 0, 0,)).convert(),  # 6

        "player1": spritesheet.spritesheet('./assets/images/Player1.png').image_at((0, 0, 32, 32),
                                                                                   (255, 0, 0)).convert(),
        # 8
        "player2": spritesheet.spritesheet('./assets/images/Player2_small.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert(),  # 9

        "wall_1": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 0, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        # 10
        "wall_2": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 1, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "wall_3": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 2, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "wall_4": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 0, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "wall_5": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 1, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "wall_6": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 2, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        # 10
        "wall_7": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 0, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "wall_8": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 1, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "wall_9": spritesheet.spritesheet('./assets/images/grass_sheet.png').image_at((32 * 2, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "wall_10": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 0, 32 * 0, 32, 32), (
            254, 254, 254)).convert(),
        "wall_11": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 0, 32 * 1, 32, 32), (
            254, 254, 254)).convert(),
        "wall_12": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 0, 32 * 2, 32, 32), (
            254, 254, 254)).convert(),
        "wall_13": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 1, 32 * 0, 32, 32), (
            254, 254, 254)).convert(),
        "wall_14": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 1, 32 * 1, 32, 32), (
            254, 254, 254)).convert(),
        "wall_15": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 2, 32 * 0, 32, 32), (
            254, 254, 254)).convert(),
        "wall_16": spritesheet.spritesheet('./assets/images/grass_sheet_2.png').image_at((32 * 1, 32 * 2, 32, 32), (
            254, 254, 254)).convert(),

        "back_wall_1": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 0, 32 * 0, 32, 32), (254, 254, 254)).convert(),
        "back_wall_2": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 1, 32 * 0, 32, 32), (254, 254, 254)).convert(),
        "back_wall_3": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 2, 32 * 0, 32, 32), (254, 254, 254)).convert(),
        "back_wall_4": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 0, 32 * 1, 32, 32), (254, 254, 254)).convert(),
        "back_wall_5": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 1, 32 * 1, 32, 32), (254, 254, 254)).convert(),
        "back_wall_6": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 2, 32 * 1, 32, 32), (254, 254, 254)).convert(),
        "back_wall_7": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 0, 32 * 2, 32, 32), (254, 254, 254)).convert(),
        "back_wall_8": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 1, 32 * 2, 32, 32), (254, 254, 254)).convert(),
        "back_wall_9": spritesheet.spritesheet('./assets/images/back_grass_sheet.png').image_at(
            (32 * 2, 32 * 2, 32, 32), (254, 254, 254)).convert(),
        "back_wall_10": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 0, 32 * 0, 32, 32), (254, 254, 254)).convert(),
        "back_wall_11": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 0, 32 * 1, 32, 32), (254, 254, 254)).convert(),
        "back_wall_12": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 0, 32 * 2, 32, 32), (254, 254, 254)).convert(),
        "back_wall_13": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 1, 32 * 0, 32, 32), (254, 254, 254)).convert(),
        "back_wall_14": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 1, 32 * 1, 32, 32), (254, 254, 254)).convert(),
        "back_wall_15": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 2, 32 * 0, 32, 32), (254, 254, 254)).convert(),
        "back_wall_16": spritesheet.spritesheet('./assets/images/back_grass_sheet_2.png').image_at(
            (32 * 1, 32 * 2, 32, 32), (254, 254, 254)).convert(),

        "wall_1_tall": spritesheet.spritesheet('./assets/images/wall1_small_tall.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert(),  # 11
        "wall_1_long": spritesheet.spritesheet('./assets/images/fallenPillar.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert(),  # 12
        "up_wall_1": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 0, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        # 10
        "up_wall_2": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 1, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "up_wall_3": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 2, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "up_wall_4": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 0, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "up_wall_5": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 1, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "up_wall_6": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 2, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        # 10
        "up_wall_7": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 0, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "up_wall_8": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 1, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "up_wall_9": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 2, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)).convert(),
        "up_wall_10": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 0, 32 * 0, 32, 32), (
            254, 254, 254)).convert(),
        "up_wall_11": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 0, 32 * 1, 32, 32), (
            254, 254, 254)).convert(),
        "up_wall_12": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 0, 32 * 2, 32, 32), (
            254, 254, 254)).convert(),
        "up_wall_13": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 1, 32 * 0, 32, 32), (
            254, 254, 254)).convert(),
        "up_wall_14": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 1, 32 * 1, 32, 32), (
            254, 254, 254)).convert(),
        "up_wall_15": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 2, 32 * 0, 32, 32), (
            254, 254, 254)).convert(),
        "up_wall_16": spritesheet.spritesheet('./assets/images/grass_sheet_3.png').image_at((32 * 1, 32 * 2, 32, 32), (
            254, 254, 254)).convert(),
        # 13
        "t_wall_1": spritesheet.spritesheet('./assets/images/telewall_sheet.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert(),  # 14
        "t_wall_2": spritesheet.spritesheet('./assets/images/telewall2_sheet.png').image_at((0, 0, 32, 32), (
            255, 255, 255)).convert(),  # 15
        "lava": spritesheet.spritesheet('./assets/images/lava.png').image_at((0, 0, 32, 32),
                                                                             (255, 255, 255)).convert(),  # 16
        "finish": spritesheet.spritesheet('./assets/images/crystal_1.png').image_at((0, 0, 32, 32),
                                                                                    (254, 254, 254)).convert(),
        "enemy": spritesheet.spritesheet('./assets/images/enemy.png').image_at((0, 0, 32, 32),
                                                                               (254, 254, 254)).convert(),
        "hitwall": spritesheet.spritesheet('./assets/images/crate.png').image_at((0, 0, 32, 32),
                                                                                 (254, 254, 254)).convert(),

        "circle_1": pygame.image.load('./assets/images/circle.png')
        # spritesheet.spritesheet('./assets/images/circle.png').image_at((0, 0, 96, 96))#,

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


def getTileState(left, right, top, bot, char="-"):
    if left == char:
        if right == char:
            if bot == char:
                if top == char:
                    f = 4

                else:
                    f = 1
            elif top == char:
                f = 7
            else:
                f = 13
        elif top == char:
            if bot == char:
                f = 5
            else:
                f = 8
        elif bot == char:
            f = 2
        else:
            f = 14
            # elif:
    elif right == char:  # NO LEFT
        if top == char:
            if bot == char:
                f = 3
            else:
                f = 6
        elif bot == char:
            f = 0
        else:
            f = 12
    elif top == char:  # NO LEFT OR RIGHT
        if bot == char:
            f = 10
        else:
            f = 11
    elif bot == char:  # NO LEFT, RIGHT, OR UP
        f = 9

    else:
        f = 15

    return f





