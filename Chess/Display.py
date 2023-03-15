'''
Driver file

Controls the visual aspects when running the program, and handles user input

Created By: Josh Johnson
'''

# python libraries
import pygame # gui for python game
import os # used to get absolute path for the project
from sys import exit
# import threading # ? possible solution for two different player game times running at the same time

# project classes
import GameEngine
import Player

# * game board settings - part 1
BOARD_WIDTH = 400 # game board width
BOARD_HEIGHT = 400 # game board height
DIMENSION = 8 # 8x8 board
TILE_SIZE = BOARD_WIDTH // DIMENSION # size of a square (tile) on the gui
MAX_FPS = 15 # for animations
PIECE_IMAGES = {} # global dictionary of chess piece images
chess_set = 1 # indicates which chess set to use; default is set 1

# * tile selected to move - indicate selected tile
highlighted_tile_color = '' 
highlighted_tile = False
left_x_loc = -1
right_x_loc = -1
top_y_loc = -1
bottom_y_loc = -1

# * window settings
WINDOW_WIDTH = BOARD_WIDTH + 300
WINDOW_HEIGHT = BOARD_HEIGHT + 200
GAP = 25 # spacing the board is from the edge of the window

# * game log settings
log_frame_width = WINDOW_WIDTH - BOARD_WIDTH - (GAP * 3)
log_frame_height = WINDOW_HEIGHT - (GAP * 3) - 75
log_frame_starting_x_coordinate = BOARD_WIDTH + (GAP * 2)
log_frame_starting_y_coordinate = GAP
game_log = []

# * bottom right button section
button_spacing_x = 10
button_section_height = WINDOW_HEIGHT - log_frame_height - (GAP * 3)
button_section_width = log_frame_width
corner_button_dimensions = (button_section_width - (button_spacing_x * 3)) / 4
corner_section_starting_x = log_frame_starting_x_coordinate
corner_section_starting_y = WINDOW_HEIGHT - GAP - button_section_height
logo_dimensions = corner_button_dimensions - (corner_button_dimensions * 0.25)

# * heading panel settings
heading_width = BOARD_WIDTH
heading_height = WINDOW_HEIGHT - BOARD_HEIGHT - (GAP * 3)
heading_starting_x_coordinate = GAP
heading_starting_y_coordinate = GAP
font_color = '' 
heading_background_color = ''

# * current player symbol
active_symbol_size = 5
symbol_location_adjustment = heading_width / 5
active1_symbol_xlocation = heading_starting_x_coordinate + symbol_location_adjustment
active2_symbol_xlocation = heading_starting_x_coordinate + heading_width - symbol_location_adjustment
active_symbol_ylocation = heading_starting_y_coordinate + 57

# * buttons in heading
heading_button_width = 8
heading_button_height = 16

# * initialize players
player_one = Player.Player(1)
player_two = Player.Player(2)

# * game board settings - part 2
game_board_starting_x_coordinate = GAP
game_board_starting_y_coordinate = WINDOW_HEIGHT - BOARD_HEIGHT - GAP

# * running program type
is_script = False

