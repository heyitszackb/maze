import pyxel
from Tile import Tile
from place_card import place_card
from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, PANNEL_SIZE
from mappings import player_action_mappings, controls
from Board import Board
from Player import Player
from PlayerToken import PlayerToken
from Timer import Timer
from CaptureSquare import CaptureSquare

# size = tile count
# height/width = pixel count

MAIN_WIDTH = (TILE_SIZE * GRID_SIZE) + (PANNEL_SIZE*TILE_SIZE*2)
MAIN_HEIGHT = TILE_SIZE * (GRID_SIZE + HEADER_SIZE)
HEADER_HEIGHT = TILE_SIZE * HEADER_SIZE
HEADER_WIDTH = MAIN_WIDTH
PANEL_WIDTH = TILE_SIZE * PANNEL_SIZE
PANNEL_HEIGHT = (GRID_SIZE * TILE_SIZE)
GRID_HEIGHT = TILE_SIZE * GRID_SIZE
GRID_WIDTH = TILE_SIZE * GRID_SIZE

# a player token is the itme on the board, a player is a human

# In initPlayers, add the player tokens.
# continue to copy relevant code from players.py to get the tokens moving on the screen.

class Game:
    def __init__(self):
        self.main_width = MAIN_WIDTH
        self.main_height = MAIN_HEIGHT
        self.header_height = HEADER_HEIGHT
        self.header_width = HEADER_WIDTH
        self.panel_width = PANEL_WIDTH
        self.panel_height = PANNEL_HEIGHT
        self.grid_height = GRID_HEIGHT
        self.grid_width = GRID_WIDTH
        self.players = []
        self.board = Board()
        self.player_tokens = []
        self.timer = Timer()
        self.redPressed = False
        self.bluePressed = False
        self.greenPressed = False
        self.yellowPressed = False
        self.capture_sqaure = CaptureSquare()


        self.level = 1
        print((GRID_SIZE//2 - 2))
        if self.board.can_place_card((GRID_SIZE//2 - 2), (GRID_SIZE//2 - 2)):
            self.board.place_card('1a', 'North', 11, 11)

    def update_frame(self):
        self.timer.decrease_time_left()
    
    def draw_header(self):
        """Handles drawing the header in the game"""
        pyxel.rectb(0,0,MAIN_WIDTH, HEADER_HEIGHT, 13)
        self.timer.draw()
        self.capture_sqaure.draw()

    def draw_players(self):

        # player panes
        for i in range(len(self.players)):
            self.players[i].draw_pane()

        # player tokens
        for i in range(len(self.players)):
            self.players[i].draw_token()



    def draw_board(self):
        self.board.draw()

    def shift_actions(self):
        """Shifts the actions in a circle between the players"""
        if len(self.players) == 2:
            self.players[0].actions, self.players[1].actions = self.players[1].actions, self.players[0].actions
        elif len(self.players) == 3:
            self.players[0].actions, self.players[1].actions, self.players[2].actions = self.players[2].actions, self.players[0].actions, self.players[1].actions
        elif len(self.players) == 4:
            self.players[0].actions, self.players[1].actions, self.players[2].actions, self.players[3].actions = self.players[3].actions, self.players[0].actions, self.players[1].actions, self.players[2].actions


    def detect_inputs(self):
        # Player 1 movement

        # action, player_trying_to_move, token_to_move, all_tokens):
        if pyxel.btnp(controls[1]['left']):
            self.players[0].current_token.move('left', self.players[0], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[1]['right']):
            self.players[0].current_token.move('right', self.players[0], self.player_tokens, self.board, self.timer ,self)
        if pyxel.btnp(controls[1]['up']):
            self.players[0].current_token.move('up', self.players[0], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[1]['down']):
            self.players[0].current_token.move('down', self.players[0], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[1]['switch']):
            self.players[0].switch_token()
        if pyxel.btnp(controls[1]['special']):
            self.board = self.players[0].current_token.special(self.players[0], self.player_tokens, self.board)

        # Player 2 movement
        if pyxel.btnp(controls[2]['left']):
            self.players[1].current_token.move('left', self.players[1], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[2]['right']):
            self.players[1].current_token.move('right', self.players[1], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[2]['up']):
            self.players[1].current_token.move('up', self.players[1], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[2]['down']):
            self.players[1].current_token.move('down', self.players[1], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[2]['switch']):
            self.players[1].switch_token()
        if pyxel.btnp(controls[2]['special']):
            self.board = self.players[1].current_token.special(self.players[1], self.player_tokens, self.board)

        # Player 3 movement
        if pyxel.btnp(controls[3]['left']):
            self.players[2].current_token.move('left', self.players[2], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[3]['right']):
            self.players[2].current_token.move('right', self.players[2], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[3]['up']):
            self.players[2].current_token.move('up', self.players[2], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[3]['down']):
            self.players[2].current_token.move('down', self.players[2], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[3]['switch']):
            self.players[2].switch_token()
        if pyxel.btnp(controls[3]['special']):
            self.board = self.players[2].current_token.special(self.players[2], self.player_tokens, self.board, self)

        # Player 4 movement
        if pyxel.btnp(controls[4]['left']):
            self.players[3].current_token.move('left', self.players[3], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[4]['right']):
            self.players[3].current_token.move('right', self.players[3], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[4]['up']):
            self.players[3].current_token.move('up', self.players[3], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[4]['down']):
            self.players[3].current_token.move('down', self.players[3], self.player_tokens, self.board, self.timer, self)
        if pyxel.btnp(controls[4]['switch']):
            self.players[3].switch_token()
        if pyxel.btnp(controls[4]['special']):
            self.board = self.players[3].current_token.special(self.players[3], self.player_tokens, self.board)
            

    def initPlayers(self, numPlayers):
        self.players = []
        colors = ['red', 'green', 'blue', 'yellow']
        playerNames = ['p1', 'p2', 'p3', 'p4']

        startingPositionOffset = (GRID_SIZE // 2) - 1
        startingPositions = [[0,0], [0,1], [1,0], [1,1]]


        panelWidth = PANEL_WIDTH
        panelHeight = (MAIN_HEIGHT - HEADER_HEIGHT) // 2


        # hard coded for 4 players -  LATER


        for i in range(4):
            self.player_tokens.append(PlayerToken(colors[i], startingPositionOffset + startingPositions[i][0], startingPositionOffset + startingPositions[i][1]))
            self.board.board[startingPositionOffset + startingPositions[i][0]][startingPositionOffset + startingPositions[i][1]].token = self.player_tokens[i]

    




        # Create players in the appropriate positions
        player1 = Player(0, HEADER_HEIGHT, panelWidth, panelHeight, colors[0], playerNames[0],self.player_tokens)
        player2 = Player(MAIN_WIDTH - panelWidth, HEADER_HEIGHT, panelWidth, panelHeight, colors[1], playerNames[1],self.player_tokens)
        player3 = Player(0, HEADER_HEIGHT + panelHeight, panelWidth, panelHeight, colors[2], playerNames[2],self.player_tokens)
        player4 = Player(MAIN_WIDTH - panelWidth, HEADER_HEIGHT + panelHeight, panelWidth, panelHeight, colors[3], playerNames[3], self.player_tokens)

        self.players.append(player1)

        if numPlayers >= 2:
            self.players.append(player2)
        if numPlayers >= 3:
            self.players.append(player3)
        if numPlayers == 4:
            self.players.append(player4)




        for i in range(len(self.players)):
            self.player_tokens[0].select_token(self.players[i])


        
        actions = player_action_mappings[numPlayers]
        for i in range(len(self.players)):
            self.players[i].set_actions(actions[i])
        

        # put the players in the board



        # Player tokens


    