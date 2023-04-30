import pyxel
import random

# CONTROLS:

PLAYER_1_RIGHT = pyxel.KEY_RIGHT
PLAYER_1_LEFT = pyxel.KEY_LEFT
PLAYER_1_UP = pyxel.KEY_UP
PLAYER_1_DOWN = pyxel.KEY_DOWN
PLAYER_1_SWITCH = pyxel.KEY_LCTRL

PLAYER_2_RIGHT = pyxel.KEY_G
PLAYER_2_LEFT = pyxel.KEY_D
PLAYER_2_UP = pyxel.KEY_R
PLAYER_2_DOWN = pyxel.KEY_F
PLAYER_2_SWITCH = pyxel.KEY_A
PLAYER_2_SPECIAL = pyxel.KEY_S

PLAYER_3_RIGHT = pyxel.KEY_J
PLAYER_3_LEFT = pyxel.KEY_G
PLAYER_3_UP = pyxel.KEY_Y
PLAYER_3_DOWN = pyxel.KEY_H
PLAYER_3_SWITCH = pyxel.KEY_V
PLAYER_3_SPECIAL = pyxel.KEY_C


PLAYER_4_RIGHT = pyxel.KEY_SEMICOLON
PLAYER_4_LEFT = pyxel.KEY_K
PLAYER_4_UP = pyxel.KEY_O
PLAYER_4_DOWN = pyxel.KEY_L
PLAYER_4_SWITCH = pyxel.KEY_M
PLAYER_4_SPECIAL = pyxel.KEY_N


class Player():
    def __init__(self,color, playerTokens):
        self.playerTokens = playerTokens
        self.color = color
        self.current_player_token_index = 0
        self.current_token = self.playerTokens[self.current_player_token_index]
        self.x = self.current_token.x
        self.y = self.current_token.y

    # switch to the next token in the list. If we are on the last token, switch to the first token
    def switch_token(self):
        self.current_token.deselect_token(self) # added
        self.current_player_token_index += 1
        if self.current_player_token_index >= len(self.playerTokens):
            self.current_player_token_index = 0
        self.current_token = self.playerTokens[self.current_player_token_index]
        self.current_token.select_token(self) # added
        self.x = self.current_token.x
        self.y = self.current_token.y
    


class PlayerToken():
    def __init__(self, color, buttons=[]):
        self.x = 2
        self.y = 2
        self.color = color # '10: yellow', '9: orange', '2: purple', '11: green'
        self.size = 6
        self.all_buttons = buttons
        self.players_with_token_selected = []
    
    def draw(self):
        pyxel.rect(self.x + 1, self.y + 1, self.size, self.size, self.color)

        # pyxel.rectb(self.x, self.y, 8, 8, self.color
        for player in self.players_with_token_selected:
            if player.color == 3:
                pyxel.blt(self.x, self.y, 1, 0, 0, 8, 8, 0)
            if player.color == 13:
                pyxel.blt(self.x, self.y, 1, 8, 0, 8, 8, 0)
            if player.color == 14:
                pyxel.blt(self.x, self.y, 1, 16, 0, 8, 8, 0)

    def select_token(self, player):
        self.players_with_token_selected.append(player)

    def deselect_token(self, player):
        self.players_with_token_selected.remove(player)

    def move(self, action, number):
        if action == 'right':
            self.x += number
        if action == 'left':
            self.x -= number
        if action == 'up':
            self.y -= number
        if action == 'down':
            self.y += number




class App:
    def __init__(self):
        pyxel.init(500, 500)
        pyxel.load("./newspace.pyxres")
        self.x = 0
        self.pt1 = PlayerToken(10)
        self.pt2 = PlayerToken(9)
        self.pt3 = PlayerToken(2)
        self.pt4 = PlayerToken(1)
        self.player1 = Player(3, [self.pt1, self.pt2, self.pt3, self.pt4])
        self.player2 = Player(13, [self.pt1, self.pt2, self.pt3, self.pt4])
        self.player3 = Player(14, [self.pt1, self.pt2, self.pt3, self.pt4])

        self.pt1.select_token(self.player1)
        self.pt1.select_token(self.player2)
        self.pt1.select_token(self.player3)


        pyxel.run(self.update, self.draw)

    def update(self):
        # Player 1 movement
        if pyxel.btnp(PLAYER_1_LEFT):
            self.player1.current_token.move('left', 8)
        if pyxel.btnp(PLAYER_1_RIGHT):
            self.player1.current_token.move('right', 8)
        if pyxel.btnp(PLAYER_1_UP):
            self.player1.current_token.move('up', 8)
        if pyxel.btnp(PLAYER_1_DOWN):
            self.player1.current_token.move('down', 8)
        if pyxel.btnp(PLAYER_1_SWITCH):
            self.player1.switch_token()

        if pyxel.btnp(PLAYER_2_LEFT):
            self.player2.current_token.move('left', 8)
        if pyxel.btnp(PLAYER_2_RIGHT):
            self.player2.current_token.move('right', 8)
        if pyxel.btnp(PLAYER_2_UP):
            self.player2.current_token.move('up', 8)
        if pyxel.btnp(PLAYER_2_DOWN):
            self.player2.current_token.move('down', 8)
        if pyxel.btnp(PLAYER_2_SWITCH):
            self.player2.switch_token()
    
        if pyxel.btnp(PLAYER_3_LEFT):
            self.player3.current_token.move('left', 8)
        if pyxel.btnp(PLAYER_3_RIGHT):
            self.player3.current_token.move('right', 8)
        if pyxel.btnp(PLAYER_3_UP):
            self.player3.current_token.move('up', 8)
        if pyxel.btnp(PLAYER_3_DOWN):
            self.player3.current_token.move('down', 8)
        if pyxel.btnp(PLAYER_3_SWITCH):
            self.player3.switch_token()


    def draw(self):
        pyxel.cls(0)
        self.pt1.draw()
        self.pt2.draw()
        self.pt3.draw()
        self.pt4.draw()

App()
