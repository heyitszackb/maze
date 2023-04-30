from constants import TILE_SIZE, GRID_SIZE, HEADER_SIZE, PANNEL_SIZE
import pyxel

class CaptureSquare:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.red = False
        self.yellow = False
        self.green = False
        self.blue = False


    def draw(self):
    # main rect
        pyxel.rectb(self.x * TILE_SIZE, self.y * TILE_SIZE, 8 * TILE_SIZE, 2 * TILE_SIZE, 5)

        # sub rects
        sub_width = int(8 * TILE_SIZE / 4)  # width of each sub-rectangle
        sub_height = 2 * TILE_SIZE  # height of each sub-rectangle

        # red, yellow, green, blue
        colors = [8,9,3,5]

        # draw sub-rectangles
        x0 = self.x * TILE_SIZE
        y0 = self.y * TILE_SIZE
        pyxel.rectb(x0, y0, sub_width, sub_height, colors[0])
        pyxel.rectb(x0 + sub_width, y0, sub_width, sub_height, colors[1])
        pyxel.rectb(x0 + 2*sub_width, y0, sub_width, sub_height, colors[2])
        pyxel.rectb(x0 + 3*sub_width, y0, sub_width, sub_height, colors[3])

        if self.red:
            pyxel.rect(x0, y0, sub_width, sub_height, colors[0])
        if self.yellow:
            pyxel.rect(x0 + sub_width, y0, sub_width, sub_height, colors[1])
        if self.green:
            pyxel.rect(x0 + 2*sub_width, y0, sub_width, sub_height, colors[2])
        if self.blue:
            pyxel.rect(x0 + 3*sub_width, y0, sub_width, sub_height, colors[3])




        
