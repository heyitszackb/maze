import pyxel



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.is_alive = True

    def update(self):
        # self.update_player_walls()
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.move_left()
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.x += 8
        if pyxel.btnp(pyxel.KEY_UP):
            self.y -= 8
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.y += 8

    def update_player_walls(self):
        pass


    def draw(self):
        pyxel.rect(self.x + 2, self.y + 2, self.w, self.h, 9)
    
    def move_left(self):
        self.x -= 8

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("newspace.pyxres")

        self.p = Player(0, 0)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.p.update()

    def draw(self):
        # pyxel.cls(0)
        # pyxel.text(0, 0, "Hello, Pyxel!", 7)
        #         (x, y, m, u, v, w, h, [colkey])
        pyxel.bltm(0, 0, 0, 0, 0, 40, 40)
        self.p.draw()
        # pyxel.rect(self.x, 0, 8, 8, 9)

App()



individual = []