import pygame
from math import sqrt

# Environment & Physics #
SCREEN_SIZE = (1400, 800)

FPS = 60
GRAVITY = 30/FPS
_STANDARD_SPEED = 300/FPS

# Player #
PLAYER_JUMP_POWER = 20*sqrt(GRAVITY)
PLAYER_SPEED = _STANDARD_SPEED * 1
PLAYER_SIZE = (40, 60)
PLAYER_START_POSITION = (200, 100)
PLAYER_LIVES = 3

# Enemy #
ENEMY_SPEED = _STANDARD_SPEED * 0.5
ENEMY_SIZE = (40, 40)
ENEMY_LIVES = 3

# Bullet #
BULLET_SPEED = 10
BULLET_SIZE = 10

# Display #
CHAR_BORDER_RADIUS = 5
PLATFORM_BORDER_RADIUS = 0

# Lives #
LIVES_SPACING = 65
LIVES_PADDING = 25

LIVES_SIZE = 50
LIVES_START_X = SCREEN_SIZE[0] - (LIVES_PADDING*2 + LIVES_SIZE/2)

# Controls #
LEFT_BUTTON = pygame.K_a
RIGHT_BUTTON = pygame.K_d
JUMP_BUTTON = pygame.K_SPACE

# Files #
_RESOURCES_FP = "../Resources/"
_LEVELS_FP = f"{_RESOURCES_FP}Levels/"

ACTIVE_LEVELS_FP = f"{_LEVELS_FP}Active/"
STORED_LEVELS_FP = f"{_LEVELS_FP}Store/"

IMAGES_FP = f"{_RESOURCES_FP}Images/"