'''
Keeps track of the board state and determains valid moves

Keeps a move log for the game
'''

import Moves

class GameState():
    # constructor for the class GameState
    def __init__(self):
        # game state
        self.current_player_white = True
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
    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.starting_piece
        self.move_log.append(move)
        self.current_player_white = not self.current_player_white

    '''
    undo last move made
    '''
    def undo_move(self):
        if len(self.move_log) != 0: # if at least one move has been made
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.starting_piece
            self.board[move.end_row][move.end_col] = move.ending_piece
            self.current_player_white = not self.current_player_white

    '''
    identifies all potential moves while considering checks
    '''
    def get_valid_moves(self):
        return self.get_all_possible_moves() # ! place holder while implementing all possible moves

    '''
    identifies all potential moves without considering checks
    '''
    def get_all_possible_moves(self):
        possible_moves = []

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if ("white" in self.board[row][col] and self.current_player_white) or ("black" in self.board[row][col] and not self.current_player_white): # if piece on tile belongs to the current player
                    if "pawn" in self.board[row][col]: # pawn moves
                        self.get_pawn_moves(row, col, possible_moves)
                    elif "rook" in self.board[row][col]: # rook moves
                        self.get_rook_moves(row, col, possible_moves)
                    elif "knight" in self.board[row][col]: # knight moves
                        self.get_knight_moves(row, col, possible_moves)
                    elif "bishop" in self.board[row][col]: # bishop moves
                        self.get_bishop_moves(row, col, possible_moves)
                    elif "queen" in self.board[row][col]: # queen moves
                        self.get_queen_moves(row, col, possible_moves)
                    elif "king" in self.board[row][col]: # king moves
                        self.get_king_moves(row, col, possible_moves)
                    
        return possible_moves

    '''
    get all pawn moves for the pawn located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_pawn_moves(self, row, col, possible_moves): # TODO transform pawns into any piece desired if reached end of board
        if self.current_player_white: # if it is whites turn
            # moving forward
            if self.board[row - 1][col] == "--": # if tile in-front of pawn is open
                possible_moves.append(Moves.Moves((row, col), (row - 1, col), self.board))

                if row == 6 and self.board[row - 2][col] == "--": # if pawn hasn't been moved yet - ability to move two tiles
                    possible_moves.append(Moves.Moves((row, col), (row - 2, col), self.board))

            # capturing pieces
            if col - 1 >= 0: # protects pawn from moving off the game board to the left
                if "black" in self.board[row - 1][col - 1]: # if opponent piece can be captured up and to the left of pawn
                    possible_moves.append(Moves.Moves((row, col), (row - 1, col - 1), self.board))

            if col + 1 <= 7: # protects pawn from moving off the game board to the right
                if "black" in self.board[row - 1][col + 1]: # if opponent piece can be captured up and to the right of pawn
                    possible_moves.append(Moves.Moves((row, col), (row - 1, col + 1), self.board))        
                
        else: # else blacks turn
            # moving forward
            if self.board[row + 1][col] == "--": # if tile in-front of pawn is open
                possible_moves.append(Moves.Moves((row, col), (row + 1, col), self.board))

                if row == 1 and self.board[row + 2][col] == "--": # if pawn hasn't been moved yet - ability to move two tiles
                    possible_moves.append(Moves.Moves((row, col), (row + 2, col), self.board))

            # capturing pieces
            if col - 1 >= 0: # protects pawn from moving off the game board to the left
                if "white" in self.board[row + 1][col - 1]: # if opponent piece can be captured up and to the left of pawn
                    possible_moves.append(Moves.Moves((row, col), (row + 1, col - 1), self.board))

            if col + 1 <= 7: # protects pawn from moving off the game board to the right
                if "white" in self.board[row + 1][col + 1]: # if opponent piece can be captured up and to the right of pawn
                    possible_moves.append(Moves.Moves((row, col), (row + 1, col + 1), self.board)) 

    '''
    get all rook moves for the rook located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_rook_moves(self, row, col, possible_moves): 
        opponent_color = "black" if self.current_player_white else "white"

        temp_row = row
        temp_col = col
        keep_going = True
        
        # moving upward
        while temp_row > 0 and keep_going: # continue to check upward until off board or block incountered
            temp_row -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # moving downward
        while temp_row < 7 and keep_going: # continue to check downward until off board or block incountered
            temp_row += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # moving left
        while temp_col > 0 and keep_going: # continue to check left until off board or block incountered
            temp_col -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # moving right
        while temp_col < 7 and keep_going: # continue to check right until off board or block incountered
            temp_col += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

    '''
    get all knight moves for the knight located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_knight_moves(self, row, col, possible_moves): # TODO 
        pass

    '''
    get all bishop moves for the bishop located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_bishop_moves(self, row, col, possible_moves):  
        opponent_color = "black" if self.current_player_white else "white"

        temp_row = row
        temp_col = col
        keep_going = True
        
        # moving up-right
        while temp_row > 0 and temp_col < 7 and keep_going: # continue to check upward and to the right until off board or block incountered
            temp_row -= 1
            temp_col += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # moving up-left
        while temp_row > 0 and temp_col > 0 and keep_going: # continue to check upward and to the left until off board or block incountered
            temp_row -= 1
            temp_col -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # moving down-right
        while temp_row < 7 and temp_col < 7 and keep_going: # continue to check down and to the left until off board or block incountered
            temp_row += 1
            temp_col += 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        temp_row = row
        temp_col = col
        keep_going = True

        # moving down-left
        while temp_row < 7 and temp_col > 0 and keep_going: # continue to check down and to the right until off board or block incountered
            temp_row += 1
            temp_col -= 1
            keep_going = self.tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

    '''
    get all queen moves for the queen located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_queen_moves(self, row, col, possible_moves): 
        self.get_rook_moves(row, col, possible_moves)
        self.get_bishop_moves(row, col, possible_moves)

    '''
    get all king moves for the king located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_king_moves(self, row, col, possible_moves): # TODO 
        ally_color = "white" if self.current_player_white else "black"

        # moving up
        if row > 0: # if not on the top row of the game board
            if not ally_color in self.board[row - 1][col]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row - 1, col), self.board))

        # moving up-left
        if row > 0 and col > 0: # if not on the top row or furthest left column of the game board
            if not ally_color in self.board[row - 1][col - 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row - 1, col - 1), self.board))

        # moving up-right
        if row > 0 and col < 7: # if not on the top row or furthest right column of the game board
            if not ally_color in self.board[row - 1][col + 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row - 1, col + 1), self.board))

        # moving down
        if row < 7: # if not on the bottom row of the game board
            if not ally_color in self.board[row + 1][col]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row + 1, col), self.board))

        # moving down-left
        if row < 7 and col > 0: # if not on the bottom row or furthest left column of the game board
            if not ally_color in self.board[row + 1][col - 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row + 1, col - 1), self.board))

        # moving down-right
        if row < 7 and col < 7: # if not on the bottom row or furthest right column of the game board
            if not ally_color in self.board[row + 1][col + 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row + 1, col + 1), self.board))

        # moving left
        if col > 0: # if not on the furthest left column of the game board
            if not ally_color in self.board[row][col - 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row, col - 1), self.board))

        # moving right
        if col < 7: # if not on the furthest right column of the game board
            if not ally_color in self.board[row][col + 1]: # if not an ally piece; is open tile or an opponent piece occupying desired location
                possible_moves.append(Moves.Moves((row, col), (row, col + 1), self.board))

    '''
    assists in checking tile status
    '''
    def tile_checker(self, row, col, temp_row, temp_col, possible_moves, opponent_color):
        if self.board[temp_row][temp_col] == "--": # if open tile above currently observing tile
            possible_moves.append(Moves.Moves((row, col), (temp_row, temp_col), self.board))
            return True
        elif opponent_color in self.board[temp_row][temp_col]: # else if tile above observing tile is occupied by an enemy piece
            possible_moves.append(Moves.Moves((row, col), (temp_row, temp_col), self.board))
        
        return False