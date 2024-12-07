import pygame
import sys
import io
import random

pygame.init()

width, height = 1280, 720
ratio = width / 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Plinko")

pins = []
pin_radius = int(5 * ratio)
pin_spacing = int(40 * ratio)
pin_rows = 16
pin_start = 0

pins.clear()
offset = pin_spacing // 2
for row in range(1, pin_rows + 1):
    row_offset = offset if row % 2 == 0 else 0
    for col in range(-(row// 2) - 1, (row - 1) // 2 + 2):
        x = width // 2 + col * pin_spacing + row_offset
        y = row * pin_spacing + pin_start
        pins.append((x, y))
