from math import floor
import math
from random import uniform
from time import time

class HashMap(object):
    """
    Hashmap is a a spatial index which can be used for a broad-phase
    collision detection strategy.
    """
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.grid = {}

    @classmethod
    def from_objects(cls, cell_size, objs):
        """
        Build a HashMap from a list of points.
        """
        hashmap = cls(cell_size)
        setdefault = hashmap.grid.setdefault
        key = hashmap.key
        for obj in objs:
            setdefault(key(obj),[]).append(obj)
        return hashmap
    @classmethod
    def empty(cls, cell_size):
        hashmap = cls(cell_size)
        setdefault = hashmap.grid.setdefault
        return hashmap

    def key(self, obj):
        cell_size = self.cell_size
        return (
            int((floor(obj.rect[0]/cell_size))*cell_size),
            int((floor(obj.rect[1]/cell_size))*cell_size),
        )

    def insert(self, obj):
        """
        Insert point into the hashmap.
        """
        self.grid.setdefault(self.key(obj), []).append(obj)

    def query(self, obj):
        """
        Return all objects in the cell specified by point.
        """
        return self.grid.setdefault(self.key(obj), [])

    def remove(self, obj):
        """Remove the object obj from the cell at cell_coord."""
        self.grid.setdefault(self.key(obj), []).remove(obj)



class SpatialHash(object):
    def __init__(self, cell_size=10.0):
        self.cell_size = float(cell_size)
        self.d = {}

    def _add(self, cell_coord, o):
        """Add the object o to the cell at cell_coord."""
        try:
            self.d.setdefault(cell_coord, set()).add(o)
        except KeyError:
            self.d[cell_coord] = {o}

    def _cells_for_rect(self, r):
        """Return a set of the cells into which r extends."""
        cells = set()
        cy = floor(r.y1 / self.cell_size)
        while (cy * self.cell_size) <= r.y2:
            cx = floor(r.x1 / self.cell_size)
            while (cx * self.cell_size) <= r.x2:
                cells.add((int(cx), int(cy)))
                cx += 1.0
            cy += 1.0
        return cells

    def add_rect(self, r, obj):
        """Add an object obj with bounds r."""
        cells = self._cells_for_rect(r)
        for c in cells:
            self._add(c, obj)

    def _remove(self, cell_coord, o):
        """Remove the object o from the cell at cell_coord."""
        cell = self.d[cell_coord]
        cell.remove(o)

        # Delete the cell from the hash if it is empty.

        if not cell:
            del (self.d[cell_coord])

    def remove_rect(self, r, obj):
        """Remove an object obj which had bounds r."""
        cells = self._cells_for_rect(r)
        for c in cells:
            self._remove(c, obj)








    """if __name__ == '__main__':
        import tests

        NUM_POINTS = 100000
        new_point = lambda: (
            uniform(-100, 100), uniform(-100, 100), uniform(-100, 100)
        )

        points = [new_point() for i in xrange(NUM_POINTS)]
        T = time()
        hashmap = tests.HashMap.from_points(10, points)
        print 1.0 / (time() - T+1), '%d point builds per second.' % NUM_POINTS

        T = time()
        hashmap.query((0, 0, 0))
        print 1.0 / (time() - T+1), '%d point queries per second.' % NUM_POINTS"""