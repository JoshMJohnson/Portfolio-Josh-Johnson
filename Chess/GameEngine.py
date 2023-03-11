'''
Controls the available actions that a player can do regarding the chess game board
'''

# custom classes
import Chess_Pieces

'''
Keeps track of the board state and determains valid moves a player can make
'''
class GameState():
    '''
    constructor for the class GameState
    '''
    def __init__(self):
        self.move_log = []
        self.white_king = Chess_Pieces.King(True) # initialize white players king
        self.black_king = Chess_Pieces.King(False) # initialize black players king

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

        if "king" in move.starting_piece: # if the king was moved
            col_adjustment = move.end_col - move.start_col

            if player_one.current_player: # if white player made the move
                self.white_king.has_moved = True
                self.white_king.current_position = (move.end_row, move.end_col)

                # if white king is castling
                if col_adjustment > 1 or col_adjustment < -1: # if king has moved 2 spaces indicating a castle move
                    # move rook as well as the king
                    if col_adjustment > 1: # if king moved to the right
                        self.board[7][7] = "--" # set rook space to open tile
                        self.board[7][move.end_col - 1] = "white_rook" # setting rook back to original tile
                    else: # else king moved to the left
                        self.board[7][0] = "--" # set rook space to open tile
                        self.board[7][move.end_col + 1] = "white_rook" # setting rook back to original tile
            else: # else black player made the move
                self.black_king.has_moved = True
                self.black_king.current_position = (move.end_row, move.end_col)

                # if black king is castling
                if col_adjustment > 1 or col_adjustment < -1: # if king has moved 2 spaces indicating a castle move
                    # move rook as well as the king
                    if col_adjustment > 1: # if king moved to the right
                        self.board[0][7] = "--" # set rook space to open tile
                        self.board[0][move.end_col - 1] = "black_rook" # setting rook back to original tile
                    else: # else king moved to the left
                        self.board[0][0] = "--" # set rook space to open tile
                        self.board[0][move.end_col + 1] = "black_rook" # setting rook back to original tile

        # * transforming a pawn if pawn reached the end of the board
        if "pawn" in move.starting_piece:
            if (player_one.current_player and move.end_row == 0) or (player_two.current_player and move.end_row == 7): # if pawn reached end of board
                self.transform_pawn(move, player_one, player_two)
                        
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
                rook = Chess_Pieces.Rook()

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

        # * adjust current player
        if player_one.current_player: # if white player
            self.white_king.in_check = False
            player_one.current_player = False
            player_two.current_player = True
        else: # else black player
            self.black_king.in_check = False
            player_two.current_player = False
            player_one.current_player = True

        print("--------------------------")

    '''
    undo last move made
    '''
    def undo_move(self, player_one, player_two):
        if len(self.move_log) != 0: # if at least one move has been made
            # * perform action of undo move
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.starting_piece
            self.board[move.end_row][move.end_col] = move.ending_piece
        
            # * update kings position and status
            if "king" in move.starting_piece: # if the king was moved last turn 
                col_adjustment = move.end_col - move.start_col
                if player_one.current_player: # if black players king was moved in previous move 
                    self.black_king.current_position = (move.start_row, move.start_col) 

                    # sets status of king has_moved to False if applicable
                    for i in range(len(self.move_log)): # loops through the move log
                        if self.move_log[i].starting_tile == (0, 4): # if a move in the log starting tile matched kings starting position
                            break

                        if i == len(self.move_log) - 1: # if gone through entire list and no king movement found
                            self.black_king.has_moved = False
                    if col_adjustment > 1 or col_adjustment < -1: # if king has moved 2 spaces indicating a castle move
                        # move rook back as well as the king
                        if col_adjustment > 1: # if king moved to the right
                            self.board[0][5] = "--" # set rook space to open tile 
                            self.board[0][7] = "black_rook" # setting rook back to original tile
                        else: # else king moved to the left
                            self.board[0][3] = "--" # set rook space to open tile
                            self.board[0][0] = "black_rook" # setting rook back to original tile
                else: # else white players king was moved in previous move
                    self.white_king.current_position = (move.start_row, move.start_col) 
                    
                    # sets status of king has_moved to False if applicable
                    for i in range(len(self.move_log)): # loops through the move log
                        if self.move_log[i].starting_tile == (7, 4): # if a move in the log starting tile matched kings starting position
                            break

                        if i == len(self.move_log) - 1: # if gone through entire list and no king movement found
                            self.white_king.has_moved = False
                    if col_adjustment > 1 or col_adjustment < -1: # if king has moved 2 spaces indicating a castle move
                        # move rook back as well as the king
                        if col_adjustment > 1: # if king moved to the right
                            self.board[7][5] = "--" # set rook space to open tile 
                            self.board[7][7] = "white_rook" # setting rook back to original tile
                        else: # else king moved to the left
                            self.board[7][3] = "--" # set rook space to open tile
                            self.board[7][0] = "white_rook" # setting rook back to original tile

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
                    rook = Chess_Pieces.Rook()

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

            # * resets previous players check status
            if player_one.current_player: # if current player was white
                self.white_king.in_check = False
                player_one.current_player = False
                player_two.current_player = True
                player_one.player_lost = False
            else: # else current player was black
                self.black_king.in_check = False
                player_two.current_player = False
                player_one.current_player = True    
                player_two.player_lost = False         
            
            print("--------------------------")     

    '''
    identifies all potential moves while considering checks
    '''
    def get_valid_moves(self, player_one, player_two): 
        self.pin_locations, self.check_locations = self.pins_checks(player_one, player_two) 
        
        # gets current players king position and status
        if player_one.current_player: # if white players turn
            king_row = self.white_king.current_position[0]
            king_col = self.white_king.current_position[1]
            in_check = self.white_king.in_check
        else: # else if black players turn
            king_row = self.black_king.current_position[0]
            king_col = self.black_king.current_position[1]
            in_check = self.black_king.in_check

        moves = []

        if in_check: # if current player is in check
            print("CHECK")
            if len(self.check_locations) == 1: # if only one piece is causing check 
                # gather data about the piece that is causing the check on the player
                pins = self.pin_locations
                check = self.check_locations[0] 
                check_row = check[0] # row of the piece that is causing a check
                check_col = check[1] # column of the piece that is causing a check
                row_direction_relative_from_king = check[2] # row adjustment of piece from the position of the king  
                col_direction_relative_from_king = check[3] # column adjustment of piece from the position of the king 

                piece_causing_check = self.board[check_row][check_col] # name of the piece that is causing a check
                tile_causing_check = (check_row, check_col) # tile ID of the piece causing a check

                moves = self.get_all_possible_moves(player_one, player_two) 
                valid_moves = []

                if "knight" in piece_causing_check: # * if the knight piece is causing check
                    for move in moves: # loop through the list of possible moves
                        if tile_causing_check == move.ending_tile: # if a move in possible moves has an ending location of this knight causing check
                            valid_moves.append(move)
            
                temp_row = king_row # sets king row as a temp variable for looping
                temp_col = king_col # sets king column as a temp variable for looping
                
                # * direction of check relative of king current position 
                if row_direction_relative_from_king == -1 and col_direction_relative_from_king == 0: # if piece north of king is causing check
                    while temp_row > check_row: # continue checking tiles in-between the king and the piece causing check
                        temp_row -= 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins)
                elif row_direction_relative_from_king == 1 and col_direction_relative_from_king == 0: # else if piece south of king is causing check
                    while temp_row < check_row: # continue checking tiles in-between the king and the piece causing check
                        temp_row += 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins)
                elif row_direction_relative_from_king == 0 and col_direction_relative_from_king == -1: # else if piece west of king is causing check
                    while temp_col > check_col: # continue checking tiles in-between the king and the piece causing check
                        temp_col -= 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins)
                elif row_direction_relative_from_king == 0 and col_direction_relative_from_king == 1: # else if piece east of king is causing check
                    while temp_col < check_col: # continue checking tiles in-between the king and the piece causing check
                        temp_col += 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins)
                elif row_direction_relative_from_king == -1 and col_direction_relative_from_king == -1: # else if piece north-west of king is causing check
                    while temp_row > check_row: # continue checking tiles in-between the king and the piece causing check
                        temp_row -= 1
                        temp_col -= 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins)
                elif row_direction_relative_from_king == -1 and col_direction_relative_from_king == 1: # else if piece north-east of king is causing check
                    while temp_col < check_col: # continue checking tiles in-between the king and the piece causing check
                        temp_row -= 1
                        temp_col += 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins)
                elif row_direction_relative_from_king == 1 and col_direction_relative_from_king == -1: # else if piece south-west of king is causing check
                    while temp_row < check_row: # continue checking tiles in-between the king and the piece causing check
                        temp_row += 1
                        temp_col -= 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins) 
                elif row_direction_relative_from_king == 1 and col_direction_relative_from_king == 1: # else if piece south-east of king is causing check
                    while temp_row < check_row: # continue checking tiles in-between the king and the piece causing check
                        temp_row += 1
                        temp_col += 1

                        self.check_valid_move(temp_row, temp_col, moves, valid_moves, pins)

                # restrict movement of pinned pieces 
                for pin in pins: # loop through the list of all pinned pieces 
                    valid_moves = [move for move in valid_moves if not self.restrict_pins(move, pin)]

                self.get_king_moves(king_row, king_col, valid_moves, player_one, player_two) # gets valid king moves

                #! testing
                print("num valid moves: " + str(len(valid_moves)))
                for v in valid_moves:
                    print("valid moves: " + str(v.starting_tile) + ", " + str(v.ending_tile))
                #! testing        
                
                if len(valid_moves) == 0: # if player is in checkmate
                    if player_one.current_player: # if white players turn
                        player_one.player_lost = True
                    else: # else if black players turn
                        player_two.player_lost = True
                
                return valid_moves
            else: # multiple ways the king is in check; king must move 
                self.get_king_moves(king_row, king_col, moves, player_one, player_two)

                if len(moves) == 0: # if player is in checkmate
                    if player_one.current_player: # if white players turn
                        player_one.player_lost = True
                    else: # else if black players turn
                        player_two.player_lost = True
        else: # if current player is not in check
            print("NO CHECK")
            pins = self.pin_locations
            moves = self.get_all_possible_moves(player_one, player_two) 

            # restrict movement of pinned pieces
            for pin in pins: # loop through the list of all pinned pieces 
                moves = [move for move in moves if not self.restrict_pins(move, pin)]

            # add castle moves when legal to the list of valid moves
            if player_one.current_player: # if whites turn
                if self.white_king.has_moved == False: # if the king has not moved yet
                    self.castling(moves, player_one, player_two)
            else: # else black players turn
                if self.black_king.has_moved == False: # if the king has not moved yet
                    self.castling(moves, player_one, player_two)

        #! testing
        print("num valid moves: " + str(len(moves)))
        for v in moves:
            print("valid moves: " + str(v.starting_tile) + ", " + str(v.ending_tile))
        #! testing 

        return moves
    
    '''
    restricts movement of a pinned piece
    '''
    def restrict_pins(self, move, pin):
        pin_tile = (pin[0], pin[1])
        pin_row_direction = pin[2]
        pin_col_direction = pin[3]

        if move.starting_tile == pin_tile: # finds pinned piece
            move_row_adjustment = move.end_row - move.start_row
            move_col_adjustment = move.end_col - move.start_col

            if move_row_adjustment > 0 and move_col_adjustment == 0 and pin_row_direction == 1 and pin_col_direction == 0: # if check is down vertically relative from the king
                return False
            elif move_row_adjustment < 0 and move_col_adjustment == 0 and pin_row_direction == -1 and pin_col_direction == 0: # if check is up vertically relative from the king
                return False
            elif move_row_adjustment == 0 and move_col_adjustment < 0 and pin_row_direction == 0 and pin_col_direction == -1: # if check is left horizontally relative from the king
                return False
            elif move_row_adjustment == 0 and move_col_adjustment > 0 and pin_row_direction == 0 and pin_col_direction == 1: #  if check is right horizontally relative from the king
                return False
            elif move_row_adjustment < 0 and move_col_adjustment > 0 and pin_row_direction == -1 and pin_col_direction == 1: # if check is up-right diagonally relative from the king
                return False
            elif move_row_adjustment < 0 and move_col_adjustment < 0 and pin_row_direction == -1 and pin_col_direction == -1: # if check is up-left diagonally relative from the king
                return False
            elif move_row_adjustment > 0 and move_col_adjustment > 0 and pin_row_direction == 1 and pin_col_direction == 1: # if check is down-right diagonally relative from the king
                return False
            elif move_row_adjustment > 0 and move_col_adjustment < 0 and pin_row_direction == 1 and pin_col_direction == -1: # if check is down-left diagonally relative from the king
                return False
                              
            return True
        return False

    '''
    checks if a move can capture a piece that is causing check and is not a pin piece
    '''
    def check_valid_move(self, temp_row, temp_col, moves, valid_moves, pins): 
        for move in moves: # loop through the list of possible moves
            if move.ending_tile == (temp_row, temp_col): # if a possible move has an ending location of the current checking tile
                for pin in pins: # loop through the list of all pin pieces
                    if move.starting_tile == pin: # if not a pin piece
                        valid_moves.append(move)

                valid_moves.append(move)

    '''
    retrieves the current player kings pin pieces and check pieces
    '''
    def pins_checks(self, player_one, player_two): 
        pins = [] # ally pieces that are preventing a check and therefore cannot be moved
        checks = [] # contains the pieces putting the player in check

        if player_one.current_player: # if white players turn
            ally_color = player_one.color
            opponent_color = player_two.color
            ally_king_row = self.white_king.current_position[0]
            ally_king_col = self.white_king.current_position[1]
        else: # else black players turn
            ally_color = player_two.color
            opponent_color = player_one.color
            ally_king_row = self.black_king.current_position[0]
            ally_king_col = self.black_king.current_position[1]

        # * checks tiles in all directions 
        # moving upward vertically
        possible_pin = () 
        row_direction = -1
        col_direction = 0
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_row > 0 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.vertical_horizontal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col) 
            
        # moving downward vertically
        possible_pin = () 
        row_direction = 1
        col_direction = 0
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_row < 7 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.vertical_horizontal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col)

        # moving left horizontally
        possible_pin = () 
        row_direction = 0
        col_direction = -1
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_col > 0 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.vertical_horizontal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col)
        
        # moving right horizontally
        possible_pin = () 
        row_direction = 0
        col_direction = 1
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_col < 7 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.vertical_horizontal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col)
                
        # moving up-right direction
        possible_pin = () 
        row_direction = -1
        col_direction = 1
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_row > 0 and temp_col < 7 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.diagonal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col)

        # moving up-left direction
        possible_pin = () 
        row_direction = -1
        col_direction = -1
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_row > 0 and temp_col > 0 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.diagonal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col)

        # moving down-right direction
        possible_pin = () 
        row_direction = 1
        col_direction = 1
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_row < 7 and temp_col < 7 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.diagonal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col)

        # moving down-left direction
        possible_pin = () 
        row_direction = 1
        col_direction = -1
        temp_row = ally_king_row
        temp_col = ally_king_col
        keep_going = True
        
        while temp_row < 7 and temp_col > 0 and keep_going: # continue to check until off board or block incountered
            temp_row += row_direction
            temp_col += col_direction
            keep_going, possible_pin = self.diagonal_check_pin_helper(pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col)

        # * check for knight checks 
        if (ally_king_row - 2 >= 0) and (ally_king_col - 1 >= 0): # if not off board
            if ("knight" in self.board[ally_king_row - 2][ally_king_col - 1]) and (opponent_color in self.board[ally_king_row - 2][ally_king_col - 1]): # * up-up-left location
                checks.append((ally_king_row - 2, ally_king_col - 1, -2, -1)) 
                
                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True
        
        if (ally_king_row - 2 >= 0) and (ally_king_col + 1 <= 7): # if not off board                
            if ("knight" in self.board[ally_king_row - 2][ally_king_col + 1]) and (opponent_color in self.board[ally_king_row - 2][ally_king_col + 1]): # * up-up-right location 
                checks.append((ally_king_row - 2, ally_king_col + 1, -2, 1)) 

                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True
        
        if (ally_king_row + 2 <= 7) and (ally_king_col - 1 >= 0): # if not off board        
            if ("knight" in self.board[ally_king_row + 2][ally_king_col - 1]) and (opponent_color in self.board[ally_king_row + 2][ally_king_col - 1]): # * down-down-left location 
                checks.append((ally_king_row + 2, ally_king_col - 1, 2, -1)) 

                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True
        
        if (ally_king_row + 2 <= 7) and (ally_king_col + 1 <= 7): # if not off board        
            if ("knight" in self.board[ally_king_row + 2][ally_king_col + 1]) and (opponent_color in self.board[ally_king_row + 2][ally_king_col + 1]): # * down-down-right location 
                checks.append((ally_king_row + 2, ally_king_col + 1, 2, 1)) 

                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True
        
        if (ally_king_row - 1 >= 0) and (ally_king_col - 2 >= 0): # if not off board
            if ("knight" in self.board[ally_king_row - 1][ally_king_col - 2]) and (opponent_color in self.board[ally_king_row - 1][ally_king_col - 2]):  # * up-left-left location 
                checks.append((ally_king_row - 1, ally_king_col - 2, -1, -2)) 

                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True
        
        if (ally_king_row + 1 <= 7) and (ally_king_col - 2 >= 0): # if not off board        
            if ("knight" in self.board[ally_king_row + 1][ally_king_col - 2]) and (opponent_color in self.board[ally_king_row + 1][ally_king_col - 2]): # * down-left-left location 
                checks.append((ally_king_row + 1, ally_king_col - 2, 1, -2)) 

                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True
        
        if (ally_king_row - 1 >= 0) and (ally_king_col + 2 <= 7): #  if not off board        
            if ("knight" in self.board[ally_king_row - 1][ally_king_col + 2]) and (opponent_color in self.board[ally_king_row - 1][ally_king_col + 2]): # * up-right-right location 
                checks.append((ally_king_row - 1, ally_king_col + 2, -1, 2)) 

                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True
        
        if (ally_king_row + 1 <= 7) and (ally_king_col + 2 <= 7): # if not off board        
            if ("knight" in self.board[ally_king_row + 1][ally_king_col + 2]) and (opponent_color in self.board[ally_king_row + 1][ally_king_col + 2]): # * down-right-right location 
                checks.append((ally_king_row + 1, ally_king_col + 2, 1, 2)) 

                if ally_color == "white": # if white player is in check
                    self.white_king.in_check = True
                else: # else black player is in check
                    self.black_king.in_check = True

        return pins, checks

    '''
    checks vertically and horizonally tiles for checks and pins
    '''
    def vertical_horizontal_check_pin_helper(self, pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col): 
        if ally_color in self.board[temp_row][temp_col]: # if ally piece is located on tile under check
            if possible_pin == (): # if first allied piece - potential pin
                possible_pin = (temp_row, temp_col, row_direction, col_direction)
            else: # else second allied piece in the line - no pin; no check possible in this direction
                return False, possible_pin
        elif opponent_color in self.board[temp_row][temp_col]: # else if enemy piece is located on tile under check 
            piece_type = self.board[temp_row][temp_col].split('_', 1) # get piece specs separated by the '_'
            piece_type = piece_type[1] # gets the name of the piece

            if piece_type == "rook" or piece_type == "queen": # if a rook or a queen found in tile
                if possible_pin == () : # if piece at current tile location is in direct line of king
                    checks.append((temp_row, temp_col, row_direction, col_direction))

                    if ally_color == "white": # if white player is in check
                        self.white_king.in_check = True
                    else: # else black player is in check
                        self.black_king.in_check = True

                    return False, possible_pin
                else: # if an ally piece is in-between found opponent piece at current tile - pin exists 
                    pins.append(possible_pin)
                    return False, possible_pin
            else: # enemy piece found besides rook and queen - protected in that direction from checks
                return False, possible_pin
        
        return True, possible_pin
    
    '''
    checks diagonal tiles for checks and pins
    '''
    def diagonal_check_pin_helper(self, pins, checks, ally_color, opponent_color, possible_pin, row_direction, col_direction, temp_row, temp_col): 
        if ally_color in self.board[temp_row][temp_col]: # if ally piece is located on tile under check
            if possible_pin == (): # if first allied piece - potential pin
                possible_pin = (temp_row, temp_col, row_direction, col_direction)
            else: # else second allied piece in the line - no pin; no check possible in this direction
                return False, possible_pin
        elif opponent_color in self.board[temp_row][temp_col]: # else if enemy piece is located on tile under check
            piece_type = self.board[temp_row][temp_col].split('_', 1) # get piece specs separated by the '_'
            piece_type = piece_type[1] # gets the name of the piece

            if piece_type == "pawn": # handling case when pawn causes check
                if opponent_color == "black" and self.white_king.current_position[0] == temp_row + 1 and (self.white_king.current_position[1] == temp_col - 1 or self.white_king.current_position[1] == temp_col + 1): # if current player is the white player
                    checks.append((temp_row, temp_col, row_direction, col_direction))
                    self.white_king.in_check = True
                elif opponent_color == "white" and self.black_king.current_position[0] == temp_row - 1 and (self.black_king.current_position[1] == temp_col - 1 or self.black_king.current_position[1] == temp_col + 1): # if current player is the black player
                    checks.append((temp_row, temp_col, row_direction, col_direction))
                    self.black_king.in_check = True

                return False, possible_pin

            if piece_type == "bishop" or piece_type == "queen": # if a rook or a queen found in tile
                if len(possible_pin) == 0: # if piece at current tile location is in direct line of king
                    checks.append((temp_row, temp_col, row_direction, col_direction))

                    if ally_color == "white": # if white player is in check
                        self.white_king.in_check = True
                    else: # else black player is in check
                        self.black_king.in_check = True

                    return False, possible_pin
                else: # if an ally piece is in-between found opponent piece at current tile - pin exists
                    pins.append(possible_pin)
                    return False, possible_pin
            else: # enemy piece found besides rook and queen - protected in that direction from checks
                return False, possible_pin

        return True, possible_pin

    '''
    identifies all potential moves without considering checks
    '''
    def get_all_possible_moves(self, player_one, player_two):
        possible_moves = []

        for row in range(len(self.board)): # goes through the game board row tiles
            for col in range(len(self.board[row])): # goes through the game board column tiles
                if (player_one.color in self.board[row][col] and player_one.current_player) or (player_two.color in self.board[row][col] and player_two.current_player): # if a tile has a chess piece on it belonging to the current player
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
    def get_pawn_moves(self, row, col, possible_moves, player_one, player_two):
        if player_one.current_player: # if it is whites turn
            # * moving forward
            if self.board[row - 1][col] == "--": # if tile in-front of pawn is open
                possible_moves.append(Moves((row, col), (row - 1, col), self.board))

                if row == 6 and self.board[row - 2][col] == "--": # if pawn hasn't been moved yet - ability to move two tiles
                    possible_moves.append(Moves((row, col), (row - 2, col), self.board))

            # * capturing pieces
            if col - 1 >= 0: # protects pawn from moving off the game board to the left
                if player_two.color in self.board[row - 1][col - 1]: # if opponent piece can be captured up and to the left of pawn
                    possible_moves.append(Moves((row, col), (row - 1, col - 1), self.board))

            if col + 1 <= 7: # protects pawn from moving off the game board to the right
                if player_two.color in self.board[row - 1][col + 1]: # if opponent piece can be captured up and to the right of pawn
                    possible_moves.append(Moves((row, col), (row - 1, col + 1), self.board))        
        elif player_two: # else blacks turn
            # * moving forward
            if self.board[row + 1][col] == "--": # if tile in-front of pawn is open
                possible_moves.append(Moves((row, col), (row + 1, col), self.board))

                if row == 1 and self.board[row + 2][col] == "--": # if pawn hasn't been moved yet - ability to move two tiles
                    possible_moves.append(Moves((row, col), (row + 2, col), self.board))

            # * capturing pieces
            if col - 1 >= 0: # protects pawn from moving off the game board to the left
                if player_one.color in self.board[row + 1][col - 1]: # if opponent piece can be captured up and to the left of pawn
                    possible_moves.append(Moves((row, col), (row + 1, col - 1), self.board))

            if col + 1 <= 7: # protects pawn from moving off the game board to the right
                if player_one.color in self.board[row + 1][col + 1]: # if opponent piece can be captured up and to the right of pawn
                    possible_moves.append(Moves((row, col), (row + 1, col + 1), self.board)) 

    '''
    get all rook moves for the rook located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_rook_moves(self, row, col, possible_moves, player_one, player_two): 
        opponent_color = player_two.color if player_one.current_player else player_one.color

        # * moving upward
        temp_row = row
        temp_col = col
        keep_going = True                
        while temp_row > 0 and keep_going: # continue to check upward until off board or block incountered
            temp_row -= 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        # * moving downward
        temp_row = row
        temp_col = col
        keep_going = True        
        while temp_row < 7 and keep_going: # continue to check downward until off board or block incountered
            temp_row += 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        # * moving left
        temp_row = row
        temp_col = col
        keep_going = True        
        while temp_col > 0 and keep_going: # continue to check left until off board or block incountered
            temp_col -= 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        # * moving right
        temp_row = row
        temp_col = col
        keep_going = True        
        while temp_col < 7 and keep_going: # continue to check right until off board or block incountered
            temp_col += 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

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

        # * moving up-right direction
        temp_row = row
        temp_col = col
        keep_going = True                
        while temp_row > 0 and temp_col < 7 and keep_going: # continue to check upward and to the right until off board or block incountered
            temp_row -= 1
            temp_col += 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        # * moving up-left direction
        temp_row = row
        temp_col = col
        keep_going = True        
        while temp_row > 0 and temp_col > 0 and keep_going: # continue to check upward and to the left until off board or block incountered
            temp_row -= 1
            temp_col -= 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        # * moving down-right direction
        temp_row = row
        temp_col = col
        keep_going = True        
        while temp_row < 7 and temp_col < 7 and keep_going: # continue to check down and to the left until off board or block incountered
            temp_row += 1
            temp_col += 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

        # * moving down-left direction
        temp_row = row
        temp_col = col
        keep_going = True
        while temp_row < 7 and temp_col > 0 and keep_going: # continue to check down and to the right until off board or block incountered
            temp_row += 1
            temp_col -= 1
            keep_going = self.sequence_tile_checker(row, col, temp_row, temp_col, possible_moves, opponent_color)

    '''
    get all queen moves for the queen located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_queen_moves(self, row, col, possible_moves, player_one, player_two): 
        self.get_rook_moves(row, col, possible_moves, player_one, player_two)
        self.get_bishop_moves(row, col, possible_moves, player_one, player_two)

    '''
    get all king moves for the king located at a specified tile passing through as a parameter and add moves to the list of possible moves
    '''
    def get_king_moves(self, king_row, king_col, possible_moves, player_one, player_two): 
        # * moving up
        if king_row > 0: # if not on the top row of the game board
            temp_row = king_row - 1
            temp_col = king_col
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

        # * moving up-left
        if king_row > 0 and king_col > 0: # if not on the top row or furthest left column of the game board
            temp_row = king_row - 1
            temp_col = king_col - 1
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

        # * moving up-right
        if king_row > 0 and king_col < 7: # if not on the top row or furthest right column of the game board
            temp_row = king_row - 1
            temp_col = king_col + 1
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

        # * moving down
        if king_row < 7: # if not on the bottom row of the game board
            temp_row = king_row + 1
            temp_col = king_col 
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

        # * moving down-left
        if king_row < 7 and king_col > 0: # if not on the bottom row or furthest left column of the game board
            temp_row = king_row + 1
            temp_col = king_col - 1
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

        # * moving down-right
        if king_row < 7 and king_col < 7: # if not on the bottom row or furthest right column of the game board
            temp_row = king_row + 1
            temp_col = king_col + 1
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

        # * moving left
        if king_col > 0: # if not on the furthest left column of the game board
            temp_row = king_row 
            temp_col = king_col - 1
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

        # * moving right
        if king_col < 7: # if not on the furthest right column of the game board
            temp_row = king_row 
            temp_col = king_col + 1
            self.valid_king_move(king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two)

    '''
    checks if potential move will put king in check; if not then adds to list of possible moves for the king
    '''
    def valid_king_move(self, king_row, king_col, temp_row, temp_col, possible_moves, player_one, player_two):
        ally_color = player_one.color if player_one.current_player else player_two.color

        if not ally_color in self.board[temp_row][temp_col]: # if not an ally piece; is open tile or an opponent piece occupying desired location
            ending_tile_status = self.board[temp_row][temp_col]

            if ally_color == player_one.color: # if current player is white
                # temp move king on board to check for checks
                self.white_king.current_position = (temp_row, temp_col)
                self.board[king_row][king_col] = "--"
                self.board[temp_row][temp_col] = "white_king"

            else: # else current player is black
                # temp move king on board to check for checks
                self.black_king.current_position = (temp_row, temp_col)
                self.board[king_row][king_col] = "--"
                self.board[temp_row][temp_col] = "black_king"

            self.pin_locations, self.check_locations = self.pins_checks(player_one, player_two)

            if ally_color == player_one.color: # if current player is white
                if len(self.check_locations) == 0: # if this move doesnt put own king in check; is legal move
                    add_move = Moves((king_row, king_col), (temp_row, temp_col), self.board)
                    if add_move not in possible_moves:
                        possible_moves.append(add_move) 
                    
                # put king back after checking an available move
                self.white_king.current_position = (king_row, king_col)
                self.board[king_row][king_col] = "white_king"
                self.board[temp_row][temp_col] = ending_tile_status
                
            else: # else current player is black
                if len(self.check_locations) == 0: # if this move doesnt put own king in check; is legal move 
                    add_move = Moves((king_row, king_col), (temp_row, temp_col), self.board)
                    if add_move not in possible_moves:
                        possible_moves.append(add_move) 

                # put king back after checking an available move
                self.black_king.current_position = (king_row, king_col) 
                self.board[king_row][king_col] = "black_king"
                self.board[temp_row][temp_col] = ending_tile_status
            
    '''
    adds castling to valid moves where legal
    '''
    def castling(self, moves, player_one, player_two):
        if player_one.current_player: # if current player is white
            if self.white_king.has_moved == False: # if the white king has not moved yet
                # castling left direction
                rook_has_moved = False
                for move in range(len(self.move_log)): # loops through the move log
                    if self.move_log[move].starting_tile == (7, 0): # if a move in the log starting tile matched rook starting position
                        rook_has_moved = True
                        break
                        
                if not rook_has_moved: # if the rook hasn't moved yet
                    # if not castling through check
                    king_castle_temp = []
                    self.valid_king_move(self.white_king.current_position[0], self.white_king.current_position[1], self.white_king.current_position[0], self.white_king.current_position[1] - 1, king_castle_temp, player_one, player_two)
                    self.valid_king_move(self.white_king.current_position[0], self.white_king.current_position[1], self.white_king.current_position[0], self.white_king.current_position[1] - 2, king_castle_temp, player_one, player_two)

                    if len(king_castle_temp) == 2:
                        king_row = self.white_king.current_position[0]
                        king_col = self.white_king.current_position[1]
                        add_move = Moves((king_row, king_col), (king_row, king_col - 2), self.board)
                        moves.append(add_move)

                # castling right direction
                rook_has_moved = False
                for move in range(len(self.move_log)): # loops through the move log
                    if self.move_log[move].starting_tile == (7, 7): # if a move in the log starting tile matched rook starting position
                        rook_has_moved = True
                        break
                        
                if not rook_has_moved: # if the rook hasn't moved yet
                    # if not castling through check
                    king_castle_temp = []
                    self.valid_king_move(self.white_king.current_position[0], self.white_king.current_position[1], self.white_king.current_position[0], self.white_king.current_position[1] + 1, king_castle_temp, player_one, player_two)
                    self.valid_king_move(self.white_king.current_position[0], self.white_king.current_position[1], self.white_king.current_position[0], self.white_king.current_position[1] + 2, king_castle_temp, player_one, player_two)

                    if len(king_castle_temp) == 2:
                        king_row = self.white_king.current_position[0]
                        king_col = self.white_king.current_position[1]
                        add_move = Moves((king_row, king_col), (king_row, king_col + 2), self.board)
                        moves.append(add_move)
        else: # else current player is black
            if self.black_king.has_moved == False: # if the white king has not moved yet
                # castling left direction
                rook_has_moved = False
                for move in range(len(self.move_log)): # loops through the move log
                    if self.move_log[move].starting_tile == (0, 0): # if a move in the log starting tile matched rook starting position
                        rook_has_moved = True
                        break
                        
                if not rook_has_moved: # if the rook hasn't moved yet
                    # if not castling through check
                    king_castle_temp = []
                    self.valid_king_move(self.black_king.current_position[0], self.black_king.current_position[1], self.black_king.current_position[0], self.black_king.current_position[1] - 1, king_castle_temp, player_one, player_two)
                    self.valid_king_move(self.black_king.current_position[0], self.black_king.current_position[1], self.black_king.current_position[0], self.black_king.current_position[1] - 2, king_castle_temp, player_one, player_two)

                    if len(king_castle_temp) == 2:
                        king_row = self.black_king.current_position[0]
                        king_col = self.black_king.current_position[1]
                        add_move = Moves((king_row, king_col), (king_row, king_col - 2), self.board)
                        moves.append(add_move)

                # castling right direction
                rook_has_moved = False
                for move in range(len(self.move_log)): # loops through the move log
                    if self.move_log[move].starting_tile == (0, 7): # if a move in the log starting tile matched rook starting position
                        rook_has_moved = True
                        break
                        
                if not rook_has_moved: # if the rook hasn't moved yet
                    # if not castling through check
                    king_castle_temp = []
                    self.valid_king_move(self.black_king.current_position[0], self.black_king.current_position[1], self.black_king.current_position[0], self.black_king.current_position[1] + 1, king_castle_temp, player_one, player_two)
                    self.valid_king_move(self.black_king.current_position[0], self.black_king.current_position[1], self.black_king.current_position[0], self.black_king.current_position[1] + 2, king_castle_temp, player_one, player_two)

                    if len(king_castle_temp) == 2:
                        king_row = self.black_king.current_position[0]
                        king_col = self.black_king.current_position[1]
                        add_move = Moves((king_row, king_col), (king_row, king_col + 2), self.board)
                        moves.append(add_move)

    '''
    handles transforming a pawn when pawn reached the end of the board
    '''
    def transform_pawn(self, move, player_one, player_two): # TODO ability to pick any piece, not just the queen
        ally_color = player_one.color if player_one.current_player else player_two.color
        desired_piece = "queen"
        desired_piece_id = ally_color + "_" + desired_piece
        self.board[move.end_row][move.end_col] = desired_piece_id

    '''
    assists in checking tile status
    '''
    def sequence_tile_checker(self, row, col, temp_row, temp_col, possible_moves, opponent_color):
        if self.board[temp_row][temp_col] == "--": # if open tile above currently observing tile
            possible_moves.append(Moves((row, col), (temp_row, temp_col), self.board))
            return True
        elif opponent_color in self.board[temp_row][temp_col]: # else if tile above observing tile is occupied by an enemy piece
            possible_moves.append(Moves((row, col), (temp_row, temp_col), self.board))
        
        return False
    
