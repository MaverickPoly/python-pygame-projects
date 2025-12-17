import pygame
from os.path import join


# ASSETS
BACKGROUND = pygame.transform.scale_by(pygame.image.load(join("assets", "background-day.png")), 3 / 2)
MENU = pygame.transform.scale_by(pygame.image.load(join("assets", "message.png")), 2)
BASE = pygame.transform.scale_by(pygame.image.load(join("assets", "base.png")), 1.3)

BIRD_IMAGE_PATHS = ["yellowbird-downflap.png", "yellowbird-midflap.png", "yellowbird-upflap.png"]
BIRD_IMAGES = [pygame.transform.scale_by(pygame.image.load(join("assets", path)), 1.5) for path in BIRD_IMAGE_PATHS]

PIPE_IMAGE = pygame.transform.scale_by(pygame.image.load(join("assets", "pipe-green.png")), 1.2)


# Window
WIDTH, HEIGHT = BACKGROUND.get_width(), BACKGROUND.get_height()
TITLE = "Flappy Bird"
FPS = 60

# BIRD
BIRD_WIDTH, BIRD_HEIGHT = BIRD_IMAGES[0].get_width(), BIRD_IMAGES[0].get_height()
GRAVITY = 0.5
JUMP_FORCE = 10

# Pipes
PIPE_DISTANCE = 170
PIPE_SPEED = 3
PIPE_GENERATE_TIMEOUT = 2200

# Colors
WHITE = (250, 250, 250)

