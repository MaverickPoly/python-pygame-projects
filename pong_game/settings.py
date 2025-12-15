import pygame


pygame.init()   # Initialize pygame

# Window
WIDTH, HEIGHT = 1400, 800
TITLE = "Pong Game"
FPS = 60
LINE_WIDTH = 2
OFFSET = 20
PADDING = 25

# Colors
BLACK = (20, 20, 20)
WHITE = (240, 240, 240)
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
RED = (240, 0, 0)

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 160
PADDLE_SPEED = 14

# Ball
BALL_RADIUS = 15
BALL_SPEED_X = 12
BALL_SPEED_Y = 10
