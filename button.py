import pygame

class Button:
    def __init__(self, x, y, width, height, text, on_click):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.on_click = on_click
        self.default_color = (34, 139, 34)
        self.hover_color = (50, 205, 50)
        self.clicked_color = (144, 238, 144)
        self.current_color = self.default_color
        self.font = pygame.font.Font(None, 36)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.current_color = self.clicked_color
            self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and self.clicked:
            if self.rect.collidepoint(event.pos):
                self.on_click()
            self.current_color = self.default_color
            self.clicked = False
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_color = self.hover_color
        else:
            self.current_color = self.default_color
