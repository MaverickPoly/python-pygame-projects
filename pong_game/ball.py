from settings import *

import random
from game_object import GameObject


class Ball(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x - BALL_RADIUS, y - BALL_RADIUS, BALL_RADIUS, BALL_RADIUS) # Top Left corner ball
        self.velocity_x = BALL_SPEED_X
        self.velocity_y = BALL_SPEED_Y

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def reset(self):
        self.x = WIDTH // 2 - BALL_RADIUS
        self.y = HEIGHT // 2 - BALL_RADIUS
        self.velocity_x *= -1
        self.velocity_y = random.choice([-1, +1]) * BALL_SPEED_Y

    def bounce_y(self):
        self.velocity_y *= -1

    def bounce_x(self):
        self.velocity_x *= -1

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, RED, (self.x + BALL_RADIUS, self.y + BALL_RADIUS), BALL_RADIUS)

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
