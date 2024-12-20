import pygame
import sys
from settings import WIDTH, HEIGHT, BACKGROUND, MAX_FPS
from pins import create_pins, draw_pins
from bins import draw_bins
from balls import create_ball, update_balls, render_balls
from button import Button

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Plinko Game")

    create_pins()
    clock = pygame.time.Clock()

    button = Button(
        x=20, 
        y=HEIGHT - 70, 
        width=100, 
        height=50, 
        text="Bet", 
        on_click=create_ball
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    create_ball()

            button.handle_event(event)

        update_balls()
        screen.fill(BACKGROUND)
        draw_pins(screen)
        draw_bins(screen)
        render_balls(screen)
        button.draw(screen)

        pygame.display.flip()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main()
