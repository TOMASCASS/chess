import pygame
import os
from pieces import Piece

# Initialize Pygame
pygame.init()

# Chessboard and window settings
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // 8

# Colors
BEIGE = (232, 220, 202)
BROWN = (166, 124, 91)

def load_pieces():
    pieces = {}
    for piece in os.listdir('pieces'):
        img = pygame.image.load(os.path.join('pieces', piece))
        pieces[piece.split('.')[0]] = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
    return pieces

def create_board(pieces):
    board = [[None for _ in range(COLS)] for _ in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):
            if row == 0 or row == 7:
                if col in (0, 7):
                    piece_name = 'white_rook' if row == 7 else 'black_rook'
                elif col in (1, 6):
                    piece_name = 'white_knight' if row == 7 else 'black_knight'
                elif col in (2, 5):
                    piece_name = 'white_bishop' if row == 7 else 'black_bishop'
                elif col == 3:
                    piece_name = 'white_queen' if row == 7 else 'black_queen'
                elif col == 4:
                    piece_name = 'white_king' if row == 7 else 'black_king'
                color = 'white' if row == 7 else 'black'
                board[row][col] = Piece(row, col, color, pieces[piece_name], SQUARE_SIZE)
            elif row == 1:
                board[row][col] = Piece(row, col, 'black', pieces['black_pawn'], SQUARE_SIZE)
            elif row == 6:
                board[row][col] = Piece(row, col, 'white', pieces['white_pawn'], SQUARE_SIZE)
    return board

def draw_board(screen, board):
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, BEIGE if (row + col) % 2 == 0 else BROWN, rect)
            piece = board[row][col]
            if piece:
                piece.draw(screen)

def get_clicked_position(pos):
    x, y = pos
    row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
    return row, col

