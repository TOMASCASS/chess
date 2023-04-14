import pygame
from chessboard import WIDTH, HEIGHT, SQUARE_SIZE, load_pieces, create_board, draw_board, get_clicked_position

def undo_move(moves_history, board):
    if moves_history:
        last_move = moves_history.pop()
        start_row, start_col, end_row, end_col, captured_piece = last_move

        moved_piece = board[end_row][end_col]
        moved_piece.move(start_row, start_col)
        board[start_row][start_col] = moved_piece
        board[end_row][end_col] = captured_piece

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chessboard")
    clock = pygame.time.Clock()
    pieces = load_pieces()
    board = create_board(pieces)
    current_player = 'white'

    selected_piece = None
    moves_history = []

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
                    if clicked_piece and clicked_piece.color == current_player:
                        selected_piece = clicked_piece
                        selected_piece.selected = True
                else:
                    if clicked_piece == selected_piece:
                        selected_piece.selected = False
                        selected_piece = None
                    elif clicked_piece is None or clicked_piece.color != current_player:
                        if selected_piece.is_valid_move(board, row, col):
                            old_row, old_col = selected_piece.row, selected_piece.col
                            captured_piece = board[row][col]
                            selected_piece.move(row, col)
                            board[row][col] = selected_piece
                            board[old_row][old_col] = None
                            moves_history.append((old_row, old_col, row, col, captured_piece))
                            print(f"Move: ({old_row}, {old_col}) -> ({row}, {col})")
                            current_player = 'black' if current_player == 'white' else 'white'
                            selected_piece.selected = False
                            selected_piece = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    undo_move(moves_history, board)

        draw_board(screen, board)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
