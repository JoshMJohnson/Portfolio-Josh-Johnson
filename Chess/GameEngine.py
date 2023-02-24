'''
Keeps track of the board state and determains valid moves

Keeps a move log for the game
'''

# custom classes
import Chess_Pieces

class GameState():
    '''
    constructor for the class GameState
    '''
    def __init__(self):
        self.move_log = []

        # initialized board so white is on bottom and black pieces are on top
        # "--" indicates an open space
        self.board = [
            ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook"],
            ["black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn"],
            ["white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook"]]

    '''
    makes a move on the game board
    '''
    def make_move(self, move, player_one, player_two):
        # * perform move
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.starting_piece

        # * update player points if a piece has been captured in move
        opponent_color = player_two.color if player_one.current_player else player_one.color
        if opponent_color in move.ending_piece: # if capturing an opponent piece
            if "pawn" in move.ending_piece:
                pawn = Chess_Pieces.Pawn()

                if player_one.current_player: # if white is capturing a black piece
                    player_one.points_taken += pawn.point_value
                else: # else black is capturing a white piece
                    player_two.points_taken += pawn.point_value
            if "rook" in move.ending_piece: # if caputuring a rook
                rook = Chess_Pieces.Rook

                if player_one.current_player: # if white is capturing a black piece
                    player_one.points_taken += rook.point_value
                else: # else black is capturing a white piece
                    player_two.points_taken += rook.point_value
            if "knight" in move.ending_piece: # if caputuring a knight
                knight = Chess_Pieces.Knight()

                if player_one.current_player: # if white is capturing a black piece
                    player_one.points_taken += knight.point_value
                else: # else black is capturing a white piece
                    player_two.points_taken += knight.point_value
            if "bishop" in move.ending_piece: # if caputuring a bishop
                bishop = Chess_Pieces.Bishop()

                if player_one.current_player: # if white is capturing a black piece
                    player_one.points_taken += bishop.point_value
                else: # else black is capturing a white piece
                    player_two.points_taken += bishop.point_value
            if "queen" in move.ending_piece: # if caputuring a queen
                queen = Chess_Pieces.Queen()

                if player_one.current_player: # if white is capturing a black piece
                    player_one.points_taken += queen.point_value
                else: # else black is capturing a white piece
                    player_two.points_taken += queen.point_value

        # * update game log
        self.move_log.append(move)

    '''
    undo last move made
    '''
    def undo_move(self, player_one, player_two):
        if len(self.move_log) != 0: # if at least one move has been made
            # * perform action of undo move
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.starting_piece
            self.board[move.end_row][move.end_col] = move.ending_piece

            # * update player points if a piece had been captured in move - needs to be undone
            ally_color = player_one.color if player_one.current_player else player_two.color
            if ally_color in move.ending_piece: # if capturing an opponent piece
                if "pawn" in move.ending_piece:
                    pawn = Chess_Pieces.Pawn()

                    if player_one.current_player: # if white is capturing a black piece
                        player_two.points_taken -= pawn.point_value
                    else: # else black is capturing a white piece
                        player_one.points_taken -= pawn.point_value
                if "rook" in move.ending_piece: # if caputuring a rook
                    rook = Chess_Pieces.Rook

                    if player_one.current_player: # if white is capturing a black piece
                        player_two.points_taken -= rook.point_value
                    else: # else black is capturing a white piece
                        player_one.points_taken -= rook.point_value
                if "knight" in move.ending_piece: # if caputuring a knight
                    knight = Chess_Pieces.Knight()

                    if player_one.current_player: # if white is capturing a black piece
                        player_two.points_taken -= knight.point_value
                    else: # else black is capturing a white piece
                        player_one.points_taken -= knight.point_value
                if "bishop" in move.ending_piece: # if caputuring a bishop
                    bishop = Chess_Pieces.Bishop()

                    if player_one.current_player: # if white is capturing a black piece
                        player_two.points_taken -= bishop.point_value
                    else: # else black is capturing a white piece
                        player_one.points_taken -= bishop.point_value
                if "queen" in move.ending_piece: # if caputuring a queen
                    queen = Chess_Pieces.Queen()

                    if player_one.current_player: # if white is capturing a black piece
                        player_two.points_taken -= queen.point_value
                    else: # else black is capturing a white piece
                        player_one.points_taken -= queen.point_value

    '''
    identifies all potential moves while considering checks
    '''
    def get_valid_moves(self, player_one, player_two):
        return self.get_all_possible_moves(player_one, player_two) # ! place holder while implementing all possible moves

    '''
    identifies all potential moves without considering checks
    '''
    def get_all_possible_moves(self, player_one, player_two):
        possible_moves = []

        for row in range(len(self.board)): # goes through the game board row tiles
            for col in range(len(self.board[row])): # goes through the game board column tiles
                if ("white" in self.board[row][col] and player_one.current_player) or ("black" in self.board[row][col] and player_two.current_player): # if a tile has a chess piece on it belonging to the current player
                    if "pawn" in self.board[row][col]: # pawn moves
                        self.get_pawn_moves(row, col, possible_moves, player_one, player_two)
                    elif "rook" in self.board[row][col]: # rook moves
                        self.get_rook_moves(row, col, possible_moves, player_one, player_two)
                    elif "knight" in self.board[row][col]: # knight moves
                        self.get_knight_moves(row, col, possible_moves, player_one, player_two)
                    elif "bishop" in self.board[row][col]: # bishop moves
                        self.get_bishop_moves(row, col, possible_moves, player_one, player_two)
                    elif "queen" in self.board[row][col]: # queen moves
                        self.get_queen_moves(row, col, possible_moves, player_one, player_two)
                    elif "king" in self.board[row][col]: # king moves
                        self.get_king_moves(row, col, possible_moves, player_one, player_two)
                    
        return possible_moves

    '''
    get all pawn moves for the pawn located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_pawn_moves(self, row, col, possible_moves, player_one, player_two): # TODO transform pawns into any piece desired if reached end of board
        if player_one.current_player: # if it is whites turn
            # * moving forward
            if self.board[row - 1][col] == "--": # if tile in-front of pawn is open
                possible_moves.append(Moves((row, col), (row - 1, col), self.board))

                if row == 6 and self.board[row - 2][col] == "--": # if pawn hasn't been moved yet - ability to move two tiles
                    possible_moves.append(Moves((row, col), (row - 2, col), self.board))

            # * capturing pieces
            if col - 1 >= 0: # protects pawn from moving off the game board to the left
                if "black" in self.board[row - 1][col - 1]: # if opponent piece can be captured up and to the left of pawn
                    possible_moves.append(Moves((row, col), (row - 1, col - 1), self.board))

            if col + 1 <= 7: # protects pawn from moving off the game board to the right
                if "black" in self.board[row - 1][col + 1]: # if opponent piece can be captured up and to the right of pawn
                    possible_moves.append(Moves((row, col), (row - 1, col + 1), self.board))        
        elif player_two: # else blacks turn
            # * moving forward
            if self.board[row + 1][col] == "--": # if tile in-front of pawn is open
                possible_moves.append(Moves((row, col), (row + 1, col), self.board))

                if row == 1 and self.board[row + 2][col] == "--": # if pawn hasn't been moved yet - ability to move two tiles
                    possible_moves.append(Moves((row, col), (row + 2, col), self.board))

            # * capturing pieces
            if col - 1 >= 0: # protects pawn from moving off the game board to the left
                if "white" in self.board[row + 1][col - 1]: # if opponent piece can be captured up and to the left of pawn
                    possible_moves.append(Moves((row, col), (row + 1, col - 1), self.board))

            if col + 1 <= 7: # protects pawn from moving off the game board to the right
                if "white" in self.board[row + 1][col + 1]: # if opponent piece can be captured up and to the right of pawn
                    possible_moves.append(Moves((row, col), (row + 1, col + 1), self.board)) 

    '''
    get all rook moves for the rook located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_rook_moves(self, row, col, possible_moves, player_one, player_two): 
        opponent_color = player_two.color if player_one.current_player else player_one.color

        temp_row = row
        temp_col = col
        keep_going = True
        
        # * moving upward
        while temp_row > 0 and keep_going: # continue to check upward until off board or block incountered
            temp_row -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # * moving downward
        while temp_row < 7 and keep_going: # continue to check downward until off board or block incountered
            temp_row += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # * moving left
        while temp_col > 0 and keep_going: # continue to check left until off board or block incountered
            temp_col -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # * moving right
        while temp_col < 7 and keep_going: # continue to check right until off board or block incountered
            temp_col += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

    '''
    get all knight moves for the knight located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_knight_moves(self, row, col, possible_moves, player_one, player_two): 
        ally_color = player_one.color if player_one.current_player else player_two.color
        
        if row - 1 > 0: # if two tile spaces up is not off the game board
            if col > 0: # if one tile space to the left is not off the game board
                if not ally_color in self.board[row - 2][col - 1]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row - 2, col - 1), self.board)) #  * up-up-left move action

            if col < 7: # if one tile space to the right is not off the game board
                if not ally_color in self.board[row - 2][col + 1]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row - 2, col + 1), self.board)) # * up-up-right move action       
        
        if row + 1 < 7: # if two tile spaces down is not off the game board
            if col > 0: # if one tile space to the left is not off the game board
                if not ally_color in self.board[row + 2][col - 1]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row + 2, col - 1), self.board)) # * down-down-left move action

            if col < 7: # if one tile space to the right is not off the game board
                if not ally_color in self.board[row + 2][col + 1]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row + 2, col + 1), self.board)) # * down-down-right move action
                
        if col - 1 > 0: # if two tile spaces left is not off the game board
            if row > 0: # if one tile space up is not off the game board
                if not ally_color in self.board[row - 1][col - 2]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row - 1, col - 2), self.board)) # * left-left-up move action

            if row < 7: # if one tile space down is not off the game board
                if not ally_color in self.board[row + 1][col - 2]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row + 1, col - 2), self.board)) # * left-left-down move action
        
        if col + 1 < 7: # if two tile spaces right is not off the game board
            if row > 0: # if one tile space up is not off the game board
                if not ally_color in self.board[row - 1][col + 2]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row - 1, col + 2), self.board)) # * right-right-up move action

            if row < 7: # if one tile space down is not off the game board
                if not ally_color in self.board[row + 1][col + 2]: # if not an ally piece in desired tile location
                    possible_moves.append(Moves((row, col), (row + 1, col + 2), self.board)) # * right-right-down move action

    '''
    get all bishop moves for the bishop located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_bishop_moves(self, row, col, possible_moves, player_one, player_two):  
        opponent_color = player_two.color if player_one.current_player else player_one.color

        temp_row = row
        temp_col = col
        keep_going = True
        
        # * moving up-right direction
        while temp_row > 0 and temp_col < 7 and keep_going: # continue to check upward and to the right until off board or block incountered
            temp_row -= 1
            temp_col += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # * moving up-left direction
        while temp_row > 0 and temp_col > 0 and keep_going: # continue to check upward and to the left until off board or block incountered
            temp_row -= 1
            temp_col -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # * moving down-right direction
        while temp_row < 7 and temp_col < 7 and keep_going: # continue to check down and to the left until off board or block incountered
            temp_row += 1
            temp_col += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # * moving down-left direction
        while temp_row < 7 and temp_col > 0 and keep_going: # continue to check down and to the right until off board or block incountered
            temp_row += 1
            temp_col -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

    '''
    get all queen moves for the queen located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_queen_moves(self, row, col, possible_moves, player_one, player_two): 
        self.get_rook_moves(row, col, possible_moves, player_one, player_two)
        self.get_bishop_moves(row, col, possible_moves, player_one, player_two)

    '''
    get all king moves for the king located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_king_moves(self, row, col, possible_moves, player_one, player_two):  
        ally_color = player_one.color if player_one.current_player else player_two.color

        # * moving up
        if row > 0: # if not on the top row of the game board
            if not ally_color in self.board[row - 1][col]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row - 1, col), self.board))

        # * moving up-left
        if row > 0 and col > 0: # if not on the top row or furthest left column of the game board
            if not ally_color in self.board[row - 1][col - 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row - 1, col - 1), self.board))

        # * moving up-right
        if row > 0 and col < 7: # if not on the top row or furthest right column of the game board
            if not ally_color in self.board[row - 1][col + 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row - 1, col + 1), self.board))

        # * moving down
        if row < 7: # if not on the bottom row of the game board
            if not ally_color in self.board[row + 1][col]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row + 1, col), self.board))

        # * moving down-left
        if row < 7 and col > 0: # if not on the bottom row or furthest left column of the game board
            if not ally_color in self.board[row + 1][col - 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row + 1, col - 1), self.board))

        # * moving down-right
        if row < 7 and col < 7: # if not on the bottom row or furthest right column of the game board
            if not ally_color in self.board[row + 1][col + 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row + 1, col + 1), self.board))

        # * moving left
        if col > 0: # if not on the furthest left column of the game board
            if not ally_color in self.board[row][col - 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row, col - 1), self.board))

        # * moving right
        if col < 7: # if not on the furthest right column of the game board
            if not ally_color in self.board[row][col + 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves((row, col), (row, col + 1), self.board))

    '''
    assists in checking tile status
    '''
    def tile_checker(self, row, col, temp_row, temp_col, possible_moves, opponent_color):
        if self.board[temp_row][temp_col] == "--": # if open tile above currently observing tile
            possible_moves.append(Moves((row, col), (temp_row, temp_col), self.board))
            return True
        elif opponent_color in self.board[temp_row][temp_col]: # else if tile above observing tile is occupied by an enemy piece
            possible_moves.append(Moves((row, col), (temp_row, temp_col), self.board))
        
        return False
    
'''
Keeps a log of the moves made by the player and performs such action
'''
class Moves():
    # hash table - map dictionaries cooresponding a chess board tile representation with an array representation
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