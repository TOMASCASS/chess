import pygame
import os

# Initialize Pygame
pygame.init()

# Chessboard and window settings
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // 8

# Colors
WHITE = (255, 255, 255)
GREEN = (152, 188, 132)

# Load piece images
def load_pieces():
    pieces = {}
    for piece in os.listdir('pieces'):
        img = pygame.image.load(os.path.join('pieces', piece))
        pieces[piece.split('.')[0]] = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
    return pieces

def draw_board(screen, pieces):
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, WHITE if (row + col) % 2 == 0 else GREEN, rect)
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
                screen.blit(pieces[piece_name], rect)
            elif row == 1:
                screen.blit(pieces['black_pawn'], rect)
            elif row == 6:
                screen.blit(pieces['white_pawn'], rect)



