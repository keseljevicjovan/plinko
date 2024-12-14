import pygame
import random
from settings import WIDTH, HEIGHT, PIN_SPACING, RATIO, PIN_ROWS

BALL_RADIUS = int(8 * RATIO)
BALL_COLOR = (255, 255, 255)
BALL_GRAVITY = 0.5
BALL_FRICTION = 0.98
MAX_BALLS = 20

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

        self.vx *= BALL_FRICTION

        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > WIDTH:
            self.vx = -self.vx

        if self.y - BALL_RADIUS > HEIGHT:
            balls.remove(self)

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
