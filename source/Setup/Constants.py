import pygame
from math import sqrt

# Environment & Physics #
SCREEN_SIZE = (1400, 800)

FPS = 60
GRAVITY = 30/FPS

# Player #
PLAYER_JUMP_POWER = 20*sqrt(GRAVITY)
PLAYER_SPEED = 300/FPS
PLAYER_SIZE = (40, 60)
PLAYER_START_POSITION = (200, 100)

# Enemy #
ENEMY_SPEED = 300/FPS
ENEMY_SIZE = (40, 40)

# Bullet #
BULLET_SPEED = 10
BULLET_SIZE = 10

# Display #
CHAR_BORDER_RADIUS = 5
PLATFORM_BORDER_RADIUS = 0

# Lives #
LIVES_PADDING = 50
LIVES_SPACING = 65

LIVES_START_X = SCREEN_SIZE[0] - LIVES_PADDING
LIVES_RADIUS = 25

# Controls #
LEFT_BUTTON = pygame.K_a
RIGHT_BUTTON = pygame.K_d
JUMP_BUTTON = pygame.K_SPACE

# Files #
ACTIVE_LEVELS_FP = "../Resources/Levels/Active/"
STORED_LEVELS_FP = "../Resources/Levels/Store/"