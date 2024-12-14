import pygame
import random
from settings import WIDTH, HEIGHT, RATIO, PIN_SPACING, PIN_RADIUS
from pins import pins

BALL_RADIUS = int(7 * RATIO)
BALL_COLOR = (255, 255, 255)
BALL_GRAVITY = 0.3
BALL_FRICTION = 1
MAX_BALLS = 20
BOUNCE_REDUCTION = 0.6
CENTER_PULL = 0.02

balls = []

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2) * RATIO
        self.vy = 0

    def update(self):
        self.vy += BALL_GRAVITY
        self.x += self.vx
        self.y += self.vy
        for pin in pins:
            if self.collides_with_pin(pin):
                self.handle_pin_collision(pin)
        self.vx *= BALL_FRICTION
        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > WIDTH:
            self.vx = -self.vx
        if self.y - BALL_RADIUS > HEIGHT:
            balls.remove(self)

    def collides_with_pin(self, pin):
        pin_x, pin_y = pin
        distance = ((self.x - pin_x) ** 2 + (self.y - pin_y) ** 2) ** 0.5
        return distance <= BALL_RADIUS + PIN_RADIUS

    def handle_pin_collision(self, pin):
        pin_x, pin_y = pin
        dx = self.x - pin_x
        dy = self.y - pin_y
        distance = ((dx) ** 2 + (dy) ** 2) ** 0.5
        if distance == 0:
            return
        nx = dx / distance
        ny = dy / distance
        dot_product = self.vx * nx + self.vy * ny
        self.vx -= 2 * dot_product * nx * BOUNCE_REDUCTION
        self.vy -= 2 * dot_product * ny * BOUNCE_REDUCTION
        if random.random() < CENTER_PULL:
            if self.x < WIDTH // 2:
                self.vx += 1 * RATIO
            else:
                self.vx -= 1 * RATIO

    def render(self, screen):
        pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)

def create_ball():
    if len(balls) < MAX_BALLS:
        x = WIDTH // 2
        y = 0
        balls.append(Ball(x, y))

def update_balls():
    for ball in balls:
        ball.update()

def render_balls(screen):
    for ball in balls:
        ball.render(screen)
