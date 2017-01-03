from pygame import *

import other


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move((self.state.topleft[0],self.state.topleft[1]) )

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l + other.HALF_WIDTH, -t + other.HALF_HEIGHT, w, h)


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + int(other.WIDTH/2), -t + int(other.HEIGHT/2), w, h

    l = min(-32, l)  # stop scrolling at the left edge
    # 7008,   #7872
    if other.ISFULLSCREEN == True:
        n = 288
    else:
        n = 64
    l = max(-(other.TOTAL_LEVEL_WIDTH-45*32+10), l)  # stop scrolling at the right edge
    t = max(-(other.HEIGHT-n), t)  # stop scrolling at the bottom
    t = min(0, t)  # stop scrolling at the top
    return Rect(l, t, w, h)
