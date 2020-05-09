from enum import Enum, auto


WINDOW_SIZE = 600
BOARD_SIZE  = 400


class Player(Enum):
    EMPTY = 0
    HUMAN = 1
    COMPUTER = 2


class Position:
    def __init__(self, pos, radius=None, player=None):
        self.pos = pos
        self.radius = radius
        self.player = player
        self.x = pos[0]
        self.y = pos[1]

    def translate_from_origin(self):
        # Position from the center of the board
        center = WINDOW_SIZE / 2
        
        # Translate from px to mm
        # TODO: This only works for tictactoe scaling
        scale = 105 / BOARD_SIZE

        x, y = (self.pos - center)
        return x*scale, y*scale
