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

# creating the game board
WIDTH = 400 # game board width
HEIGHT = 400 # game board height
DIMENSION = 8 # 8x8 board
TILE_SIZE = WIDTH // DIMENSION # size of a square (tile) on the gui
PIECE_IMAGES = {} # holds the locations of all the chess piece images
MAX_FPS = 15 # for animations

# window settings
WINDOW_WIDTH = WIDTH + 300
WINDOW_HEIGHT = HEIGHT + 200
BOARD_GAP = 25 # spacing the board is from the edge of the window

'''
global dictionary of images
'''
def load_images(set):
    base_path = path.dirname(__file__) # finds absolute path for the project

    # determines the piece set
    piece_set = ""
    if set == 1:
        piece_set = "Set1"
    elif set == 2:
        piece_set = "Set2"
    else:
        piece_set = "Set3"

    # loads the piece set
    pieces = ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook", "black_pawn",
                "white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook", "white_pawn"]
    for piece in pieces:
        PIECE_IMAGES[piece] = pygame.transform.scale(pygame.image.load(base_path + "/Game_Images/Piece_Sets/" + piece_set + "/" + piece + ".png"), (TILE_SIZE, TILE_SIZE))

'''
main function
'''
def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("light grey"))

    # prepare game on load up of program
    game_state = GameState.GameState()
    load_images(1) # TODO change parameter for each set chosen; 1, 2, or 3
    running = True
    print(game_state.board) # ! used for testing purposes

    tile_selected = () # keeps track of the last tile clicked by the user
    player_clickes = [] # keeps track of a plyaer clicks; two tuples: [(x1,y1), (x2,y2)]

    # actions to perform for an active game
    while running:
        # quit application
        for e in pygame.event.get():
            if e.type == pygame.QUIT: # if closed the application
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN: # else if mouse has clicked and is holding the button down
                location = pygame.mouse.get_pos() # (x, y) location of the mouse; x value at index 0; y value at index 1                
                col = (location[0] - BOARD_GAP) // TILE_SIZE 
                row = (location[1] - (WINDOW_HEIGHT - HEIGHT - BOARD_GAP)) // TILE_SIZE
                                
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

                    # resets user input clicks
                    tile_selected = () 
                    player_clickes = []

        
        drawGameState(screen, game_state) 
        clock.tick(MAX_FPS)
        pygame.display.flip()

''' 
creates all graphics of the game 
'''
def drawGameState(screen, game_state):
    drawBoard(screen) 
    drawPieces(screen, game_state.board) 

''' 
draws the squares on the board; top left square is always light
'''
def drawBoard(screen):
    # chess sets
    colors = [pygame.Color("white"), pygame.Color("grey")] # set 1
    # TODO set 2
    # TODO set 3

    # colors the tiles
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect((col * TILE_SIZE) + 25, (row * TILE_SIZE) + WINDOW_HEIGHT - HEIGHT - 25, TILE_SIZE, TILE_SIZE))

'''
draw pieces on top of the board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]

            # if not an empty tile; has a piece on the tile 
            if piece != "--":
                screen.blit(PIECE_IMAGES[piece], pygame.Rect((col * TILE_SIZE) + 25, (row * TILE_SIZE) + WINDOW_HEIGHT - HEIGHT - 25, TILE_SIZE, TILE_SIZE))

# convension for calling the main function; useful for running as a script
if __name__ == "__main__":
    main()