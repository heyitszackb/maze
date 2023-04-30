import pyxel
from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, CARD_FILE_NAME
from mappings import player_number_mappings



class Player:
    def __init__(self, pane_x, pane_y, w, h, color, player_name, playerTokens = []):
        self.player_name = player_name #p1, p2, p3, p4
        self.pane_x = pane_x
        self.pane_y = pane_y
        self.width = w
        self.height = h
        self.color = color # yellow, green, blue, red
        self.actions = []

        self.playerTokens = playerTokens
        self.color = color
        self.current_player_token_index = 0
        self.current_token = self.playerTokens[self.current_player_token_index]
        self.cursor_x = self.current_token.board_row
        self.cursor_y = self.current_token.board_col

        self.playerTokens = playerTokens

    def set_actions(self, actions):
        self.actions = actions
    

        # switch to the next token in the list. If we are on the last token, switch to the first token
    def switch_token(self):
        pyxel.play(2, 2)
        self.current_token.deselect_token(self) # added
        self.current_player_token_index += 1
        if self.current_player_token_index >= len(self.playerTokens):
            self.current_player_token_index = 0
        self.current_token = self.playerTokens[self.current_player_token_index]
        self.current_token.select_token(self) # added
        self.cursor_x = self.current_token.board_row
        self.cursor_y = self.current_token.board_col
    

    def get_actions(self):
        return self.actions

    def draw_player_controls(self):

        X_OFFSET = (self.width // TILE_SIZE) // 2
        Y_OFFSET = (self.height // TILE_SIZE) // 2

        color_mappings = {
            'red': 1,
            'green': 2,
            'blue': 3,
            'yellow': 4
        }
        # ACTIONS = ['up','down', 'left', 'right', 'vortex', 'search', 'key' ]
        # if you have the action, you should draw it in the color that you are
        # if you don't have the action, you should draw it in black

        up_arrow_color = color_mappings[self.color]
        left_arrow_color = color_mappings[self.color]
        right_arrow_color = color_mappings[self.color]
        down_arrow_color = color_mappings[self.color]
        vortex_color = color_mappings[self.color]
        key_color = color_mappings[self.color]
        search_color = color_mappings[self.color] 

        if 'up' not in self.actions:
            up_arrow_color = 0
        if 'left' not in self.actions:
            left_arrow_color = 0
        if 'right' not in self.actions:
            right_arrow_color = 0
        if 'down' not in self.actions:
            down_arrow_color = 0
        if 'vortex' not in self.actions:
            vortex_color = 0
        if 'key' not in self.actions:
            key_color = 0
        if 'search' not in self.actions:
            search_color = 0

        # up arrow
        pyxel.blt(self.pane_x + (TILE_SIZE * (-1 + X_OFFSET)), self.pane_y + (TILE_SIZE * (-2 + Y_OFFSET)), 2, 1*0*(TILE_SIZE), TILE_SIZE*up_arrow_color*2, TILE_SIZE*2, TILE_SIZE*2)

        # left arrow
        pyxel.blt(self.pane_x + (TILE_SIZE * (-3 + X_OFFSET)), self.pane_y + (TILE_SIZE * (0 + Y_OFFSET)), 2, 1*2*(TILE_SIZE), TILE_SIZE*left_arrow_color*2, TILE_SIZE*2, TILE_SIZE*2)

        # right arrow   
        pyxel.blt(self.pane_x + (TILE_SIZE * (1 + X_OFFSET)), self.pane_y + (TILE_SIZE * (0 + Y_OFFSET)), 2, 1*4*(TILE_SIZE), TILE_SIZE*right_arrow_color*2, TILE_SIZE*2, TILE_SIZE*2)

        # down arrow
        pyxel.blt(self.pane_x + (TILE_SIZE * (-1 + X_OFFSET)), self.pane_y + (TILE_SIZE * (2 + Y_OFFSET)), 2, 1*6*(TILE_SIZE), TILE_SIZE*down_arrow_color*2, TILE_SIZE*2, TILE_SIZE*2)

        # vortex
        pyxel.blt(self.pane_x + (TILE_SIZE * (-1 + X_OFFSET)), self.pane_y + (TILE_SIZE * (0 + Y_OFFSET)), 2, 1*8*(TILE_SIZE), TILE_SIZE*vortex_color*2, TILE_SIZE*2, TILE_SIZE*2)

        # key
        pyxel.blt(self.pane_x + (TILE_SIZE * (-4 + X_OFFSET)), self.pane_y + (TILE_SIZE * (3 + Y_OFFSET)), 2, 1*10*(TILE_SIZE), TILE_SIZE*key_color*2, TILE_SIZE*2, TILE_SIZE*2)

        # search
        pyxel.blt(self.pane_x + (TILE_SIZE * (2 + X_OFFSET)), self.pane_y + (TILE_SIZE * (2.7 + Y_OFFSET)), 2, 1*12*(TILE_SIZE), TILE_SIZE*search_color*2, TILE_SIZE*2, TILE_SIZE*2)




    def draw_player_name(self):
        VERTICAL_TEXT_OFFSET = 1
        HORIZONTAL_TEXT_OFFSET = 2
        pyxel.rectb(self.pane_x, self.pane_y, self.width, self.height, 15)
        # draw the word "Player"
        pyxel.blt(self.pane_x + (TILE_SIZE*HORIZONTAL_TEXT_OFFSET),self.pane_y + (TILE_SIZE*VERTICAL_TEXT_OFFSET),1,0,0,TILE_SIZE*6,TILE_SIZE)
        # draw the player number

        tile_x, tile_y = player_number_mappings[self.player_name]

        
        pyxel.blt(self.pane_x + (TILE_SIZE*HORIZONTAL_TEXT_OFFSET + (7 * TILE_SIZE)),self.pane_y + (TILE_SIZE*(VERTICAL_TEXT_OFFSET)),1,tile_x * TILE_SIZE,tile_y * TILE_SIZE,TILE_SIZE,TILE_SIZE)
        

    def draw_pane(self):
        """Handles all logic for drawing the player pane"""
        self.draw_player_name()
        self.draw_player_controls()

    def draw_token(self):
        for token in self.playerTokens:
            token.draw()