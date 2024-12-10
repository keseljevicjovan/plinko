import pygame
from settings import WIDTH, RATIO

PIN_RADIUS = int(5 * RATIO)
PIN_SPACING = int(40 * RATIO)
PIN_ROWS = 16
PIN_START = 50
pins = []

def create_pins():
    pins.clear()
    for row in range(1, PIN_ROWS + 1):
        row_offset = PIN_SPACING // 2 if row % 2 == 0 else 0
        for col in range(-(row // 2) - 1, (row - 1) // 2 + 2):
            x = WIDTH // 2 + col * PIN_SPACING + row_offset
            y = row * PIN_SPACING + PIN_START
            pins.append((x, y))

def draw_pins(screen):
    for pin in pins:
        pygame.draw.circle(screen, (255, 255, 255), pin, PIN_RADIUS)
