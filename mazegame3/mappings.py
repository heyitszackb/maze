import pyxel

color_tile_mappings = {
    # vortex
    'green_vortex': (0,4),
    'blue_vortex': (1,4),
    'yellow_vortex': (2,4),
    'red_vortex': (3,4),

    # capture
    'green_capture': (0,5),
    'blue_capture': (1,5),
    'yellow_capture': (2,5),
    'red_capture': (3,5),

    # exit
    'green_exit': (0,6),
    'blue_exit': (1,6),
    'yellow_exit': (2,6),
    'red_exit': (3,6),

    # search north
    'green_search_north': (0,7),
    'blue_search_north': (1,7),
    'yellow_search_north': (2,7),
    'red_search_north': (3,7),

    # search west
    'green_search_west': (0,8),
    'blue_search_west': (1,8),
    'yellow_search_west': (2,8),
    'red_search_west': (3,8),

    # search south
    'green_search_south': (0,9),
    'blue_search_south': (1,9),
    'yellow_search_south': (2,9),
    'red_search_south': (3,9),

    # search east
    'green_search_east': (0,10),
    'blue_search_east': (1,10),
    'yellow_search_east': (2,10),
    'red_search_east': (3,10),

    # timer
    'timer': (0,11),

    # mage ball
    'mage_ball': (1,11),

    # security camera
    'security_camera': (2,11),
}

player_action_mappings = {
    2: [['key','search','down','left'],['vortex','up','right']],
    3: [['vortex','left'],['key','down','search'],['up','right']],
    4: [['key','right'],['vortex','left'],['search','down'],['up']],
}

ACTIONS = ['up','down', 'left', 'right', 'vortex', 'search', 'key' ]

player_number_mappings = {
    'p1': (0,1),
    'p2': (1,1),
    'p3': (2,1),
    'p4': (3,1),
}


door_mappings = {
    # door
    (False, False, False, False): (0,0),
    (True, False, False, False): (3,14),
    (False, True, False, False): (1,14),
    (False, False, False, True): (0,14),
    (False, False, True, False): (2,14),
}

level_mappings = {
    # level -> cards in level
    1: ['2','3','4','5','6','7','8','9','10','11','12'],
    2: ['2','3','4','5','6','7','8','9','10','11','12','13','14'], # speaking on green squares
    3: ['2','3','4','5','6','7','8','9','10','11','12','13','14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'], # speaking on green squares
}

base_tile_mappings = {
    #North, West, South, East
    (False, False, False, False): (0,0),
    (False, False, False, True): (1,0),
    (False, False, True, False): (2,0),
    (False, False, True, True): (3,0),
    (False, True, False, False): (0,1),
    (False, True, False, True): (1,1),
    (False, True, True, False): (2,1),
    (False, True, True, True): (3,1),
    (True, False, False, False): (0,2),
    (True, False, False, True): (1,2),
    (True, False, True, False): (2,2),
    (True, False, True, True): (3,2),
    (True, True, False, False): (0,3),
    (True, True, False, True): (1,3),
    (True, True, True, False): (2,3),
    (True, True, True, True): (3,3),
}

# Dictionary of controls for each player

controls = {
    2: {
        'right': pyxel.KEY_QUOTE,
        'left': pyxel.KEY_L,
        'up': pyxel.KEY_P,
        'down': pyxel.KEY_SEMICOLON,
        'switch': pyxel.KEY_COMMA,
        'special': pyxel.KEY_M
    },
    1: {
        'right': pyxel.KEY_D,
        'left': pyxel.KEY_A,
        'up': pyxel.KEY_W,
        'down': pyxel.KEY_S,
        'switch': pyxel.KEY_C,
        'special': pyxel.KEY_V
    },
    3: {
        'right': pyxel.KEY_1,
        'left': pyxel.KEY_1,
        'up': pyxel.KEY_1,
        'down': pyxel.KEY_1,
        'switch': pyxel.KEY_1,
        'special': pyxel.KEY_1
    },
    
    # Player 4 controls (right on keyboard)
    4: {
        'right': pyxel.KEY_1,
        'left': pyxel.KEY_1,
        'up': pyxel.KEY_1,
        'down': pyxel.KEY_1,
        'switch': pyxel.KEY_1,
        'special': pyxel.KEY_1
    }

    
    # # Player 1 controls (left on gamepad)
    # 1: {
    #     'right': pyxel.KEY_RIGHT,
    #     'left': pyxel.KEY_LEFT,
    #     'up': pyxel.KEY_UP,
    #     'down': pyxel.KEY_DOWN,
    #     'switch': pyxel.KEY_LCTRL,
    #     'special': pyxel.KEY_LALT
    # },
    
    # # Player 2 controls (right on gamepad)
    # 2: {
    #     'right': pyxel.KEY_G,
    #     'left': pyxel.KEY_D,
    #     'up': pyxel.KEY_R,
    #     'down': pyxel.KEY_F,
    #     'switch': pyxel.KEY_A,
    #     'special': pyxel.KEY_S
    # },
    
    # # NOTE: Player 3 and 4 should be on different keyboards!
    
    # Player 3 controls (left on keyboard)
    # 3: {
    #     'right': pyxel.KEY_K,
    #     'left': pyxel.KEY_H,
    #     'up': pyxel.KEY_U,
    #     'down': pyxel.KEY_J,
    #     'switch': pyxel.KEY_B,
    #     'special': pyxel.KEY_V
    # },
    
    # # Player 4 controls (right on keyboard)
    # 4: {
    #     'right': pyxel.KEY_QUOTE,
    #     'left': pyxel.KEY_L,
    #     'up': pyxel.KEY_P,
    #     'down': pyxel.KEY_SEMICOLON,
    #     'switch': pyxel.KEY_COMMA,
    #     'special': pyxel.KEY_M
    # }
}


playerCursors = {
    'p1': (0,15),
    'p2': (1,15),
    'p3': (2,15),
    'p4': (3,15),
}

playerTokens = {
    'green': (4,15),
    'red': (5,15),
    'yellow': (6,15),
    'blue': (7,15),
}