'''
loads the desired chess set
'''
def load_chess_set(screen):
    global font_color
    global heading_background_color
    global highlighted_tile_color

    # * chess theme settings
    if chess_set == 1: # chess set 1
        piece_set = "Set1"
        background_color = 'light grey'
        heading_background_color = 'white'
        font_color = 'black'
        highlighted_tile_color = pygame.Color(105,105,105)
    elif chess_set == 2: # chess set 2
        piece_set = "Set2"
        background_color = pygame.Color(222,184,135)
        heading_background_color = pygame.Color(255,228,196)
        font_color = pygame.Color(139,69,19)
        highlighted_tile_color = 'black'
    else: # chess set 3
        piece_set = "Set3"
        background_color = pygame.Color(51,51,51)
        heading_background_color = 'black'
        font_color = 'white'
        highlighted_tile_color = pygame.Color(0, 191, 255)

    game_log_background_color = heading_background_color

    # * load chess pieces
    pieces = ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook", "black_pawn",
                "white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook", "white_pawn"]
    
    if not is_script: # used for running Display.py directly from VS
        base_path = os.path.dirname(__file__) # finds absolute path for the project
        for piece in pieces:
            image_path = os.path.join(base_path, "Game_Images", piece_set, piece + ".png")
            PIECE_IMAGES[piece] = pygame.transform.scale(pygame.image.load(image_path), (TILE_SIZE, TILE_SIZE))
    else: # used for running script
        for piece in pieces:
            image_path = os.path.join("Game_Images", piece_set, piece + ".png")
            PIECE_IMAGES[piece] = pygame.transform.scale(pygame.image.load(image_path), (TILE_SIZE, TILE_SIZE))

    # * loads set background    
    screen.fill(pygame.Color(background_color))

    # * display heading initial content
    pygame.draw.rect(screen, heading_background_color, pygame.Rect(heading_starting_x_coordinate, heading_starting_y_coordinate, heading_width, heading_height))

    # display the title
    title_font = pygame.font.SysFont('monospace', 32, 'bold')
    title_label = title_font.render("The Game of Chess", True, font_color)
    title_rect = title_label.get_rect(center=(heading_width / 2 + heading_starting_x_coordinate, heading_starting_y_coordinate + GAP))
    screen.blit(title_label, title_rect)

    # display the initial player settings in the heading
    heading_font = pygame.font.SysFont('monospace', 12)

    #  player one
    # create player labels
    player_color1_label = heading_font.render("Player : ", True, font_color)
    player_points_taken1_label = heading_font.render("Points Taken : ", True, font_color)
    player_time_remaining1_label = heading_font.render("Time Remaining : ", True, font_color)
    
    # display player labels
    screen.blit(player_color1_label, (heading_starting_x_coordinate + (GAP / 2), heading_starting_y_coordinate + (GAP * 2)))
    screen.blit(player_points_taken1_label, (heading_starting_x_coordinate + (GAP / 2), heading_starting_y_coordinate + (GAP * 3)))
    screen.blit(player_time_remaining1_label, (heading_starting_x_coordinate + (GAP / 2), heading_starting_y_coordinate + (GAP * 4)))    

    # player two
    # create player labels
    player_color2_label = heading_font.render(" : Player", True, font_color)
    player_points_taken2_label = heading_font.render(" : Points Taken", True, font_color)
    player_time_remaining2_label = heading_font.render(" : Time Remaining", True, font_color)
    
    # create player label rectangles
    player_color2_label_rect = player_color2_label.get_rect(topright=(heading_starting_x_coordinate + heading_width - (GAP / 2), heading_starting_y_coordinate + (GAP * 2)))
    player_points_taken2_label_rect = player_points_taken2_label.get_rect(topright=(heading_starting_x_coordinate + heading_width - (GAP / 2), heading_starting_y_coordinate + (GAP * 3)))
    player_time_remaining2_label_rect = player_time_remaining2_label.get_rect(topright=(heading_starting_x_coordinate + heading_width - (GAP / 2), heading_starting_y_coordinate + (GAP * 4)))
    
    # insert into heading
    screen.blit(player_color2_label, player_color2_label_rect)
    screen.blit(player_points_taken2_label, player_points_taken2_label_rect)
    screen.blit(player_time_remaining2_label, player_time_remaining2_label_rect) 

    # current player symbol; player one symbol = active
    pygame.draw.circle(screen, font_color, (active1_symbol_xlocation, active_symbol_ylocation), active_symbol_size)
    
    # * prepare game log panel
    pygame.draw.rect(screen, game_log_background_color, pygame.Rect(log_frame_starting_x_coordinate, log_frame_starting_y_coordinate, log_frame_width, log_frame_height))

    # * load and draw the ranks and files for the board (numbers and letters on the sides of the board identifying tiles)
    rank_file_font = pygame.font.SysFont('monospace', 16)
    starting_file_value = 65 # ascii value of 'A'
    
    for col in range(DIMENSION): # draws the file (column) identifiers for the chess board
        pygame.draw.rect(screen, background_color, pygame.Rect((col * TILE_SIZE) + (TILE_SIZE / 2) + GAP, WINDOW_HEIGHT - (GAP / 2), GAP / 2, GAP / 2))
        col_label = rank_file_font.render(chr(starting_file_value), True, font_color)
        file_label_rect = col_label.get_rect(center=((TILE_SIZE * col) + (TILE_SIZE / 2) + GAP, WINDOW_HEIGHT - (GAP / 2))) 
        screen.blit(col_label, file_label_rect)
        starting_file_value += 1 # assign file ascii value to be equal to the next column

    for row in range(DIMENSION): # draws the rank (row) identifiers for the chess board
        pygame.draw.rect(screen, background_color, pygame.Rect(GAP / 2, (row * TILE_SIZE) + WINDOW_HEIGHT - GAP - (TILE_SIZE / 2), GAP / 2, GAP / 2))
        row_label = rank_file_font.render(str(row + 1), True, font_color)
        rank_label_rect = row_label.get_rect(center=(GAP / 2, WINDOW_HEIGHT - GAP - (TILE_SIZE * row) - (TILE_SIZE / 2)))
        screen.blit(row_label, rank_label_rect)

    # * load label for undo moves
    author_font = pygame.font.SysFont('monospace', 12, italic=True)
    author_label = author_font.render("Created by Josh Johnson", True, font_color)
    author_label_rect = author_label.get_rect(center=(log_frame_starting_x_coordinate + (log_frame_width / 2), WINDOW_HEIGHT - GAP))
    screen.blit(author_label, author_label_rect)
    
