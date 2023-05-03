from constants import CARD_FILE_NAME, TILE_SIZE, GRID_SIZE, HEADER_SIZE, CARD_SIZE
from Tile import Tile
from get_card_from_file import get_card_from_file

class Card:
    def __init__(self, card_name, direction,x,y):
        self.card_name = card_name
        self.direction = direction
        self.tiles = []
        self.x = x
        self.y = y
        # self.card_data = get_card_from_file(card_name, CARD_FILE_NAME)

    def generate_tiles(self):
        for i in range(CARD_SIZE):
            row = []
            for j in range(CARD_SIZE):
                row.append(Tile(i + self.x, j + self.y, 'red_vortex'))
            self.tiles.append(row)
    
    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw()

# TODO: Drawing is weird, need to figure out how I want to draw the tiles and if the tile should be resppnsible for knowing it's x and y location. I don't think it actually should.
# I think the tile should be drawn way outside whenever we draw the board, and we draw the tile at the correct location then.
# That way, when we place_card, all that method does is take the board and the card and replace the boad with the correct tiles.
# yes, this is good. zcb

# c = Card('1a', 'North', 0, 0)
        # more complicated logic goes here
        # for i,row in enumerate(self.card_data):
            # row = []
        #     for j,tile in enumerate(row):
        #         if tile[0] == '-':
        #             continue
        #         else:
        #             if (j < len(row) - 1) and (row[j+1][0] == '-'):
        #                 tile = tile + row[j+1]for i,row in enumerate(self.card_data):

    