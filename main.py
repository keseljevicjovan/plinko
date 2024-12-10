import pygame
import sys
from settings import WIDTH, HEIGHT, BACKGROUND
from pins import create_pins, draw_pins
from bins import draw_bins

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Plinko Game")

    create_pins()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND)

        draw_pins(screen)
        draw_bins(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