'''
displays the initial player values in the header
'''
def display_player_values(screen):
    heading_font = pygame.font.SysFont('monospace', 12, italic=True)

    # * player one values
    # create player value labels
    player_color1_value_label = heading_font.render(str(player_one.color), True, font_color)
    player_points_taken1_value_label = heading_font.render(str(player_one.points_taken), True, font_color)
    player_time_remaining1_value_label = heading_font.render(str(player_one.time_remaining), True, font_color)

    # create player value label rectangles
    player_color1_value_label_rect = player_color1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 2)))
    player_points_taken1_value_label_rect = player_points_taken1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 3)))
    player_time_remaining1_value_label_rect = player_time_remaining1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 4)))
    
    # display player value labels
    screen.blit(player_color1_value_label, player_color1_value_label_rect)
    screen.blit(player_points_taken1_value_label, player_points_taken1_value_label_rect)
    screen.blit(player_time_remaining1_value_label, player_time_remaining1_value_label_rect)  

    # * player two values
    # create player value labels
    player_color2_value_label = heading_font.render(str(player_two.color), True, font_color)
    player_points_taken2_value_label = heading_font.render(str(player_two.points_taken), True, font_color)
    player_time_remaining2_value_label = heading_font.render(str(player_two.time_remaining), True, font_color)

    # display player value labels
    screen.blit(player_color2_value_label, (heading_starting_x_coordinate + (heading_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 2)))
    screen.blit(player_points_taken2_value_label, (heading_starting_x_coordinate + (heading_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3)))
    screen.blit(player_time_remaining2_value_label, (heading_starting_x_coordinate + (heading_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 4)))  
        
'''
main function
'''
def main():
    open_new_window()

