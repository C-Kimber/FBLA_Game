import pygame
from wall import TWall
from random import uniform
from time import time
import hashmap
from data import Data


if __name__ == '__main__':
    ar = []
    for x in range(0, 400):
        for y in range(0, 40):
            ar.append(TWall(x * 32, y * 32))

    NUM_POINTS = len(ar)


    T = time()
    hashmap = hashmap.HashMap.from_objects(64, ar)
    print 1.0 / (time() - T + 1), '%d point builds per second.' % NUM_POINTS

    T = time()
    print hashmap.query(TWall(32,32))
    print 1.0 / (time() - T + 1), '%d point queries per second.' % NUM_POINTS

