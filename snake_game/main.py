from settings import *
import random
from snake import Snake
from fruit import Fruit


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.score = 0

        self.snake = Snake()
        self.fruit = Fruit(random.randint(1, COLS), random.randint(1, ROWS))

        self.font = pygame.font.SysFont("comicsans", 64)

    def draw_background(self):
        for row in range(ROWS):
            for col in range(COLS):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                color = LIGHT_GREEN if (row + col) % 2 == 0 else DARK_GREEN
                pygame.draw.rect(self.window, color, (x, y, CELL_SIZE, CELL_SIZE))

    def reset_game(self):
        self.game_over = False
        self.snake = Snake()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_game()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: self.snake.turn_right()
        if keys[pygame.K_LEFT]: self.snake.turn_left()
        if keys[pygame.K_UP]: self.snake.turn_up()
        if keys[pygame.K_DOWN]: self.snake.turn_down()

    def update(self):
        if self.game_over: return

        self.snake.update()
        if self.snake.game_over():
            self.game_over = True

        head = self.snake.body[0]
        if head == self.fruit.position:
            # Eat Fruit
            # FIXME^  Sometimes fruit is not respawning
            self.score += 1
            self.snake.grow()

            free_cells: list[pygame.Vector2] = []
            for row in range(ROWS):
                for col in range(COLS):
                    pos = pygame.Vector2(row, col)
                    if not self.snake.contains_part(pos):
                        free_cells.append(pos)

            if free_cells:
                new_position = random.choice(free_cells)
                self.fruit = Fruit(new_position.x, new_position.y)
            else:
                self.game_over = True

    def draw(self):
        self.draw_background()
        self.snake.draw(self.window)
        self.fruit.draw(self.window)

        if self.game_over:
            game_over_text = self.font.render(f"Game Over! Score: {self.score}", True, BLACK)
            y = HEIGHT // 2 - game_over_text.get_height() - 80
            self.window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, y))

            score_text = self.font.render(f"Score: {self.score}", True, BLACK)
            y += PADDING + game_over_text.get_height()
            self.window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, y))

            restart_text = self.font.render("Press r to restart...", True, BLACK)
            y += PADDING + restart_text.get_height()
            self.window.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, y))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
