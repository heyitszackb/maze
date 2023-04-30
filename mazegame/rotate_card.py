import numpy as np
def rotate_card(card, dir):
    card_array = np.array(card)
    if dir == 'West':
        rotated_array = np.rot90(card_array, k=1)
    elif dir == 'South':
        rotated_array = np.rot90(card_array, k=2)
    elif dir == 'East':
        rotated_array = np.rot90(card_array, k=3)
    else:
        rotated_array = card_array

    rotated_card = rotated_array.tolist()
    rotated_card = [[str(element) for element in row] for row in rotated_card]
    
    return rotated_card