'''
loads the game with the chess set theme and runs the game
'''
def run_game(screen, clock):
    global chess_set
    global game_log
    global highlighted_tile
    global left_x_loc
    global right_x_loc
    global top_y_loc
    global bottom_y_loc
    global player_one
    global player_two

    load_chess_set(screen) 
    display_player_values(screen)
    create_theme_buttons(screen)
    create_game_buttons(screen)

    game_state = GameEngine.GameState()
    valid_moves = game_state.get_valid_moves(player_one, player_two) # gets all valid moves a player could make
    move_made = False

    tile_selected = () # keeps track of the last tile clicked by the user
    player_clicks = [] # keeps track of a plyaer clicks; two tuples: [(x1,y1), (x2,y2)]
    running = True

    # * actions to perform for an active game
    while running:
        for e in pygame.event.get(): # handles triggered events by user
            if e.type == pygame.QUIT: # quit application
                running = False
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN: # else if mouse has clicked and is holding the button down
                location = pygame.mouse.get_pos() # (x, y) location of the mouse; x value at index 0; y value at index 1                
                col = (location[0] - GAP) // TILE_SIZE 
                row = (location[1] - (WINDOW_HEIGHT - BOARD_HEIGHT - GAP)) // TILE_SIZE
                if col >= 0 and col <= 7 and row >= 0 and row <= 7: # if clicking on the chess board
                    if tile_selected == (row, col): # if user clicked same tile twice in a row
                        tile_selected == () # deselect
                        player_clicks == [] # clear player clicks

                        if highlighted_tile:
                            highlighted_tile = False
                        else:
                            highlighted_tile = True
                    else: # else; 2 different tiles clicked in order
                        tile_selected = (row, col)
                        player_clicks.append(tile_selected)
                        if len(player_clicks) == 2: # if second tile was clicked that was different than the first 
                            move = GameEngine.Moves(player_clicks[0], player_clicks[1], game_state.board) 
                            if move in valid_moves:
                                game_state.make_move(move, player_one, player_two)
                                game_log.append(move.get_chess_notation())
                                move_made = True
                                update_player_points(screen)
                                display_game_log(screen)

                            # resets user input clicks
                            highlighted_tile = False
                            tile_selected = () 
                            player_clicks = []          
                        else: # if a tile has been selected indicating a starting location for a possible move
                            highlighted_tile = True

                            # tile location data
                            left_x_loc = (col * TILE_SIZE) + game_board_starting_x_coordinate
                            right_x_loc = left_x_loc + TILE_SIZE - 2
                            top_y_loc = (row * TILE_SIZE) + game_board_starting_y_coordinate
                            bottom_y_loc = top_y_loc + TILE_SIZE - 2                                       
                elif ((location[0] >= (heading_width / 2) - (heading_button_width / 2) + GAP) and (location[0] <= (heading_width / 2) + (heading_button_width / 2) + heading_button_width + GAP) 
                        and (location[1] >= heading_starting_y_coordinate + (GAP * 2)) and (location[1] <= heading_starting_y_coordinate + (GAP * 2) + heading_button_height)): # else if theme 1 is selected
                    chess_set = 1
                    game_log = []
                    highlighted_tile = False
                    player_one = Player.Player(1)
                    player_two = Player.Player(2)
                    pygame.quit() # close current window
                    open_new_window()
                elif ((location[0] >= (heading_width / 2) - (heading_button_width / 2) + GAP) and (location[0] <= (heading_width / 2) + (heading_button_width / 2) + heading_button_width + GAP) 
                        and (location[1] >= heading_starting_y_coordinate + (GAP * 3)) and (location[1] <= heading_starting_y_coordinate + (GAP * 3) + heading_button_height)): # else if theme 2 is selected
                    chess_set = 2
                    game_log = []
                    highlighted_tile = False
                    player_one = Player.Player(1)
                    player_two = Player.Player(2)
                    pygame.quit() # close current window
                    open_new_window()                    
                elif ((location[0] >= (heading_width / 2) - (heading_button_width / 2) + GAP) and (location[0] <= (heading_width / 2) + (heading_button_width / 2) + heading_button_width + GAP) 
                        and (location[1] >= heading_starting_y_coordinate + (GAP * 4)) and (location[1] <= heading_starting_y_coordinate + (GAP * 4) + heading_button_height)): # else if theme 3 is selected
                    chess_set = 3
                    game_log = []
                    highlighted_tile = False
                    player_one = Player.Player(1)
                    player_two = Player.Player(2)
                    pygame.quit() # close current window
                    open_new_window()  
                # elif : # TODO else if help button pressed
                #     help_button_active()                    
                # elif : # TODO else if settings button pressed
                #     settings_button_active()
                # elif : # TODO else if valid moves button pressed
                #     valid_moves_button_active()
                # elif : # TODO else if en passant button pressed
                #     en_passant_button_active()
            elif e.type == pygame.KEYDOWN: # if a key is pressed on the keyboard
                if e.key == pygame.K_u: # undo move and update game log
                    if len(game_log) != 0:
                        game_state.undo_move(player_one, player_two)
                        update_player_points(screen)
                        game_log.pop()
                        display_game_log(screen)
                        move_made = True

        if move_made: # if a move was made; get a new list of valid moves for the next move
            valid_moves = game_state.get_valid_moves(player_one, player_two)

            if len(valid_moves) == 0: # if checkmate or stalemate
                check_handling(screen, True)
            elif player_one.player_in_check or player_two.player_in_check: # else if check 
                check_handling(screen, False)
            
            update_current_player_symbol(screen)
            move_made = False

        draw_game_state(screen, game_state) 
        update_player_game_time(screen)
        clock.tick(MAX_FPS)
        pygame.display.flip()

