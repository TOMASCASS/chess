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
