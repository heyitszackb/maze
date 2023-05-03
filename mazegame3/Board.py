import pyxel
import random
from get_card_from_file import get_card_from_file
from rotate_card import rotate_card
from Tile import Tile
from place_card import place_card
from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, CARD_FILE_NAME

class Board:
    def __init__(self):
        self.board = self.init_board()
        self.size = GRID_SIZE
        self.vortexesOnBoard = {} # indexs: 'red', 'blue', 'green', 'yellow' (value is an array of tiles that have that color on them)
        self.vortexesOnBoard['red'] = []
        self.vortexesOnBoard['blue'] = []
        self.vortexesOnBoard['green'] = []
        self.vortexesOnBoard['yellow'] = []
    
        if self.can_place_card((GRID_SIZE//2 - 2), (GRID_SIZE//2 - 2)):
            self.place_card('1a', 'North', 11, 11)

    
    def init_board(self):
        board = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                t = Tile()
                t.isVoid = True
                row.append(t)
            board.append(row)
        return board

    def draw(self):
        """Draw the board on the pyxel screen"""
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].draw(i, j)
    
    def can_place_card(self, board_row, board_col):
        """Logic for checking if card placement is valid"""
        if board_row < 0 or board_row > GRID_SIZE - 4:
            return False
        if board_col < 0 or board_col > GRID_SIZE - 4:
            return False
        return True
    

    def place_card(self,card_name, dir,board_row,board_col):
        tile_data_for_card = self.get_tile_data_for_card(card_name, dir)
        for row in range(4):
            for col in range(4):
                # check for adjacent search tiles


                # if len(self.board) < board_col + col:
                #     adjacent_tile_type = self.board[board_col + col][board_row].tile_type
                #     if adjacent_tile_type and 'search' in adjacent_tile_type:
                #         self.board[board_col + col][board_row].tile_type = ''
                # if len(self.board[0]) < board_row + row:
                #     adjacent_tile_type = self.board[board_col][board_row + row].tile_type
                #     if adjacent_tile_type and 'search' in adjacent_tile_type:
                #         self.board[board_col][board_row + row].tile_type = ''
                # if board_col + col > 0:
                #     adjacent_tile_type = self.board[board_col + col - 1][board_row].tile_type
                #     if adjacent_tile_type and 'search' in adjacent_tile_type:
                #         self.board[board_col + col - 1][board_row].tile_type = ''
                # if board_row + row > 0:
                #     adjacent_tile_type = self.board[board_col][board_row + row - 1].tile_type
                #     if adjacent_tile_type and 'search' in adjacent_tile_type:
                #         self.board[board_col][board_row + row - 1].tile_type = ''
                


                
                if len(self.board[0]) < board_row + row:
                    pass


                self.board[board_col + col][board_row + row] = tile_data_for_card[row][col]
                # save off vortexes
                tile_type = tile_data_for_card[row][col].tile_type 
                if tile_type and 'vortex' in tile_type:
                    if 'red' in tile_type:
                        self.vortexesOnBoard['red'].append([board_col + col, board_row + row])
                    if 'blue' in tile_type:
                        self.vortexesOnBoard['blue'].append([board_col + col, board_row + row])
                    if 'green' in tile_type:
                        self.vortexesOnBoard['green'].append([board_col + col, board_row + row])
                    if 'yellow' in tile_type:
                        self.vortexesOnBoard['yellow'].append([board_col + col, board_row + row])


        return self.board
    
    def get_tile_data_for_card(self, card_name, dir):
        tiles = []
        for _ in range(4):
            row = []
            for _ in range(4):
                t = Tile()
                t.isVoid = False
                row.append(t)
            tiles.append(row)

        data = get_card_from_file(card_name, CARD_FILE_NAME)
        data = rotate_card(data, dir)

        for row in range(len(data)):
            for col in range(len(data[row])):
                if (data[row][col][0] == '-') or (data[row][col][0] == '.') or (data[row][col][0] == '='):
                    continue
                else:
                    encoded_direction = [True,True,True,True]
                    encoded_door_direction = [False,False,False,False]
                    if (col < len(data[row]) - 1):
                        if (data[row][col + 1][0] == '-'):
                            encoded_direction[3] = False # East
                        if (data[row][col + 1][0] == '='):
                            encoded_door_direction[3] = True # East
                            encoded_direction[3] = False # East
                    if (col >= 0):
                        if (data[row][col - 1][0] == '-'):
                            encoded_direction[1] = False # West
                        if (data[row][col - 1][0] == '='):
                            encoded_door_direction[1] = True # West
                            encoded_direction[1] = False # West
                            
                    if (row < len(data) - 1):
                        if (data[row + 1][col][0] == '-'):
                            encoded_direction[2] = False # South
                        if (data[row + 1][col][0] == '='):
                            encoded_door_direction[2] = True # South
                            encoded_direction[2] = False # South
                    if (row >= 0):
                        if (data[row - 1][col][0] == '-'):
                            encoded_direction[0] = False # North
                        if (data[row - 1][col][0] == '='):
                            encoded_door_direction[0] = True # North
                            encoded_direction[0] = False # North
                    tiles[int(row // 2)][int(col // 2)].set_tile_walls(encoded_direction)
                    tiles[int(row // 2)][int(col // 2)].set_tile_doors(encoded_door_direction)

                    firstChar = data[row][col][0]
                    secondChar = data[row][col][1]
                    thirdChar = data[row][col][2]
                    fourthChar = data[row][col][3]


                    if firstChar == 'C':
                        if secondChar == 'V': # vortex
                            tiles[int(row // 2)][int(col // 2)].set_tile_type(self.assignColorTileType(thirdChar, 'vortex'))
                        elif secondChar == 'S': #search
                            direction = ''
                            if col == 0:
                                direction = '_west'
                            elif col == 6:
                                direction = '_east'
                            elif row == 0:
                                direction = '_north'
                            elif row == 6:
                                direction = '_south'
                            tiles[int(row // 2)][int(col // 2)].set_tile_type(self.assignColorTileType(thirdChar, 'search', direction=direction))
                        elif secondChar == 'X': # exit
                            tiles[int(row // 2)][int(col // 2)].set_tile_type(self.assignColorTileType(thirdChar, 'exit'))
                        elif secondChar == 'C': # capture
                            tiles[int(row // 2)][int(col // 2)].set_tile_type(self.assignColorTileType(thirdChar, 'capture'))
                    elif firstChar == 'S':
                        if secondChar == 'T':
                            tiles[int(row // 2)][int(col // 2)].set_tile_type('timer')
                        if secondChar == 'M':
                            tiles[int(row // 2)][int(col // 2)].set_tile_type('mage_ball')
                        if secondChar == 'S':
                            tiles[int(row // 2)][int(col // 2)].set_tile_type('security_camera')
                        if secondChar == 'E':
                            tiles[int(row // 2)][int(col // 2)].set_tile_type('card_enter')
                    
        return tiles
    
    def assignColorTileType(self, color, type, direction = ''):
        """Maps:
        G -> 'green_vortex'
        B -> 'blue_vortex'
        Y -> 'yellow_vortex'
        R -> 'red_vortex'

        Types:
        'exit', 'search', 'capture', 'vortex'

        direction: (only for search)
        north
        south
        east
        west

        """
        tile_type = ''
        if color == 'G':
            tile_type = 'green_' + type + direction
        elif color == 'B':
            tile_type = 'blue_' + type + direction
        elif color == 'Y':
            tile_type = 'yellow_' + type + direction
        elif color == 'R':
            tile_type = 'red_' + type + direction

        return tile_type
    


