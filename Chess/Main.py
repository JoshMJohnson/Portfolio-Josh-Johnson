'''
Driver file

Loads up a chess board to display for the user, and handles user input

Created By: Josh Johnson
'''

# python libraries
import random # implements pseudo-random number generators for various distributions
import pygame # gui for python game
from os import path # used to get absolute path for the project

# project classes
import GameState
import Moves
import Player

# game board settings
BOARD_WIDTH = 400 # game board width
BOARD_HEIGHT = 400 # game board height
DIMENSION = 8 # 8x8 board
TILE_SIZE = BOARD_WIDTH // DIMENSION # size of a square (tile) on the gui
MAX_FPS = 15 # for animations
PIECE_IMAGES = {} # global dictionary of chess piece images
chess_set = 1 # indicates which chess set to use; default is set 1

# window settings
WINDOW_WIDTH = BOARD_WIDTH + 300
WINDOW_HEIGHT = BOARD_HEIGHT + 200
GAP = 25 # spacing the board is from the edge of the window

# game log settings
log_frame_width = WINDOW_WIDTH - BOARD_WIDTH - GAP - (GAP * 2)
log_frame_height = WINDOW_HEIGHT - (GAP * 2)
log_frame_starting_x_coordinate = BOARD_WIDTH + GAP + GAP
log_frame_starting_y_coordinate = GAP
game_log = []

# heading panel settings
heading_width = BOARD_WIDTH
heading_height = WINDOW_HEIGHT - BOARD_HEIGHT - (GAP * 3)
heading_starting_x_coordinate = GAP
heading_starting_y_coordinate = GAP
font_color = '' # color of the font; initialized as the color 'black'
heading_background_color = '' # heading background color; initialized as the color 'white'

# buttons in heading
button_width = 8
button_height = 16

# initialize players
player_one = Player.Player(1)
player_two = Player.Player(2)    

'''
loads the desired chess set
'''
def load_chess_set(screen):
    global font_color
    global heading_background_color

    if chess_set == 1: # chess set 1
        piece_set = "Set1"
        background_color = 'light grey'
        heading_background_color = 'white'
        font_color = 'black'
        game_log_background_color = 'white'
    elif chess_set == 2: # chess set 2
        piece_set = "Set2"
        background_color = pygame.Color(222,184,135)
        heading_background_color = pygame.Color(255,228,196)
        font_color = pygame.Color(139,69,19)
        game_log_background_color = heading_background_color
    else: # chess set 3
        piece_set = "Set3"
        background_color = pygame.Color(51,51,51)
        heading_background_color = 'black'
        font_color = 'white'
        game_log_background_color = heading_background_color

    # * load chess pieces
    base_path = path.dirname(__file__) # finds absolute path for the project

    pieces = ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook", "black_pawn",
                "white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook", "white_pawn"]
    
    for piece in pieces:
        PIECE_IMAGES[piece] = pygame.transform.scale(pygame.image.load(base_path + "/Game_Images/Piece_Sets/" + piece_set + "/" + piece + ".png"), (TILE_SIZE, TILE_SIZE))

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
    # * initialize game
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Lets Play Chess!")
            
    # display game board with initial set theme
    run_game(screen, clock)

'''
loads the game with the chess set theme and runs the game
'''
def run_game(screen, clock):
    global chess_set
    global game_log

    game_state = GameState.GameState()
    load_chess_set(screen) 
    display_player_values(screen)
    create_theme_buttons(screen)

    tile_selected = () # keeps track of the last tile clicked by the user
    player_clickes = [] # keeps track of a plyaer clicks; two tuples: [(x1,y1), (x2,y2)]

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
                        player_clickes == [] # clear player clicks
                    else: # else; 2 different tiles clicked in order
                        tile_selected = (row, col)
                        player_clickes.append(tile_selected)
                    
                    if len(player_clickes) == 2: # if second tile was clicked that was different than the first
                        move = Moves.Moves(player_clickes[0], player_clickes[1], game_state.board)
                        print(move.get_chess_notation()) # ! used for testing purposes
                        game_state.make_move(move)
                        game_log.append(move.get_chess_notation())

                        # update player points and switches current player
                        if player_one.current_player:
                            update_player_points(screen, player_one)
                            player_one.current_player = False
                            player_two.current_player = True
                        else:
                            update_player_points(screen, player_two)
                            player_one.current_player = True
                            player_two.current_player = False

                        # displays move within the move log on the window
                        display_game_log(screen)

                        # resets user input clicks
                        tile_selected = () 
                        player_clickes = []    
                elif ((location[0] >= (heading_width / 2) - (button_width / 2) + GAP) and (location[0] <= (heading_width / 2) + (button_width / 2) + button_width + GAP) 
                        and (location[1] >= heading_starting_y_coordinate + (GAP * 2)) and (location[1] <= heading_starting_y_coordinate + (GAP * 2) + button_height)): # else if theme 1 is selected
                    chess_set = 1
                    game_log = []
                    open_theme()
                elif ((location[0] >= (heading_width / 2) - (button_width / 2) + GAP) and (location[0] <= (heading_width / 2) + (button_width / 2) + button_width + GAP) 
                        and (location[1] >= heading_starting_y_coordinate + (GAP * 3)) and (location[1] <= heading_starting_y_coordinate + (GAP * 3) + button_height)): # else if theme 2 is selected
                    chess_set = 2
                    game_log = []
                    open_theme()                    
                elif ((location[0] >= (heading_width / 2) - (button_width / 2) + GAP) and (location[0] <= (heading_width / 2) + (button_width / 2) + button_width + GAP) 
                        and (location[1] >= heading_starting_y_coordinate + (GAP * 4)) and (location[1] <= heading_starting_y_coordinate + (GAP * 4) + button_height)): # else if theme 3 is selected
                    chess_set = 3
                    game_log = []
                    open_theme()  

        draw_game_state(screen, game_state) 
        clock.tick(MAX_FPS)
        pygame.display.flip()

