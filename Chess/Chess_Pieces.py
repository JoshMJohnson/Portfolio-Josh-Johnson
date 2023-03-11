'''
Holds the point values of all the chess pieces in the game of chess
'''

'''
Class for the chess piece 'Pawn'
'''
class Pawn:
    def __init__(self):
        self.point_value = 1 # point value of piece
        self.starting_amount = 8 # number of starting pieces on the board

'''
Class for the chess piece 'Bishop'
'''
class Bishop:
    def __init__(self):
        self.point_value = 3 # point value of piece
        self.starting_amount = 2 # number of starting pieces on the board

'''
Class for the chess piece 'Knight'
'''
class Knight:
    def __init__(self):
        self.point_value = 3 # point value of piece
        self.starting_amount = 2 # number of starting pieces on the board

'''
Class for the chess piece 'Rook'
'''
class Rook:
    def __init__(self):
        self.point_value = 5 # point value of piece
        self.starting_amount = 2 # number of starting pieces on the board

'''
Class for the chess piece 'Queen'
'''
class Queen:
    def __init__(self):
        self.point_value = 9 # point value of piece
        self.starting_amount = 1 # number of starting pieces on the board

'''
Class for the chess piece 'King'
'''
class King:
    def __init__(self, white_player):
        self.in_check = False
        self.has_moved = False

        # contains the current position of the king (row, column)
        if white_player: # white player
            self.current_position = (7, 4)
        else: # black player
            self.current_position = (0, 4)