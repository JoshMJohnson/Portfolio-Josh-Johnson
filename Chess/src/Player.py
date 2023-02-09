'''
Instance for Player One

Game Time Rules:
In the case of chess, the World Chess Federation FIDE has a single, 
classical time control for most of its major events, 90 minutes for 
the first 40 moves, followed by 30 minutes for the rest of the game, 
with an addition of 30 seconds per move starting from move one.
'''

import time # time access and conversions

class Player:
    # player state
    color = -1
    points_remaining = -1
    points_taken = -1
    num_moves_made = -1
    time_remaining = -1

    # constructor
    def __init__(self, player):
        # color that the player controls
        if player == 1:
            self.color = 'white'
        else:
            self.color = 'black'

        # points remaining for player
        self.points_remaining = self.starting_points_calculator()

        # points taken from other player
        self.points_taken = 0
        
        # number of moves made
        self.num_moves_made = 0

        # time remaining for player before forfeit due to delay
        mins, secs = divmod(90, 60)
        self.time_remaining = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)

    def starting_points_calculator(self):
        # piece point values
        pawn_value = 1
        bishop_value = 3
        knight_value = 3
        rook_value = 5
        queen_value = 9

        # num of each piece
        num_pawns = 8
        num_bishops = 2
        num_knights = 2
        num_rooks = 2
        num_queens = 1

        # point calculations
        return ((num_pawns * pawn_value) 
                    + (num_bishops * bishop_value) 
                    + (num_knights * knight_value) 
                    + (num_rooks * rook_value) 
                    + (num_queens * queen_value))

    # getter function for the player color variable
    def player_color(self):
        return self.color
    
    # getter function for the points remaining for player
    def player_points_remaining(self):
        return self.points_remaining

    # getter function for the points player has taken from opponent
    def player_points_taken(self):
        return self.points_taken

    # getter function for the number of moves player has made so far
    def player_moves_made(self):
        return self.num_moves_made

    # getter function for time remaining for player
    def player_time_remaining(self):
        return self.time_remaining


# ! testing purposes below
obj = Player(1)
print('color: ' + obj.player_color())
print('points_remaining: ' + str(obj.player_points_remaining()))
print('points_taken: ' + str(obj.player_points_taken()))
print('num_moves_made: ' + str(obj.player_moves_made()))
print('time_remaining: ' + str(obj.player_time_remaining()))