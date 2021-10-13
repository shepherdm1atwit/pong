import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Lab2")

    WIDTH = 800
    HEIGHT = 480
    BORDER = 20

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    wcolor = pygame.Color("white")

    screen.fill([0, 0, 0])

    # top
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    # left
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    # right
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()