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

# python libraries
import time # time access and conversions

# custom classes
import Chess_Pieces

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

        self.player_in_check = False # indicates if player is in check
        self.player_lost = False # indicates if player has lost
        self.player_out_of_time = False # indicates if player ran out of time on the game clock
        self.points_taken = 0 # points taken from other player
        
        # * timer settings
        # default game clock settings
        self.mins_remaining = 20 # mins remaining for the player
        self.seconds_gained_from_move = 0 # seconds gained by player after a move
        mins, secs = divmod(self.mins_remaining * 60, 60)
        self.time_remaining = '{:01d}:{:02d}'.format(mins, secs)

        self.timer_running = False
        self.total_seconds_remaining = 60 * self.mins_remaining

        self.is_window_closed = False
        
    '''
    calculates the total amount of points a player has at the start of the game
    '''
    def starting_points_calculator(self):
        pawn = Chess_Pieces.Pawn()
        bishop = Chess_Pieces.Bishop()
        knight = Chess_Pieces.Knight()
        rook = Chess_Pieces.Rook()
        queen = Chess_Pieces.Queen()

        return ((pawn.starting_amount * pawn.point_value) 
                    + (bishop.starting_amount * bishop.point_value) 
                    + (knight.starting_amount * knight.point_value) 
                    + (rook.starting_amount * rook.point_value) 
                    + (queen.starting_amount * queen.point_value))

    '''
    changes the game clock settings; will reset timer 
    '''
    def change_timer(self, starting_mins, add_secs):
        self.mins_remaining = starting_mins
        self.seconds_gained_from_move = add_secs
        mins, secs = divmod(self.mins_remaining * 60, 60)
        self.time_remaining = '{:01d}:{:02d}'.format(mins, secs)

        self.total_seconds_remaining = 60 * self.mins_remaining

    '''
    manages the game clock timers for each player
    '''
    def game_clock_running_management(self):
        while not self.is_window_closed: # run continuously
            time.sleep(0.5) # prevent over processing
            while self.current_player and self.timer_running: # if current player and timer unpaused
                if self.total_seconds_remaining > 0: # if player is not out of time
                    self.total_seconds_remaining -= 1

                    mins, secs = divmod(self.total_seconds_remaining, 60)
                    self.time_remaining = '{:01d}:{:02d}'.format(mins, secs)
                    time.sleep(1)
                else: # player is out of time
                    self.player_out_of_time = True

    '''
    adds the bonus seconds to the players game clock
    '''
    def add_bonus_seconds(self):
        self.total_seconds_remaining += self.seconds_gained_from_move

        mins, secs = divmod(self.total_seconds_remaining, 60)
        self.time_remaining = '{:01d}:{:02d}'.format(mins, secs)

    '''
    remove the bonus seconds to the players game clock
    '''
    def remove_bonus_seconds(self):
        self.total_seconds_remaining -= self.seconds_gained_from_move

        mins, secs = divmod(self.total_seconds_remaining, 60)
        self.time_remaining = '{:01d}:{:02d}'.format(mins, secs)

    '''
    enables/disables game clocks
    '''
    def toggle_timer(self):
        if self.timer_running:
            self.timer_running = False
        else:
            self.timer_running = True
