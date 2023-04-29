import pyxel
import numpy as np
from Tile import Tile
from place_card import place_card
from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, PANNEL_SIZE
from Board import Board
from Player import Player
from Game import Game

# size = tile count
# height/width = pixel count

MAIN_WIDTH = (TILE_SIZE * GRID_SIZE) + (PANNEL_SIZE*TILE_SIZE*2)
MAIN_HEIGHT = TILE_SIZE * (GRID_SIZE + HEADER_SIZE)

class App:
    def __init__(self):
        self.main_width = MAIN_WIDTH
        self.main_height = MAIN_HEIGHT
        pyxel.init(self.main_width, self.main_height)
        pyxel.load('game.pyxres')
        pyxel.mouse(visible=True)
        self.game = Game()
        self.game.initPlayers(4)
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            print("actions")
            self.game.shift_actions()
        self.game.detect_inputs()



    def draw(self):
        pyxel.cls(0)

        self.game.draw_board()
        self.game.draw_header()
        self.game.draw_players()

App()