'''
opens a new window
'''
def open_new_window():
    # * open new window with updated theme settings
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Lets Play Chess!")
    run_game(screen, clock)    

'''
handle checkmate and stalemate
'''
def check_handling(screen, is_game_over):
    status = "Check"
    check_font = pygame.font.SysFont('monospace', 12)

    if player_one.player_lost or player_two.player_lost: # if player 1 in checkmate
        status = "Checkmate"
    elif is_game_over: # else stalemate
        status = "Stalemate"

    # turn previous value invisible 
    check_label = check_font.render(str(status), True, heading_background_color, heading_background_color)
    screen.blit(check_label, (log_frame_starting_x_coordinate + 5, log_frame_starting_y_coordinate + 5))

    # display new value of player score
    check_label = check_font.render(str(status), True, font_color)
    screen.blit(check_label, (log_frame_starting_x_coordinate + 5, log_frame_starting_y_coordinate + 5))

'''
updates the player points
'''
def update_player_points(screen):  
    heading_font = pygame.font.SysFont('monospace', 12, italic=True)

    # * player one
    # turn previous value invisible 
    player_points_taken1_value_label = heading_font.render(str(39), True, heading_background_color, heading_background_color)
    player_points_taken1_value_label_rect = player_points_taken1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 3)))
    screen.blit(player_points_taken1_value_label, player_points_taken1_value_label_rect)

    # display new value of player score
    player_points_taken1_value_label = heading_font.render(str(player_one.points_taken), True, font_color)
    player_points_taken1_value_label_rect = player_points_taken1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 3)))
    screen.blit(player_points_taken1_value_label, player_points_taken1_value_label_rect)

    # * player two
    # turn previous value invisible 
    player_points_taken2_value_label = heading_font.render(str(39), True, heading_background_color, heading_background_color)
    screen.blit(player_points_taken2_value_label, (heading_starting_x_coordinate + (heading_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3)))

    # display new value of player score
    player_points_taken2_value_label = heading_font.render(str(player_two.points_taken), True, font_color)
    screen.blit(player_points_taken2_value_label, (heading_starting_x_coordinate + (heading_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3)))
        
'''
updates the player game time left
'''
def update_player_game_time(screen): 
    heading_font = pygame.font.SysFont('monospace', 12, italic=True)

    if player_one.current_player: # TODO if whites players move
        # starts/stops player timer


        # turns old player time value invisible
        player_points_taken1_value_label = heading_font.render('99:99', True, heading_background_color, heading_background_color)
        player_points_taken1_value_label_rect = player_points_taken1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 4)))
        screen.blit(player_points_taken1_value_label, player_points_taken1_value_label_rect)

        # writes new player time
        player_time_remaining1_value_label = heading_font.render(str(player_one.time_remaining), True, font_color)
        player_time_remaining1_value_label_rect = player_time_remaining1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 4)))   
        screen.blit(player_time_remaining1_value_label, player_time_remaining1_value_label_rect)  
    else: # TODO else black players move
        pass

