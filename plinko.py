import pygame
import sys
import io
import random

pygame.init()

# Resolution
width, height = 1280, 720
ratio = width / 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Plinko")

# Pins
pins = []
pin_radius = int(5 * ratio)
pin_spacing = int(40 * ratio)
pin_rows = 16
pin_start = 0

# Balls
ball_radius = int(9 * ratio) 
balls = []
del_balls_x = []
fall_speed_increment = 0.6 * ratio
balls_at_once = 1

def create_pins():
    pins.clear()
    offset = pin_spacing // 2
    for row in range(1, pin_rows + 1):
        row_offset = offset if row % 2 == 0 else 0
        for col in range(-(row// 2) - 1, (row - 1) // 2 + 2):
            x = width // 2 + col * pin_spacing + row_offset
            y = row * pin_spacing + pin_start
            pins.append((x, y))

if __name__ == '__main__':
    create_pins()
