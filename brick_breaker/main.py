from typing import List

from settings import *

from brick import Brick
from paddle import Paddle
from ball import Ball


class Game:
    def __init__(self):
        # Window
        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

        # Game States
        self.running = True
        self.clock = pygame.time.Clock()
        self.score = 0
        self.lives = 3
        self.is_game_over = False
        self.won = False

        # Game Objects
        self.paddle = Paddle(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 20 - PADDLE_HEIGHT)
        self.bricks = self._generate_bricks()
        self.ball = Ball(WIDTH // 2 - BALL_RADIUS, HEIGHT - 100)

        self.font = pygame.font.SysFont("comicsans", 36)

    @staticmethod
    def _generate_bricks() -> List[Brick]:
        bricks = []
        colors = [RED, GREEN, BLUE, SKY, ORANGE, YELLOW]
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = BRICK_OFFSET_X + col * (BRICK_WIDTH + BRICK_PADDING)
                y = BRICK_OFFSET_Y + row * (BRICK_HEIGHT + BRICK_PADDING)
                color = colors[row % len(colors)]
                brick = Brick(x, y, color)
                bricks.append(brick)

        return bricks

    def _reset_game(self):
        self.score = 0
        self.lives = 3
        self.is_game_over = False
        self.won = False
        self.bricks = self._generate_bricks()
        self.paddle.reset()
        self.ball.reset()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (self.is_game_over or self.won):
                    self._reset_game()

        keys = pygame.key.get_pressed()

        # Move paddle LEFT/RIGHT
        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()

    def update(self):
        if self.is_game_over or self.won:
            return

        self.ball.update()

        # Ball Collision with wall
        if self.ball.rect.left < 0:
            self.ball.bounce_x()
            self.ball.rect.left = 0
        if self.ball.rect.right > WIDTH:
            self.ball.bounce_x()
            self.ball.rect.right = WIDTH
        if self.ball.rect.top < 0:
            self.ball.bounce_y()

        # Ball Collision with paddle
        if self.ball.rect.colliderect(self.paddle.rect) and self.ball.dy > 0:
            self.ball.bounce_y()
            offset = (self.ball.rect.centerx - self.paddle.rect.centerx) / (PADDLE_WIDTH / 2)
            self.ball.dx = offset * BALL_SPEED

        # Ball Collision with bricks
        for brick in self.bricks:
            if brick.active and self.ball.rect.colliderect(brick.rect):
                brick.active = False
                self.score += 10
                self.ball.bounce_y()
                break

        # Ball Goes below the screen
        if self.ball.rect.top > HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                self.is_game_over = True
            else:
                self.ball.reset()
                self.paddle.reset()

        self.won = all(not brick.active for brick in self.bricks)

    def draw(self):
        self.window.fill(BLACK)

        for brick in self.bricks:
            if brick.active:
                brick.draw(self.window)

        self.paddle.draw(self.window)
        self.ball.draw(self.window)

        # Display score and lives
        score_text = self.font.render(f"Scores: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)

        self.window.blit(score_text, (10, 10))
        self.window.blit(lives_text, (WIDTH - 10 - lives_text.get_width(), 10))

        if self.is_game_over:
            game_over_text = self.font.render(
                f"Game Over! Score: {self.score}. Press r to restart...",
                True, WHITE)
            self.window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2,
                                              HEIGHT // 2 - game_over_text.get_height() // 2))
        elif self.won:
            won_text = self.font.render(
                f"You Won! Score: {self.score}. Press r to restart...",
                True, WHITE)
            self.window.blit(won_text, (WIDTH // 2 - won_text.get_width() // 2,
                                              HEIGHT // 2 - won_text.get_height() // 2))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
