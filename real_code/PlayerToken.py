import pyxel
from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, PANNEL_SIZE
from mappings import playerCursors, playerTokens
import random

class PlayerToken():
    def __init__(self, color, x, y, buttons=[]):
        self.board_row = x # X - these are switched but whatever x
        self.board_col = y # Y - these are switched but whatever y
        self.color = color # '10: red', '9: yellow', '2: green', '11: blue'
        self.all_buttons = buttons
        self.players_with_token_selected = []


    
    def change_player_color_when_selected(self):
        for player in self.players_with_token_selected:
            player.color = self.color
            player.draw_player_controls()


    def get_position(self, board_row , board_col):
        """Calculate the x,y position of the tile on the pyxel grid given the board row and col."""
        tile_x = (board_row * TILE_SIZE) + (PANNEL_SIZE * TILE_SIZE)
        tile_y = (board_col * TILE_SIZE) + (HEADER_SIZE * TILE_SIZE)
        return tile_x, tile_y

    # i, j is the position on the grid
    def draw(self):

        # cursor(s)
        """Draw the cursor on the board"""
        for player in self.players_with_token_selected:
            tile_map_x, tile_map_y = playerCursors[player.player_name]
            tile_x, tile_y = self.get_position(self.board_row, self.board_col)
            pyxel.blt(tile_x,tile_y,0,tile_map_x*TILE_SIZE,tile_map_y*TILE_SIZE,TILE_SIZE,TILE_SIZE,0)

        # token
        """Draw the token on the board"""
        tile_map_x, tile_map_y = playerTokens[self.color]
        tile_x, tile_y = self.get_position(self.board_row, self.board_col)
        pyxel.blt(tile_x,tile_y,0,tile_map_x*TILE_SIZE,tile_map_y*TILE_SIZE,TILE_SIZE,TILE_SIZE,0)


    def select_token(self, player):
        self.players_with_token_selected.append(player)
        self.change_player_color_when_selected()

    def deselect_token(self, player):
        self.players_with_token_selected.remove(player)


    def spawnNewTile(self, current_tile_type, token_to_move, board):
        direction =  ''
        color = ''
        if 'north' in current_tile_type:
            direction = 'North'
        elif 'west' in current_tile_type:
            direction = 'West'
        elif 'south' in current_tile_type:
            direction = 'South'
        elif 'east' in current_tile_type:
            direction = 'East'

        if 'green' in current_tile_type:
            color = 'green'
        elif 'blue' in current_tile_type:
            color = 'blue'
        elif 'yellow' in current_tile_type:
            color = 'yellow'
        elif 'red' in current_tile_type:
            color = 'red'

        randomCard = random.randint(2,24)
        randomCard = str(randomCard)

        if (direction == 'North') and (token_to_move.color == color):
            if board.can_place_card(token_to_move.board_col - 4, token_to_move.board_row - 1):
                # place tile
                board.place_card(randomCard, 'North', token_to_move.board_col- 4, token_to_move.board_row - 1)

                # remove walls from the tile
                board.board[token_to_move.board_row][token_to_move.board_col].north = False
                board.board[token_to_move.board_row][token_to_move.board_col - 1].south = False

                # remove that tile as a search tile
                board.board[token_to_move.board_row][token_to_move.board_col].set_tile_type('')

        if (direction == 'South') and (token_to_move.color == color):
            if board.can_place_card(token_to_move.board_col + 1, token_to_move.board_row - 2):
                # place tile
                board.place_card(randomCard, 'South', token_to_move.board_col + 1, token_to_move.board_row - 2)

                # remove walls from the tile
                board.board[token_to_move.board_row][token_to_move.board_col].south = False
                board.board[token_to_move.board_row][token_to_move.board_col + 1].north = False

                # remove that tile as a search tile 
                board.board[token_to_move.board_row][token_to_move.board_col].set_tile_type('')

        if (direction == 'East') and (token_to_move.color == color):
            if board.can_place_card(token_to_move.board_col - 1, token_to_move.board_row + 1):
                # place tile
                board.place_card(randomCard, 'East', token_to_move.board_col - 1, token_to_move.board_row + 1)

                # remove walls from the tile
                board.board[token_to_move.board_row][token_to_move.board_col].east = False
                board.board[token_to_move.board_row + 1][token_to_move.board_col].west = False

                # remove that tile as a search tile
                board.board[token_to_move.board_row][token_to_move.board_col].set_tile_type('')
        
        if (direction == 'West') and (token_to_move.color == color):
            if board.can_place_card(token_to_move.board_col - 2, token_to_move.board_row - 4):
                # place tile
                board.place_card(randomCard, 'West', token_to_move.board_col - 2, token_to_move.board_row - 4)

                # remove walls from the tile
                board.board[token_to_move.board_row][token_to_move.board_col].west = False
                board.board[token_to_move.board_row - 1][token_to_move.board_col].east = False

                # remove that tile as a search tile
                board.board[token_to_move.board_row][token_to_move.board_col].set_tile_type('')


        return board


    def special(self, player_trying_to_move, all_tokens, board):
        # print('special')
        token_to_move = player_trying_to_move.current_token

        # we need to detect if we are on a search space, a vortex, or standing next to a door.
        current_tile_type = board.board[token_to_move.board_row][token_to_move.board_col].tile_type
        if current_tile_type:
            if 'search' in current_tile_type:
                if 'search' in player_trying_to_move.actions:
                    board = self.spawnNewTile(current_tile_type, token_to_move, board)
                    print('search')
            elif 'vortex' in current_tile_type:
                print('vortex')
        
        return board



    def movingIntoWall(self, action, token_to_move, board):
        print('North:', board.board[token_to_move.board_row][token_to_move.board_col].north)
        print('West:', board.board[token_to_move.board_row][token_to_move.board_col].west)
        print('East:', board.board[token_to_move.board_row][token_to_move.board_col].east)
        print('South', board.board[token_to_move.board_row][token_to_move.board_col].south)
        if action == 'up':
            if board.board[token_to_move.board_row][token_to_move.board_col].north == True:
                return True
        if action == 'down':
            if board.board[token_to_move.board_row][token_to_move.board_col].south == True:
                return True
            
        if action == 'left':
            if board.board[token_to_move.board_row][token_to_move.board_col].west == True:
                return True
            
        if action == 'right':
            if board.board[token_to_move.board_row][token_to_move.board_col].east == True:
                return True
        
        return False


    def tokenCanMove(self, action, player_trying_to_move, all_tokens, board):
        token_to_move = player_trying_to_move.current_token

        if self.movingIntoWall(action, token_to_move, board):
            return False

        if action == 'up':
            # remember that row and col are flipped oooof
            # check to see if you are on the edge of the board
            if token_to_move.board_col == 0:
                return False
            else:
                # check to see if you are going to run into another player
                for token in all_tokens:
                    if token.board_col == token_to_move.board_col - 1 and token.board_row == token_to_move.board_row:
                        return False
        if action == 'down':
            if token_to_move.board_col == GRID_SIZE - 1:
                return False
            else:
                # check to see if you are going to run into another player
                for token in all_tokens:
                    if token.board_col == token_to_move.board_col + 1 and token.board_row == token_to_move.board_row:
                        return False
                    

        if action == 'left':
            # check to see if you are on the edge of the board
            if token_to_move.board_row == 0:
                return False
            else:
                # check to see if you are going to run into another player
                for token in all_tokens:
                    if token.board_row == token_to_move.board_row - 1 and token.board_col == token_to_move.board_col:
                        return False
                    
        if action == 'right':
            # check to see if you are on the edge of the board
            if token_to_move.board_row == GRID_SIZE - 1:
                return False
            else:
                # check to see if you are going to run into another player
                for token in all_tokens:
                    if token.board_row == token_to_move.board_row + 1 and token.board_col == token_to_move.board_col:
                        return False
            

        if action in player_trying_to_move.actions:
            return True
        else:
            return False
        




    def move(self, action, player_trying_to_move, all_tokens, board):

        if self.tokenCanMove(action, player_trying_to_move, all_tokens, board):
            if action == 'right':
                self.board_row += 1
            if action == 'left':
                self.board_row -= 1
            if action == 'up':
                self.board_col -= 1
            if action == 'down':
                self.board_col += 1
        else:
            # the player cannot move in that direction, play a sound or add animation or something
            print('you cant move that way.')