import pygame
import sys
from settings import WIDTH, HEIGHT, BACKGROUND, MAX_FPS
from pins import create_pins, draw_pins
from bins import draw_bins
from balls import create_ball, update_balls, render_balls

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Plinko Game")

    create_pins()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    create_ball()

        update_balls()

        screen.fill(BACKGROUND)
        draw_pins(screen)
        draw_bins(screen)
        render_balls(screen)

        pygame.display.flip()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main()

