from settings import *

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

        self.left_paddle_score = 0
        self.right_paddle_score = 0

        # Game Objects
        self.left_paddle = Paddle(OFFSET, HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.right_paddle = Paddle(WIDTH - OFFSET - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2)

        self.font = pygame.font.SysFont("comicsans", 72)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

        # Left Paddle Movement
        if keys[pygame.K_w]:
            self.left_paddle.move_up()
        if keys[pygame.K_s]:
            self.left_paddle.move_down()

        # Right paddle Movement
        if keys[pygame.K_UP]:
            self.right_paddle.move_up()
        if keys[pygame.K_DOWN]:
            self.right_paddle.move_down()

    def update(self):
        self.ball.update()

        # Ball Collision with Walls
        if self.ball.y < 0:
            self.ball.y = 0
            self.ball.bounce_y()
        if self.ball.y + BALL_RADIUS > HEIGHT:
            self.ball.y = HEIGHT - BALL_RADIUS
            self.ball.bounce_y()

        # Ball Collision with paddles
        ball_rect = self.ball.get_rect()
        if ball_rect.colliderect(self.left_paddle.get_rect()) and self.ball.velocity_x < 0:   # Left Paddle
            self.ball.bounce_x()
            self.ball.x = self.left_paddle.x + PADDLE_WIDTH
        if ball_rect.colliderect(self.right_paddle.get_rect()) and self.ball.velocity_x > 0:  # Right Paddle
            self.ball.bounce_x()
            self.ball.x = self.right_paddle.x - BALL_RADIUS * 2

        # Ball Went off the screen (scoring)
        if self.ball.x + BALL_RADIUS * 2 < 0:
            # Scoring for right paddle
            self.right_paddle_score += 1
            self.ball.reset()
        if self.ball.x > WIDTH:
            # Scoring for left paddle
            self.left_paddle_score += 1
            self.ball.reset()

        pygame.display.update()

    def draw(self):
        self.window.fill(BLACK)

        pygame.draw.rect(self.window, DARK_GRAY, (WIDTH // 2 - LINE_WIDTH // 2, 0, LINE_WIDTH, HEIGHT))

        self.left_paddle.draw(self.window)
        self.right_paddle.draw(self.window)
        self.ball.draw(self.window)

        # Draw scores
        left_paddle_text = self.font.render(f"{self.left_paddle_score}", True, WHITE)
        right_paddle_text = self.font.render(f"{self.right_paddle_score}", True, WHITE)

        self.window.blit(left_paddle_text, (PADDING, PADDING))
        self.window.blit(right_paddle_text, (WIDTH - PADDING - right_paddle_text.get_width(), PADDING))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
