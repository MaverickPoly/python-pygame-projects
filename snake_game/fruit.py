from settings import *


class Fruit:
    def __init__(self, row: int, col: int):
        self.position = pygame.Vector2(row, col)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, RED, (self.position.x * CELL_SIZE, self.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


