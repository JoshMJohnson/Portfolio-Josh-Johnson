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
import BoardState

# creating the game board
WIDTH = 400 # game board width
HEIGHT = 400 # game board height
DIMENSION = 8 # 8x8 board
TILE_SIZE = WIDTH // DIMENSION # size of a square (tile) on the gui
PIECE_IMAGES = {} # holds the locations of all the chess piece images
MAX_FPS = 15 # for animations

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
main function; driver for the code
'''
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    board_state = BoardState.BoardState()
    print(board_state.board)
    load_images(1) # TODO change parameter for each set chosen; 1, 2, or 3
    running = True

    # actions to perform for an active game
    while running:
        # quit application
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        drawGameState(screen, board_state) 
        clock.tick(MAX_FPS)
        pygame.display.flip()

''' 
creates all graphics of the game 
'''
def drawGameState(screen, board_state):
    drawBoard(screen) 
    drawPieces(screen, board_state.board) 

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
            pygame.draw.rect(screen, color, pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

'''
draw pieces on top of the board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]

            # if not an empty tile
            if piece != "--":
                screen.blit(PIECE_IMAGES[piece], pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

# convension for calling the main function; useful for running as a script
if __name__ == "__main__":
    main()