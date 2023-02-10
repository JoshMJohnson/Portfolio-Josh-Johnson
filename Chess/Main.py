'''
Driver file

Loads up a chess board showing the user, and handles user input

Created By: Josh Johnson
'''

# pre-made classes
import random # implements pseudo-random number generators for various distributions
import pygame
from os import path # used to get relative path for the project

# build classes
import BoardState

# creating the game board
WIDTH = 400 # game board width
HEIGHT = 400 # game board height
DIMENSION = 8 # 8x8 board
TILE_SIZE = WIDTH // DIMENSION # size of a square (tile) on the gui

MAX_FPS = 15 # for animations
IMAGES = {}

# global dictionary of images
def load_images(set):
    # finds relative path for the project
    base_path = path.dirname(__file__)

    # determines the piece set
    piece_set = ""
    if set == 1:
        piece_set = "Set1"
    elif set == 2:
        piece_set = "Set2"
    else:
        piece_set = "Set1"

    # loads the piece set
    pieces = ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook", "black_pawn"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(base_path + "/Game_Images/Piece_Sets/" + piece_set + "/" + piece + ".png"), (TILE_SIZE, TILE_SIZE))
    
# main function; driver for the code
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    board_state = BoardState.BoardState()
    print(board_state.board)
    load_images(1)
    running = True

    while running:
        # quit application
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        # drawGameState(screen, board_state) TODO
        clock.tick(MAX_FPS)
        pygame.display.flip()

# def drawGameState(screen, board_state): TODO


# convension for calling the main function; useful for running as a script
if __name__ == "__main__":
    main()