'''
current player symbol change
'''
def update_current_player_symbol(screen):
    if player_one.current_player: # if current player needs to be white
        pygame.draw.circle(screen, font_color, (active1_symbol_xlocation, active_symbol_ylocation), active_symbol_size) # player 1
        pygame.draw.circle(screen, heading_background_color, (active2_symbol_xlocation, active_symbol_ylocation), active_symbol_size) # player 2
    else: # else current player needs to be black
        pygame.draw.circle(screen, heading_background_color, (active1_symbol_xlocation, active_symbol_ylocation), active_symbol_size) # player 1
        pygame.draw.circle(screen, font_color, (active2_symbol_xlocation, active_symbol_ylocation), active_symbol_size) # player 2

''' 
creates all graphics of the game 
'''
def draw_game_state(screen, game_state):
    draw_board_tiles(screen) 
    draw_pieces(screen, game_state.board) 
    if highlighted_tile: # if a starting tile has been selected
        draw_selected_tile_indicator(screen)
    
''' 
draws the squares on the game board; top left square is always light
'''
def draw_board_tiles(screen):
    if chess_set == 1: # chess set 1
        tile_color1 = 'white'
        tile_color2 = 'grey'
    elif chess_set == 2: # chess set 2
        tile_color1 = pygame.Color(255,228,196)
        tile_color2 = pygame.Color(210,105,30)
    else: # chess set 3
        tile_color1 = 'white'
        tile_color2 = 'black'

    tile_colors = [pygame.Color(tile_color1), pygame.Color(tile_color2)]

    # colors the tiles onto the game board
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = tile_colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect((col * TILE_SIZE) + game_board_starting_x_coordinate, (row * TILE_SIZE) + game_board_starting_y_coordinate, TILE_SIZE, TILE_SIZE))

'''
draw pieces on top of the board
'''
def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--": # if not an empty tile; has a piece on the tile 
                screen.blit(PIECE_IMAGES[piece], pygame.Rect((col * TILE_SIZE) + game_board_starting_x_coordinate, (row * TILE_SIZE) + game_board_starting_y_coordinate, TILE_SIZE, TILE_SIZE))

'''
indicates a highlighted tile
'''
def draw_selected_tile_indicator(screen):
    line_thickness = 2 # border thickness of highlighted tile
    pygame.draw.line(screen, highlighted_tile_color, (left_x_loc, top_y_loc), (right_x_loc, top_y_loc), line_thickness) # top line
    pygame.draw.line(screen, highlighted_tile_color, (left_x_loc, bottom_y_loc), (right_x_loc, bottom_y_loc), line_thickness) # bottom line
    pygame.draw.line(screen, highlighted_tile_color, (left_x_loc, top_y_loc), (left_x_loc, bottom_y_loc), line_thickness) # left line
    pygame.draw.line(screen, highlighted_tile_color, (right_x_loc, top_y_loc), (right_x_loc, bottom_y_loc), line_thickness) # right line

'''
creates 3 buttons for the different themes (chess sets)
'''
def create_theme_buttons(screen):
    # * theme one button
    color1 = pygame.Color(105,105,105)
    color2 = pygame.Color(36, 15, 15)  
    pygame.draw.rect(screen, color1, pygame.Rect((heading_width / 2) - (heading_button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 2), heading_button_width, heading_button_height))
    pygame.draw.rect(screen, color2, pygame.Rect((heading_width / 2) + (heading_button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 2), heading_button_width, heading_button_height))

    # * theme two button
    color1 = pygame.Color(222,184,135)
    color2 = pygame.Color(210,105,30)  
    pygame.draw.rect(screen, color1, pygame.Rect((heading_width / 2) - (heading_button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3), heading_button_width, heading_button_height))
    pygame.draw.rect(screen, color2, pygame.Rect((heading_width / 2) + (heading_button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3), heading_button_width, heading_button_height))

    # * theme three button 
    color1 = 'light grey'
    color2 = pygame.Color(36, 15, 15)    
    pygame.draw.rect(screen, color1, pygame.Rect((heading_width / 2) - (heading_button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 4), heading_button_width, heading_button_height))
    pygame.draw.rect(screen, color2, pygame.Rect((heading_width / 2) + (heading_button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 4), heading_button_width, heading_button_height))

    pygame.display.update()

