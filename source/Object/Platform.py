import pygame
from Setup import Colours


class Platform:
    def __init__(self, size, position):
        self.size = size
        self.position = position

        self.colour = Colours.BLUE
        self.rect = pygame.Rect(position, size)

    def __str__(self):
        return f"Platform of size {self.size}, pos {self.position}"
