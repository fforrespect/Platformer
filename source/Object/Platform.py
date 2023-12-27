import pygame
from Setup import Colours, Constants


class Platform:
    def __init__(self, size, position):
        self.size          = size
        self.position      = position

        self.colour        = Colours.BLUE
        self.rect          = pygame.Rect(position, size)
        self.bounding_rect = self.rect

    def __str__(self):
        return f"Platform of size {self.size}, at pos {self.position}"

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=Constants.PLATFORM_BORDER_RADIUS)

