from settings import *

"""
LEFT: -1,0
RIGHT: 1:0
UP:    0:-1
DOWN:  0:1
"""

LEFT = pygame.Vector2(-1, 0)
RIGHT = pygame.Vector2(1, 0)
UP = pygame.Vector2(0, -1)
DOWN = pygame.Vector2(0, 1)


class Snake:
    def __init__(self):
        # (Col, Row)
        self.body = [
            pygame.Vector2(6, 10), pygame.Vector2(5, 10), pygame.Vector2(4, 10),
        ]
        self.direction = RIGHT

        self.last_moved = 0
        self.can_move = True

        self.lost = False

    def turn_up(self):
        if self.direction != DOWN:
            self.direction = UP
    def turn_down(self):
        if self.direction != UP:
            self.direction = DOWN
    def turn_left(self):
        if self.direction != RIGHT:
            self.direction = LEFT
    def turn_right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def move(self):
        self.body.pop()
        self.body.insert(0, self.body[0] + self.direction)

        for i in range(1, len(self.body)):
            part = self.body[i]
            if part == self.body[0]:
                self.lost = True

    def contains_part(self, current_part: pygame.Vector2):
        for part in self.body:
            if part == current_part:
                return True
        return False

    def game_over(self) -> bool:
        if self.lost: return True

        for part in self.body:
            x = part.x * CELL_SIZE
            y = part.y * CELL_SIZE
            if x >= WIDTH or x < 0 or y < 0 or y >= HEIGHT:
                return True
        return False

    def grow(self):
        last_part = self.body[-1]
        new_part = pygame.Vector2(last_part.x - self.direction.x, last_part.y - self.direction.y)
        self.body.append(new_part)

    def update(self):
        self.can_move = self.last_moved + SNAKE_MOVE_TIMEOUT < pygame.time.get_ticks()
        if self.can_move:
            self.move()
            self.last_moved = pygame.time.get_ticks()

    def draw(self, surface):
        for part in self.body:
            x = part.x * CELL_SIZE
            y = part.y * CELL_SIZE
            pygame.draw.rect(surface, ORANGE, (x, y, CELL_SIZE, CELL_SIZE))
