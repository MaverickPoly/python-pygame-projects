from settings import *


class Paddle:
    def __init__(self, x: int, y: int):
        self.color = GRAY
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def reset(self):
        self.rect.x = WIDTH // 2 - PADDLE_WIDTH // 2
        self.rect.y = HEIGHT - 20 - PADDLE_HEIGHT

    def move_left(self):
        self.rect.x -= PADDLE_SPEED
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += PADDLE_SPEED
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.rect)
