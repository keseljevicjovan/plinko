import pygame
import sys
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 1280, 720
RATIO = WIDTH / 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plinko Game")

# Colors
BACKGROUND = (15, 33, 47)
WHITE = (255, 255, 255)
GREEN = (34, 200, 34)
RED = (250, 1, 62)

# Pin settings
PIN_RADIUS = int(5 * RATIO)
PIN_SPACING = int(40 * RATIO)
PIN_ROWS = 16
PIN_START = 50
pins = []

# Bin settings
BIN_COUNT = 10
BIN_HEIGHT = int(60 * RATIO)
BIN_WIDTH = WIDTH // BIN_COUNT
BIN_LABELS = [round(i * 0.2, 1) for i in range(BIN_COUNT)]

def create_pins():
    pins.clear()
    for row in range(1, PIN_ROWS + 1):
        row_offset = PIN_SPACING // 2 if row % 2 == 0 else 0
        for col in range(-(row // 2) - 1, (row - 1) // 2 + 2):
            x = WIDTH // 2 + col * PIN_SPACING + row_offset
            y = row * PIN_SPACING + PIN_START
            pins.append((x, y))

def draw_pins():
    for pin in pins:
        pygame.draw.circle(screen, WHITE, pin, PIN_RADIUS)

#def draw_bins(): 

def main():
    create_pins()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND)

        draw_pins()
#        draw_bins()

        pygame.display.flip()

if __name__ == "__main__":
    main()
