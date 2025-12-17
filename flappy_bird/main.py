from typing import Optional
import random
import os

from settings import *

from bird import Bird
from pipe import Pipe


class Game:
    def __init__(self):
        pygame.init()

        # Window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        # Game States
        self.running = True
        self.is_menu = True
        self.is_game_over = False
        self.clock = pygame.time.Clock()
        self.score = 0

        self.can_generate_pipe = False
        self.last_pipe_generate = pygame.time.get_ticks()

        # Game Elements
        self.bird: Optional[Bird] = None
        self.pipes: list[Pipe] = []

        self.fontLarge = pygame.font.Font(os.path.join("fonts", "Font.TTF"), 54)
        self.fontSmall = pygame.font.Font(os.path.join("fonts", "Font.TTF"), 30)

        # self.load_game()

    def load_game(self):
        self.is_menu = False
        self.bird = Bird(WIDTH // 2 - BIRD_WIDTH, HEIGHT // 2 - BIRD_HEIGHT // 2)
        self.pipes = []
        self.can_generate_pipe = False
        self.last_pipe_generate = pygame.time.get_ticks()
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.is_menu:
                    self.bird.jump()
                if event.key == pygame.K_m and self.is_game_over:
                    self.is_menu = True
                    self.is_game_over = False

        mouse_presses = pygame.mouse.get_pressed()
        if self.is_menu and mouse_presses[0]:
            self.load_game()

    def generate_pipe(self):
        self.can_generate_pipe = False
        self.last_pipe_generate = pygame.time.get_ticks()
        offset = random.randint(-130, 0)
        pipe = Pipe(offset)
        self.pipes.append(pipe)

    def draw_menu(self):
        self.window.blit(BACKGROUND, (0, 0))
        self.window.blit(MENU, (WIDTH // 2 - MENU.get_width() // 2, HEIGHT // 2 - MENU.get_height() // 2))

    def check_score(self):
        if len(self.pipes) <= 0:
            return

        if self.pipes[-1].passed: return
        if self.pipes[-1].rect.x <= self.bird.rect.x:
            self.pipes[-1].passed = True
            self.score += 1

    def update(self):
        if self.is_game_over:
            return

        self.bird.update()

        if pygame.time.get_ticks() - self.last_pipe_generate > PIPE_GENERATE_TIMEOUT:
            self.can_generate_pipe = True
        if self.can_generate_pipe:
            self.generate_pipe()

        for pipe in self.pipes:
            if pipe.active:
                pipe.update()

        self.check_score()

        if self.bird.rect.bottom >= HEIGHT:
            self.is_game_over = True
        if self.bird.rect.top <= 0:
            self.is_game_over = True

        if len(self.pipes) > 0:
            last_pipe = self.pipes[-1]
            if self.bird.rect.colliderect(last_pipe.rect) or self.bird.rect.colliderect(last_pipe.rotated_rect):
                self.is_game_over = True

    def draw(self):
        pygame.display.update()
        self.window.blit(BACKGROUND, (0, 0))
        self.window.blit(BASE, (0, HEIGHT - BASE.get_height() + 10))
        self.bird.draw(self.window)

        for pipe in self.pipes:
            if pipe.active:
                pipe.draw(self.window)

        score_text = self.fontLarge.render(f"{self.score}", True, WHITE)
        self.window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 100))

        if self.is_game_over:
            text = self.fontSmall.render("Game Over! Press m...", True, WHITE)
            self.window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    def run(self):
        while self.running:
            self.handle_events()
            if self.is_menu:
                self.draw_menu()
            else:
                self.update()
                self.draw()
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
