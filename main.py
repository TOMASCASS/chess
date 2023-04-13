import pygame
from chessboard import WIDTH, HEIGHT, load_pieces,draw_board, create_board, get_clicked_position
from pieces import Piece




screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")
clock = pygame.time.Clock()
pieces = load_pieces()
board = create_board(pieces)

selected_piece = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_position(pos)
            clicked_piece = board[row][col]

            if not selected_piece:
                if clicked_piece:
                    selected_piece = clicked_piece
                    selected_piece.selected = True
            else:
                if clicked_piece == selected_piece:
                    selected_piece.selected = False
                    selected_piece = None
                else:
                    old_row, old_col = selected_piece.row, selected_piece.col
                    selected_piece.move(row, col)
                    board[row][col] = selected_piece
                    board[old_row][old_col] = None
                    selected_piece.selected = False
                    selected_piece = None

    draw_board(screen, board)
    pygame.display.update()
    clock.tick(60)

pygame.quit()