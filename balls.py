import pygame
import random
from settings import WIDTH, HEIGHT, RATIO, PIN_SPACING, PIN_RADIUS
from pins import pins

BALL_RADIUS = int(7 * RATIO)
BALL_COLOR = (255, 255, 255)
BALL_GRAVITY = 0.2
BALL_FRICTION = 0.98
MAX_BALLS = 20
BOUNCE_REDUCTION = 0.9
MIN_BOUNCE_DISTANCE = 0.1
MAX_BOUNCE_DISTANCE = 1.2
CENTER_PULL = 0.8

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
        self.vy *= BALL_FRICTION

        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > WIDTH:
            self.vx = -self.vx * BOUNCE_REDUCTION
        
        if self.y - BALL_RADIUS > HEIGHT:
            balls.remove(self)

    def collides_with_pin(self, pin):
        pin_x, pin_y = pin
        distance = ((self.x - pin_x) ** 2 + (self.y - pin_y) ** 2) ** 0.5
        return distance < BALL_RADIUS + PIN_RADIUS

    def handle_pin_collision(self, pin):
        pin_x, pin_y = pin
        dx = self.x - pin_x
        dy = self.y - pin_y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance == 0:
            return

        nx = dx / distance
        ny = dy / distance

        dot_product = self.vx * nx + self.vy * ny

        bounce_factor = 0.7
        self.vx -= 2 * dot_product * nx * bounce_factor
        self.vy -= 2 * dot_product * ny * bounce_factor

        overlap = (BALL_RADIUS + PIN_RADIUS) - distance
        self.x += nx * overlap * 0.5
        self.y += ny * overlap * 0.5

        self.apply_horizontal_move()

        self.vy = self.calculate_bounce_velocity(pin)

    def apply_horizontal_move(self):
        if random.random() < CENTER_PULL:
            if self.x < WIDTH // 2:
                self.vx += random.uniform(0, 1)
            else:
                self.vx -= random.uniform(0, 1)
        else:
            if random.random() < 0.5:
                self.vx += random.uniform(0, 1)
            else:
                self.vx -= random.uniform(0, 1)

    def calculate_bounce_velocity(self, pin):
        pin_x, pin_y = pin
        distance_to_pin = ((self.x - pin_x) ** 2 + (self.y - pin_y) ** 2) ** 0.5
        
        bounce_distance = random.uniform(MIN_BOUNCE_DISTANCE, MAX_BOUNCE_DISTANCE)

        if distance_to_pin < bounce_distance:
            bounce_height = distance_to_pin
        else:
            bounce_height = bounce_distance
        
        return -((2 * BALL_GRAVITY * bounce_height) ** 0.5)

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
