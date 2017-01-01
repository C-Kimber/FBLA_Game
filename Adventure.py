from game_mouse import Game
from data import Data
from DataD import DataD
import other


class Design(Game):
    def __init__(self, width, height, frame_rate):
        self.newGame(width, height, frame_rate)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        return

    def paint(self, surface):
        self.data.draw(surface)

        return

    def newGame(self, width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        Game.__init__(self, "LEVEL EDITOR", width, height, frame_rate)
        self.data = DataD(width, height, frame_rate)


class Adventure(Game):
    def __init__(self, width, height, frame_rate):
        self.newGame(width, height, frame_rate)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        # switch between modes I.E. menu and game
        if other.GAMESTATE == 0:
            self.data.menuve(keys, newkeys, buttons, newbuttons, mouse_position)
        if other.GAMESTATE == 1:
            self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        if other.GAMESTATE == 2 or other.GAMESTATE == 3:
            self.data.mainEvolve(keys, newkeys, buttons, newbuttons, mouse_position)
        return

    def paint(self, surface):
        if other.GAMESTATE == 0:
            self.data.menuDraw(surface)
        elif other.GAMESTATE == 1:
            self.data.draw(surface)
        elif other.GAMESTATE == 2:
            self.data.mainDraw(surface)
        elif other.GAMESTATE == 3:
            self.data.GameOverDraw(surface)

        return

    def newGame(self, width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        Game.__init__(self, "Uukukoa", width, height, frame_rate)
        self.data = Data(width, height, frame_rate)