'''

'''
def open_theme():
    pygame.quit() # close previous window

    # * open new window with updated theme settings
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Lets Play Chess!")
    run_game(screen, clock)    

'''
updates the player points
'''
def update_player_points(screen, player):  
    heading_font = pygame.font.SysFont('monospace', 12, italic=True)

    if player.color == 'white': # player one
        # turn previous value invisible
        player_points_taken1_value_label = heading_font.render(str(39), True, heading_background_color, heading_background_color)
        player_points_taken1_value_label_rect = player_points_taken1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 3)))
        screen.blit(player_points_taken1_value_label, player_points_taken1_value_label_rect)

        # display new value of player score
        player_points_taken1_value_label = heading_font.render(str(player.points_taken), True, font_color)
        player_points_taken1_value_label_rect = player_points_taken1_value_label.get_rect(topright=(heading_starting_x_coordinate + (heading_width / 2) - GAP, heading_starting_y_coordinate + (GAP * 3)))
        screen.blit(player_points_taken1_value_label, player_points_taken1_value_label_rect)
    else: # player two 
        # turn previous value invisible
        player_points_taken2_value_label = heading_font.render(str(39), True, heading_background_color, heading_background_color)
        screen.blit(player_points_taken2_value_label, (heading_starting_x_coordinate + (heading_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3)))

        # display new value of player score
        player_points_taken2_value_label = heading_font.render(str(player.points_taken), True, font_color)
        screen.blit(player_points_taken2_value_label, (heading_starting_x_coordinate + (heading_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3)))
        
'''
updates the player game time left
'''
def update_player_game_time(): # TODO
    pass

''' 
creates all graphics of the game 
'''
def draw_game_state(screen, game_state):
    draw_board_tiles(screen) 
    draw_pieces(screen, game_state.board) 
    
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
            pygame.draw.rect(screen, color, pygame.Rect((col * TILE_SIZE) + GAP, (row * TILE_SIZE) + WINDOW_HEIGHT - BOARD_HEIGHT - GAP, TILE_SIZE, TILE_SIZE))

'''
draw pieces on top of the board
'''
def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]

            # if not an empty tile; has a piece on the tile 
            if piece != "--":
                screen.blit(PIECE_IMAGES[piece], pygame.Rect((col * TILE_SIZE) + GAP, (row * TILE_SIZE) + WINDOW_HEIGHT - BOARD_HEIGHT - GAP, TILE_SIZE, TILE_SIZE))

'''
creates 3 buttons for the different themes (chess sets)
'''
def create_theme_buttons(screen):
    # theme button one
    color1 = pygame.Color(105,105,105)
    color2 = pygame.Color(36, 15, 15)  
    pygame.draw.rect(screen, color1, pygame.Rect((heading_width / 2) - (button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 2), button_width, button_height))
    pygame.draw.rect(screen, color2, pygame.Rect((heading_width / 2) + (button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 2), button_width, button_height))

    # theme button two
    color1 = pygame.Color(222,184,135)
    color2 = pygame.Color(210,105,30)  
    pygame.draw.rect(screen, color1, pygame.Rect((heading_width / 2) - (button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3), button_width, button_height))
    pygame.draw.rect(screen, color2, pygame.Rect((heading_width / 2) + (button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 3), button_width, button_height))


    # theme button three 
    color1 = 'light grey'
    color2 = pygame.Color(36, 15, 15)    
    pygame.draw.rect(screen, color1, pygame.Rect((heading_width / 2) - (button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 4), button_width, button_height))
    pygame.draw.rect(screen, color2, pygame.Rect((heading_width / 2) + (button_width / 2) + GAP, heading_starting_y_coordinate + (GAP * 4), button_width, button_height))

    pygame.display.update()

'''
display game log in panel 
'''
def display_game_log(screen): # TODO make a scrollable game log that fades out at the bottom when out of space
    # colors over the previous heading with a new blank template
    pygame.draw.rect(screen, heading_background_color, pygame.Rect(log_frame_starting_x_coordinate, log_frame_starting_y_coordinate, log_frame_width, log_frame_height))

    # places most recent moves in the begining of the list
    game_log_rev_order = game_log.copy()
    game_log_rev_order.reverse()

    # sets the font style and size of game log content
    heading_font = pygame.font.SysFont('monospace', 16)

    # displays moves within the game log section; more recent moves placed above previous moves
    for move in range(len(game_log_rev_order)):
        # x, y coordinates of the log geting made
        y_location = log_frame_starting_y_coordinate + GAP + (move * GAP)
        x_location = log_frame_starting_x_coordinate + (log_frame_width / 2) 

        # display move in the log frame
        log_move = heading_font.render(game_log_rev_order[move], True, font_color)
        log_move_rect = log_move.get_rect(center=(x_location, y_location))
        screen.blit(log_move, log_move_rect)



# convension for calling the main function; useful for running as a script
if __name__ == "__main__":
    main()