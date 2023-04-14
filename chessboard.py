import pygame
import os
from pieces import King, Pawn, Rook, Knight, Bishop, Queen

# Initialize Pygame
pygame.init()

# Chessboard and window settings
ROWS, COLS = 8, 8
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
FLIPPED_BOARD = False

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
                    color = 'white' if row == 7 else 'black'
                    piece_name = f'{color}_rook'
                    board[row][col] = Rook(row, col, color, pieces[piece_name], SQUARE_SIZE)
                elif col in (1, 6):
                    color = 'white' if row == 7 else 'black'
                    piece_name = f'{color}_knight'
                    board[row][col] = Knight(row, col, color, pieces[piece_name], SQUARE_SIZE)
                elif col in (2, 5):
                    color = "white" if row == 7 else "black"
                    piece_name = f'{color}_bishop'
                    board[row][col] = Bishop(row, col, color, pieces[piece_name], SQUARE_SIZE)
                elif col == 3:
                    color = "white" if row == 7 else "black"
                    piece_name = f'{color}_queen'
                    board[row][col] = Queen(row, col, color, pieces[piece_name], SQUARE_SIZE)
                elif col == 4:
                    color = 'white' if row == 7 else 'black'
                    piece_name = f'{color}_king'
                    board[row][col] = King(row, col, color, pieces[piece_name], SQUARE_SIZE)
            elif row == 1:
                board[row][col] = Pawn(row, col, 'black', pieces['black_pawn'], SQUARE_SIZE)
            elif row == 6:
                board[row][col] = Pawn(row, col, 'white', pieces['white_pawn'], SQUARE_SIZE)
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
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    if FLIPPED_BOARD:
        row = ROWS - 1 - row
        col = COLS - 1 - col
    return row, col

