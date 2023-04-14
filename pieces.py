import pygame

class Piece:
    def __init__(self, row, col, color, img, square_size):
        self.row = row
        self.col = col
        self.color = color
        self.img = img
        self.selected = False
        self.square_size = square_size

    def draw(self, screen):
        rect = pygame.Rect(self.col * self.square_size, self.row * self.square_size, self.square_size, self.square_size)
        if self.selected:
            pygame.draw.rect(screen, (0, 255, 0), rect, 2)
        screen.blit(self.img, rect)

    def move(self, row, col):
        self.row = row
        self.col = col

    def is_valid_move(self, board, end_row, end_col):
        raise NotImplementedError("Subclasses must implement this method")

class Pawn(Piece):
    def __init__(self, row, col, color, img, square_size):
        super().__init__(row, col, color, img, square_size)
        self.first_move = True
    
    def move(self, row, col):
        super().move(row, col)
        self.first_move = False
    
    def is_valid_move(self, board, end_row, end_col):
        row_diff = abs(self.row - end_row)
        col_diff = abs(self.col - end_col)

        if self.color == "white":
            direction = -1
        else:
            direction = 1
        
        # One square forward move
        if row_diff == 1 and col_diff == 0 and self.row + direction == end_row and board[end_row][end_col] is None:
            return True
        
         # Two squares forward (only allowed if it's the pawn's first move)
        if self.first_move and row_diff == 2 and col_diff == 0 and self.row + 2 * direction == end_row and board[end_row][end_col] is None and board[self.row + direction][self.col] is None:
            return True
        
        # Capture diagonally
        if row_diff == 1 and col_diff == 1 and self.row + direction == end_row and board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
            return True
        
        return False

class Rook(Piece):
    def __init__(self, row, col, color, img, square_size):
        super().__init__(row, col, color, img, square_size)

    def is_valid_move(self, board, end_row, end_col):
        row_diff = abs(end_row - self.row)
        col_diff = abs(end_col - self.col)

        # Check if the move is horizontal or vertical
        if row_diff == 0 or col_diff == 0:
            row_step = 0 if row_diff == 0 else (end_row - self.row) // row_diff
            col_step = 0 if col_diff == 0 else (end_col - self.col) // col_diff

            row, col = self.row + row_step, self.col + col_step

            # Check if the path between the starting and ending positions is clear
            while row != end_row or col != end_col:
                if board[row][col] is not None:
                    return False
                row += row_step
                col += col_step

            # Check if the target square is empty or has an opponent's piece
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True

        return False

class Knight(Piece):
    def __init__(self, row, col, color, img, square_size):
        super().__init__(row, col, color, img, square_size)

    def is_valid_move(self, board, end_row, end_col):
        row_diff = abs(end_row - self.row)
        col_diff = abs(end_col - self.col)

        # Check if the move is an L-shape (2 steps in one direction and 1 step in the other)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target_piece = board[end_row][end_col]

            # Check if the target square is empty or has an opponent's piece
            if target_piece is None or target_piece.color != self.color:
                return True

        return False

class Bishop(Piece):
    def __init__(self, row, col, color, img, square_size):
        super().__init__(row, col, color, img, square_size)
    
    def is_valid_move(self, board, end_row, end_col):
        row_diff = abs(end_row - self.row)
        col_diff = abs(end_col - self.col)

        # Checks if move is diagonal
        if row_diff == col_diff:
            row_step = (end_row - self.row) // row_diff
            col_step = (end_col - self.col) // col_diff

            row, col = self.row + row_step, self.col + col_step

            # Check if the path between the starting and ending positions is clear
            while row != end_row or col != end_col:
                if board[row][col] is not None:
                    return False
                row += row_step
                col += col_step

            # Check if the target square is empty or has an opponent's piece
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True

        return False

class Queen(Piece):
    def __init__(self, row, col, color, img, square_size):
        super().__init__(row, col, color, img, square_size)
    
    def is_valid_move(self, board, end_row, end_col):
        row_diff = abs(end_row - self.row)
        col_diff = abs(end_col - self.col)

        # Check if it is diagonal, horizontal, or vertical
        if (row_diff == col_diff) or row_diff == 0 or col_diff == 0:
            if row_diff == col_diff:
                row_step = (end_row - self.row) // row_diff
                col_step = (end_col - self.col) // col_diff
                row, col = self.row + row_step, self.col + col_step
            elif self.row == end_row:
                row_step = 0
                col_step = (end_col - self.col) // col_diff
                row, col = self.row, self.col + col_step
            else:
                row_step = (end_row - self.row) // row_diff
                col_step = 0
                row, col = self.row + row_step, self.col

            # Check if the path between the starting and ending positions is clear
            while row != end_row or col != end_col:
                if board[row][col] is not None:
                    return False
                row += row_step
                col += col_step

            # Check if the target square is empty or has an opponent's piece
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True

        return False

class King(Piece):
    def __init__(self, row, col, color, img, square_size):
        super().__init__(row, col, color, img, square_size)
    
    def is_valid_move(self, board, end_row, end_col):
        row_diff = abs(end_row - self.row)
        col_diff = abs(end_col - self.col)

        #checks if move is only one square away
        if row_diff <= 1 and col_diff <= 1:
            # Check if the target square is empty or has an opponent's piece
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True

        return False