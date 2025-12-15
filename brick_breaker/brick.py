from typing import Tuple

from settings import *


class Brick:
    def __init__(self, x: int, y: int, color: Tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color
        self.active = True

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.rect)
