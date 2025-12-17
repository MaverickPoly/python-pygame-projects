from settings import *


class Pipe:
    def __init__(self, offset):
        self.offset = offset
        self.image = PIPE_IMAGE
        self.rotated_image = pygame.transform.rotate(PIPE_IMAGE, 180)
        self.x = WIDTH
        self.y = offset
        self.active = True
        self.passed = False

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.offset)
        self.rotated_rect = self.rotated_image.get_rect()
        self.rotated_rect.topleft = (self.x, self.offset + PIPE_IMAGE.get_height() + PIPE_DISTANCE)

    def update(self):
        self.rect.x -= PIPE_SPEED
        self.rotated_rect.x -= PIPE_SPEED
        if self.rect.x + PIPE_IMAGE.get_width() < 0:
            self.active = False

    def draw(self, surface: pygame.Surface):
        surface.blit(self.rotated_image, self.rect)
        surface.blit(self.image, self.rotated_rect)
