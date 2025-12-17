from settings import *


class Bird:
    def __init__(self, x: int, y: int):
        self.current_index = 0.0
        self.image = BIRD_IMAGES[int(self.current_index)]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 0

    def jump(self):  # Flap
        self.velocity = -JUMP_FORCE

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        # Animation
        self.current_index = (self.current_index + 0.08) % len(BIRD_IMAGES)
        self.image = BIRD_IMAGES[int(self.current_index)]

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
