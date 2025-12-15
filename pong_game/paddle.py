from game_object import GameObject
from settings import *


class Paddle(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move_up(self):
        self.y = max(0, self.y - PADDLE_SPEED)

    def move_down(self):
        self.y = min(HEIGHT - PADDLE_HEIGHT, self.y + PADDLE_SPEED)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, GRAY, self.get_rect())

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
