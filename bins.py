import pygame
from settings import WIDTH, RATIO, PIN_ROWS, PIN_SPACING
from utils import create_rgb_gradient, draw_rounded_rect

# Bin settings
BIN_COUNT = PIN_ROWS + 1
BIN_HEIGHT = int(60 * RATIO)
BIN_WIDTH = WIDTH // BIN_COUNT
BIN_LABELS = [round(i * 0.2, 1) for i in range(BIN_COUNT)]
BIN_TEXTS = ['1000', '130x', '26x', '9x', '4x', '2x', '0.2x', '0.2x', '0.2x', '0.2x', '0.2x', '2x', '4x', '9x', '26x', '130x', '1000']
hit_bins = []

# Gradient
START_COLOR = (253, 0, 65)  # Red
CENTER_COLOR = (254, 190, 11)  # Yellow
END_COLOR = START_COLOR

gradient_steps = BIN_COUNT // 2
left_gradient = create_rgb_gradient(START_COLOR, CENTER_COLOR, gradient_steps + 1)
right_gradient = create_rgb_gradient(CENTER_COLOR, END_COLOR, gradient_steps + 1)[1:]
bin_colors = left_gradient + right_gradient

def create_bin_text_surfaces():
    bin_text_surfaces = []
    for text in BIN_TEXTS:
        rendered_text = pygame.font.SysFont('Gill Sans', int(14 * RATIO), True).render(text, True, (0, 0, 0))
        bin_text_surfaces.append(rendered_text)
    return bin_text_surfaces

def render_bins(screen):
    global hit_bins
    bin_text_surfaces = create_bin_text_surfaces()
    click_offset = 4 * RATIO
    bin_start_offset = WIDTH // 2 - (PIN_ROWS // 2 + 0.5) * PIN_SPACING 
    base_y = PIN_ROWS * PIN_SPACING + 50 + PIN_SPACING // 2 
    bin_width = BIN_WIDTH // 2 

    for bin in range(BIN_COUNT):
        animate = True if bin in hit_bins else False
        offset_x = bin * PIN_SPACING + (not PIN_ROWS % 2) * PIN_SPACING // 2
        index = bin + 8 - PIN_ROWS // 2
        if PIN_ROWS % 2 and bin <= PIN_ROWS // 2:
            index -= 1

        bin_text_surface = bin_text_surfaces[index]
        base_x = bin_start_offset - bin_width // 2 + offset_x
        bin_color = bin_colors[bin]

        if animate:
            light_rect_right = pygame.Rect(base_x, base_y + click_offset, bin_width, bin_width)
            text_rect = bin_text_surface.get_rect(center=(base_x + bin_width // 2, base_y + bin_width // 2 + click_offset))
            hit_bins = list(filter(lambda x: x != bin, hit_bins))
        else:
            dark_rect_right = pygame.Rect(base_x, base_y + click_offset, bin_width, bin_width)
            light_rect_right = pygame.Rect(base_x, base_y, bin_width, bin_width)
            text_rect = bin_text_surface.get_rect(center=(base_x + bin_width // 2, base_y + bin_width // 2))
            draw_rounded_rect(screen, dark_rect_right, bin_color, int(4 * RATIO) + (RATIO > 1))

        draw_rounded_rect(screen, light_rect_right, bin_color, int(4 * RATIO) + (RATIO > 1))
        screen.blit(bin_text_surface, text_rect)

def draw_bins(screen):
    render_bins(screen)
