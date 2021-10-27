from paddle import Paddle
from ball import Ball
import pygame



import random

def main():
    pygame.init()
    pygame.display.set_caption("Lab2")

    WIDTH = 800
    HEIGHT = 480
    BORDER = 20
    VELOCITY = 1

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    color = pygame.Color("white")
    bgcolor = pygame.Color("black")

    screen.fill([0, 0, 0])

    # top
    topwall = pygame.Rect((0, 0), (WIDTH, BORDER))
    pygame.draw.rect(screen, color, topwall)
    # left
    leftwall = pygame.Rect((0, 0), (BORDER, HEIGHT))
    pygame.draw.rect(screen, color, leftwall)
    # bottom
    bottomwall = pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER))
    pygame.draw.rect(screen, color, bottomwall)

    # ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    vy0 = VELOCITY

    b0 = Ball(x0, y0, vx0, vy0, screen, color, bgcolor)
    b0.show(color)

    pygame.display.update()

    running = True
    while running:
        # ball movement
        pygame.display.update()
        if topwall.collidepoint(b0.x+b0.vx,b0.y-8+b0.vy):
            b0.vy = b0.vy * (-1)
        elif bottomwall.collidepoint(b0.x+b0.vx,b0.y+8+b0.vy):
            b0.vy = b0.vy * (-1)
        elif leftwall.collidepoint(b0.x-8+b0.vx,b0.y+b0.vy):
            b0.vx = b0.vx * (-1)
        b0.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




if __name__ == "__main__":
    main()