'''
Keeps a log of the moves made by the player and performs such action
'''
class Moves():
    # map dictionaries cooresponding a chess board tile representation with an array representation
    # file = column and rank = row on a chess board
    ranks_to_rows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0} # cooresponds chess board rows with coding indices
    rows_to_ranks = {x : y for y, x in ranks_to_rows.items()} # swaps the keys with the values of those keys
    files_to_cols = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7} # cooresponds chess board columbs with coding indices
    cols_to_files = {x : y for y, x in files_to_cols.items()} # swaps the keys with the values of those keys

    '''
    constructor for the Moves class
    '''
    def __init__(self, starting_tile, ending_tile, board):
        # starting and ending coordinates of the piece being moved
        self.start_row = starting_tile[0]
        self.start_col = starting_tile[1]
        self.end_row = ending_tile[0]
        self.end_col = ending_tile[1]

        # starting and ending index locations within the board array
        self.starting_piece = board[self.start_row][self.start_col]
        self.ending_piece = board[self.end_row][self.end_col]
        
        # unique move ID
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col

    '''
    override the equals method
    '''
    def __eq__(self, other):
        if isinstance(other, Moves):
            return self.move_id == other.move_id
        
        return False

    '''
    returns the chess notation of a potential move
    '''
    def get_chess_notation(self): # TODO proper chess notation has first letter of piece in front of notation
        return self.get_rank_file_pair(self.start_row, self.start_col) + " -> " + self.get_rank_file_pair(self.end_row, self.end_col)

    '''
    returns the chess notation of a tile on the game board
    '''
    def get_rank_file_pair(self, row, col):
        return self.cols_to_files[col] + self.rows_to_ranks[row]