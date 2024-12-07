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
BLACK = (0, 0, 0)
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
BIN_TEXTS = ['1000', '130', '26x', '9x', '4x', '2x', '0.2x', '0.2x', '0.2x','0.2x','0.2x','2x','4x','9x','26x', '130', '1000']
hit_bins = []  # List to store hit bins

# Fonts for the headers
font = 'Gill Sans'
header0 = pygame.font.SysFont(font, int(24 * RATIO), True)
header1 = pygame.font.SysFont(font, int(22 * RATIO), True)
header2 = pygame.font.SysFont(font, int(14 * RATIO), True)
header_money = pygame.font.SysFont(font, int(36 * RATIO), True)

# Define other variables for bin rendering
bin_width = BIN_WIDTH // 2  # Adjusted width of the bins

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

def create_bin_text_surfaces():
    bin_text_surfaces = []
    texts = BIN_TEXTS
    if PIN_ROWS < 10:  # Assuming this is for some special case
        texts = BIN_TEXTS  # You might want to define low_bin_texts elsewhere
    for text in texts:
        rendered_text = header2.render(text, True, BLACK)
        bin_text_surfaces.append(rendered_text)
    return bin_text_surfaces

def draw_rounded_rect(surface, rect, color, radius, border_radius=0):
    """Draws a rounded rectangle."""
    pygame.draw.rect(surface, color, rect, border_radius)

def render_bins():
    global hit_bins
    bin_text_surfaces = create_bin_text_surfaces()
    click_offset = 4 * RATIO
    bin_start_offset = WIDTH // 2 - (PIN_ROWS // 2 + 0.5) * PIN_SPACING
    base_y = PIN_ROWS * PIN_SPACING + PIN_START + PIN_SPACING // 2
    for bin in range(PIN_ROWS + 1):
        animate = True if bin in hit_bins else False  # if hit

        offset_x = bin * PIN_SPACING + (not PIN_ROWS % 2) * PIN_SPACING // 2
        index = bin + 8 - PIN_ROWS // 2
        if PIN_ROWS % 2 and bin <= PIN_ROWS // 2:
            index -= 1

        bin_text_surface = bin_text_surfaces[index]

        base_x = bin_start_offset - bin_width // 2 + offset_x

        if animate:
            # Configure Rects for drawing  
            light_rect_right = pygame.Rect(base_x, base_y + click_offset, bin_width, bin_width)
            text_rect = bin_text_surface.get_rect(center=(base_x + bin_width // 2, base_y + bin_width // 2 + click_offset))

            # Remove animated bin
            hit_bins = list(filter(lambda x: x != bin, hit_bins))
        else:
            # Configure Rects for drawing  
            dark_rect_right = pygame.Rect(base_x, base_y + click_offset, bin_width, bin_width)       
            light_rect_right = pygame.Rect(base_x, base_y, bin_width, bin_width)
            text_rect = bin_text_surface.get_rect(center=(base_x + bin_width // 2, base_y + bin_width // 2))

            # Draw dark rectangle
            draw_rounded_rect(screen, dark_rect_right, GREEN, int(4 * RATIO) + (RATIO > 1))

        # Draw light rectangle and text
        draw_rounded_rect(screen, light_rect_right, GREEN, int(4 * RATIO) + (RATIO > 1))
        screen.blit(bin_text_surface, text_rect)

def draw_bins(): 
    render_bins()

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
        draw_bins()

        pygame.display.flip()

if __name__ == "__main__":
    main()