'''
display game log in panel 
'''
def display_game_log(screen):
    # colors over the previous heading with a new blank template
    pygame.draw.rect(screen, heading_background_color, pygame.Rect(log_frame_starting_x_coordinate, log_frame_starting_y_coordinate, log_frame_width, log_frame_height))

    # places most recent moves in the begining of the list
    game_log_rev_order = game_log.copy()
    game_log_rev_order.reverse()
    
    heading_font = pygame.font.SysFont('monospace', 16) # sets the font style and size of game log content
    
    # displays moves within the game log section; more recent moves placed above previous moves
    for move in range(len(game_log_rev_order)):
        alpha = 255 # determines the transparency of the logged move 

        # x, y coordinates of the log geting made
        y_location = log_frame_starting_y_coordinate + GAP + (move * GAP)
        x_location = log_frame_starting_x_coordinate + (log_frame_width / 2) 

        # creates the label for the move to be logged
        log_move = heading_font.render(game_log_rev_order[move], True, font_color)
        log_move_rect = log_move.get_rect(center=(x_location, y_location))

        # have logged items fade out if running out of space at the bottom of the frame
        if y_location <= WINDOW_HEIGHT - (GAP * 12): 
            screen.blit(log_move, log_move_rect)
        elif y_location > WINDOW_HEIGHT - (GAP * 12) and y_location <= WINDOW_HEIGHT - (GAP * 11):
            alpha = alpha * 0.85
        elif y_location > WINDOW_HEIGHT - (GAP * 11) and y_location <= WINDOW_HEIGHT - (GAP * 10):
            alpha = alpha * 0.7
        elif y_location > WINDOW_HEIGHT - (GAP * 10) and y_location <= WINDOW_HEIGHT - (GAP * 9):
            alpha = alpha * 0.55
        elif y_location > WINDOW_HEIGHT - (GAP * 9) and y_location <= WINDOW_HEIGHT - (GAP * 8):
            alpha = alpha * 0.4
        elif y_location > WINDOW_HEIGHT - (GAP * 8) and y_location <= WINDOW_HEIGHT - (GAP * 7):
            alpha = alpha * 0.25
        elif y_location > WINDOW_HEIGHT - (GAP * 7) and y_location <= WINDOW_HEIGHT - (GAP * 6):
            alpha = alpha * 0.12
        else:
            break

        log_move.set_alpha(alpha)
        screen.blit(log_move, log_move_rect)

