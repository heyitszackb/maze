import random
import pyxel
from mappings import color_tile_mappings, base_tile_mappings, door_mappings
from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, PANNEL_SIZE

class Tile:
    def __init__(self,tile_type = None):
        self.tile_encoding = None
        self.tile_type = tile_type
        self.isVoid = True
        self.token = None
        
        # self.tile_id = None
        # self.escalatorStatus = None # 'None', 'escalator_1', 'escalator_2'
        self.north = False
        self.west = False
        self.south = False
        self.east = False

        self.door_north = False
        self.door_west = False
        self.door_south = False
        self.door_east = False
        # tile_x is the x position on the pyxel screen of the tile in the top right corner 
        # tile_y is the y position on the pyxel screen of the tile in the top right corner 
        # board_row is the row of the tile in the board object (0, 25)
        # board_col is the column of the tile in the board object (0, 25)
    
    def get_position(self, board_row , board_col):
        """Calculate the x,y position of the tile on the pyxel grid given the board row and col."""
        tile_x = (board_row * TILE_SIZE) + (PANNEL_SIZE * TILE_SIZE)
        tile_y = (board_col * TILE_SIZE) + (HEADER_SIZE * TILE_SIZE)
        return tile_x, tile_y

    # i, j is the position on the grid
    def draw_base_tile(self, board_row, board_col):
        """Draw the base tile image."""
        if self.isVoid:
            return
        tile_map_x, tile_map_y = base_tile_mappings[(self.north, self.west, self.south, self.east)]
        tile_x, tile_y = self.get_position(board_row, board_col)
        pyxel.blt(tile_x,tile_y,0,tile_map_x*TILE_SIZE,tile_map_y*TILE_SIZE,TILE_SIZE,TILE_SIZE)

    def draw_decorators(self, board_row, board_col):
        """Draw any decorators on the tile"""
        if self.tile_type in color_tile_mappings:
            tile_map_x, tile_map_y = color_tile_mappings[self.tile_type]
            tile_x, tile_y = self.get_position(board_row, board_col)
            pyxel.blt(tile_x,tile_y,0,tile_map_x*TILE_SIZE,tile_map_y*TILE_SIZE,TILE_SIZE,TILE_SIZE,7)

    def draw_doors(self, board_row, board_col):
        """Draw any doors on tile"""
        tile_map_x, tile_map_y = door_mappings[(self.door_north, self.door_west, self.door_south, self.door_east)]
        tile_x, tile_y = self.get_position(board_row, board_col)
        pyxel.blt(tile_x,tile_y,0,tile_map_x*TILE_SIZE,tile_map_y*TILE_SIZE,TILE_SIZE,TILE_SIZE,7)


    def draw(self, board_row, board_col):
        """Draw a tile on the pyxel screen"""
        self.draw_base_tile(board_row, board_col)
        self.draw_decorators(board_row, board_col)
        self.draw_doors(board_row, board_col)

    def set_tile_type(self, type):
        """Set the tile type"""
        self.tile_type = type

    def set_tile_walls(self, encoded_walls):
        """Set the tile walls"""
        self.north = encoded_walls[0]
        self.west = encoded_walls[1]
        self.south = encoded_walls[2]
        self.east = encoded_walls[3]

    def set_tile_doors(self, encoded_doors):
        """Set the tile doors"""
        self.door_north = encoded_doors[0]
        self.door_west = encoded_doors[1]
        self.door_south = encoded_doors[2]
        self.door_east = encoded_doors[3]


