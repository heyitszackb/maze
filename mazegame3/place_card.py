from Card import Card

# Ex. place_tile("1a", "north", 0, 0)
# x and y will be the top left corner of the card and it will be between
# 0 and GRID_SIZE - 1 (0,25),(0,25)
def place_card(board,tile_name, dir,x,y):
    card = Card(tile_name,dir,x,y)
    # TODO this
    return board
