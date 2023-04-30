from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, PANNEL_SIZE
import pyxel
import time

class Timer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.max_time = 180
        self.time_left = self.max_time
        self.percentage_time_left = self.time_left / self.max_time
        self.width = 26
        self.height = 1
        self.fill_capacity_pixels = (GRID_SIZE * TILE_SIZE) // (self.time_left)

    def draw(self):
        # main rect
        pyxel.rectb(self.x + (PANNEL_SIZE * TILE_SIZE), self.y + (self.height * TILE_SIZE), (self.width * TILE_SIZE), TILE_SIZE, 7)

        # fill rect
        pyxel.rect(self.x + (PANNEL_SIZE * TILE_SIZE), self.y + (self.height * TILE_SIZE), (self.width * TILE_SIZE * self.percentage_time_left), TILE_SIZE, 7)

    def decrease_time_left(self):
        self.time_left -= 0.04
        # self.time_left -= 1
        self.percentage_time_left = self.time_left / self.max_time

    def hitTimerSpace(self):
        INCREASE = 40
        if self.time_left + INCREASE <= self.max_time:
            self.time_left += INCREASE
        else:
            self.time_left = self.max_time

    def isEmpty(self):
        if self.time_left <= 0:
            return True
        else:
            return False

    