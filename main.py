import pygame
from chessboard import WIDTH, HEIGHT, load_pieces,draw_board




screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")
clock = pygame.time.Clock()
pieces = load_pieces()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board(screen, pieces)
    pygame.display.update()
    clock.tick(60)

pygame.quit()