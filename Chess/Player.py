'''
Instance class for players in the game
---------------------------------------
Game Time Rules:

Time controls are displayed in an "X|Y" format 
    - The first number refers to the number of minutes each player has on game start
    - The second number refers to the seconds of increment per move 
        - Increment is how many seconds are added to the clock for each move that is played. 

For example, a 3|0 time control refers to a game where each player receives three minutes to 
complete the game with no increment per move, while a 5|5 time control refers to a game where 
each player receives five minutes and gains five seconds per move for the increment.
'''

import time # time access and conversions

'''
contains an instance of a player
'''
class Player:
    '''
    constructor for the Player class
    '''
    def __init__(self, player):
        # color that the player controls
        if player == 1:
            self.color = 'white'
            self.current_player = True
        else:
            self.color = 'black'
            self.current_player = False

        self.player_lost = False

        # points remaining for player
        self.points_remaining = self.starting_points_calculator()

        # points taken from other player
        self.points_taken = 0
        
        # number of moves made
        self.num_moves_made = 0

        # time remaining for player before forfeit due to delay
        self.mins_remaining = 5
        self.secs_remaining = 0
        mins, secs = divmod(self.mins_remaining * 60, 60)
        self.time_remaining = '{:01d}:{:02d}'.format(mins, secs)
        
    '''
    calculates the total amount of points a player has at the start of the game
    '''
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

    '''
    continues the player timer
    '''
    def continue_timer():
        time.sleep(1)

    '''
    pauses the player timer
    '''
    def pause_timer(self):
        pass

    '''
    checks if player ran out of time on the clock
    '''
    def is_player_out_of_time(self):
        pass