'''
Helps keep a game log of moves
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
        self.starting_tile = (self.start_row, self.start_col)
        self.ending_tile = (self.end_row, self.end_col)

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
    def get_chess_notation(self):
        # chess piece abbreviations
        moving_piece_abbriv = ' '
        if "king" in self.starting_piece: # if moving a king
            moving_piece_abbriv = "K"
        elif "queen" in self.starting_piece: # else if moving a queen
            moving_piece_abbriv = "Q"
        elif "bishop" in self.starting_piece: # else if moving a bishop
            moving_piece_abbriv = "B"
        elif "knight" in self.starting_piece: # else if moving a knight
            moving_piece_abbriv = "N"
        elif "rook" in self.starting_piece: # else if moving a rook
            moving_piece_abbriv = "R"

        caputring_piece = ' '
        if self.ending_piece != "--":
            if "king" in self.ending_piece: # if moving a king
                caputring_piece = "K"
            elif "queen" in self.ending_piece: # else if moving a queen
                caputring_piece = "Q"
            elif "bishop" in self.ending_piece: # else if moving a bishop
                caputring_piece = "B"
            elif "knight" in self.ending_piece: # else if moving a knight
                caputring_piece = "N"
            elif "rook" in self.ending_piece: # else if moving a rook
                caputring_piece = "R"

        return moving_piece_abbriv + self.get_rank_file_pair(self.start_row, self.start_col) + " -> " + caputring_piece + self.get_rank_file_pair(self.end_row, self.end_col)

    '''
    returns the chess notation of a tile on the game board
    '''
    def get_rank_file_pair(self, row, col):
        return self.cols_to_files[col] + self.rows_to_ranks[row]