'''
creates the help, settings, valid moves, and en passant buttons
'''
def create_game_buttons(screen):
    if chess_set == 1: # if chess set 1
        set_folder = "Set1"
    elif chess_set == 2: # else if chess set 2
        set_folder = "Set2"
    else: # else chess set 3
        set_folder = "Set3"

    # * help button
    x_corner_first_button_loc = corner_section_starting_x
    y_corner_button_loc = corner_section_starting_y
    pygame.draw.rect(screen, heading_background_color, pygame.Rect(x_corner_first_button_loc, y_corner_button_loc, corner_button_dimensions, corner_button_dimensions)) # background
    
    # symbol on the button
    if not is_script: # used for running Display.py directly from VS
        base_path = os.path.dirname(__file__) # finds absolute path for the project
        image_path = os.path.join(base_path, "Game_Images", set_folder, "Icon_Symbols", "help_button.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions, logo_dimensions))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), y_corner_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), corner_button_dimensions, corner_button_dimensions)) 
    else: # used when running program as a script
        image_path = os.path.join("Game_Images", set_folder, "Icon_Symbols", "help_button.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions, logo_dimensions))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), y_corner_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), corner_button_dimensions, corner_button_dimensions)) 
        
     # * settings button
    pygame.draw.rect(screen, heading_background_color, pygame.Rect(corner_section_starting_x + corner_button_dimensions + button_spacing_x, corner_section_starting_y, corner_button_dimensions, corner_button_dimensions)) # background
    
    # symbol
    if not is_script: # used for running Display.py directly from VS
        base_path = os.path.dirname(__file__) # finds absolute path for the project
        image_path = os.path.join(base_path, "Game_Images", set_folder, "Icon_Symbols", "stopwatch_button.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions, logo_dimensions))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions) / 2) + corner_button_dimensions + button_spacing_x, y_corner_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), corner_button_dimensions, corner_button_dimensions)) 
    else: # used when running program as a script
        image_path = os.path.join("Game_Images", set_folder, "Icon_Symbols", "stopwatch_button.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions, logo_dimensions))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions) / 2) + corner_button_dimensions + button_spacing_x, y_corner_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), corner_button_dimensions, corner_button_dimensions)) 

     # * valid moves button
    pygame.draw.rect(screen, heading_background_color, pygame.Rect(corner_section_starting_x + (corner_button_dimensions * 2) + (button_spacing_x * 2), corner_section_starting_y, corner_button_dimensions, corner_button_dimensions)) # background
    
    # symbol
    if not is_script: # used for running Display.py directly from VS
        base_path = os.path.dirname(__file__) # finds absolute path for the project
        image_path = os.path.join(base_path, "Game_Images", set_folder, "Icon_Symbols", "valid_moves_button.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions, logo_dimensions))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions) / 2) + (corner_button_dimensions * 2) + (button_spacing_x * 2), y_corner_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), corner_button_dimensions, corner_button_dimensions)) 
    else: # used when running program as a script
        image_path = os.path.join("Game_Images", set_folder, "Icon_Symbols", "valid_moves_button.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions, logo_dimensions))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions) / 2) + (corner_button_dimensions * 2) + (button_spacing_x * 2), y_corner_button_loc + ((corner_button_dimensions - logo_dimensions) / 2), corner_button_dimensions, corner_button_dimensions)) 

     # * en passant button
    pygame.draw.rect(screen, heading_background_color, pygame.Rect(corner_section_starting_x + (corner_button_dimensions * 3) + (button_spacing_x * 3), corner_section_starting_y, corner_button_dimensions, corner_button_dimensions)) # background
    
    # symbol
    if not is_script: # used for running Display.py directly from VS
        base_path = os.path.dirname(__file__) # finds absolute path for the project
        image_path = os.path.join(base_path, "Game_Images", set_folder, "black_pawn.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions + 10, logo_dimensions + 10))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions - 10) / 2) + (corner_button_dimensions * 3) + (button_spacing_x * 3), y_corner_button_loc + ((corner_button_dimensions - logo_dimensions - 10) / 2), corner_button_dimensions, corner_button_dimensions)) 
    else: # used when running program as a script
        image_path = os.path.join("Game_Images", set_folder, "black_pawn.png")
        help_button = pygame.transform.scale(pygame.image.load(image_path), (logo_dimensions + 10, logo_dimensions + 10))
        screen.blit(help_button, pygame.Rect(x_corner_first_button_loc + ((corner_button_dimensions - logo_dimensions - 10) / 2) + (corner_button_dimensions * 3) + (button_spacing_x * 3), y_corner_button_loc + ((corner_button_dimensions - logo_dimensions - 10) / 2), corner_button_dimensions, corner_button_dimensions)) 

'''
handles actions when help button is pressed
'''
def help_button_active(): # TODO
    print("got to help button")

'''
handles actions when settings button is pressed
'''
def settings_button_active(): # TODO
    print("got to settings button")

'''
handles actions when valid moves button is pressed
'''
def valid_moves_button_active(): # TODO
    print("got to valid moves button")

'''
handles actions when en passant button is pressed
'''
def en_passant_button_active(): # TODO
    print("got to en passant button")

# convension for calling the main function; useful for running as a script
if __name__ == "__main__":
    main()