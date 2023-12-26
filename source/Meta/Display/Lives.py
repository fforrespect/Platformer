import pygame

from Setup import GlobalVars, Colours, Constants


def display():
    # How many lives the player has
    lives = GlobalVars.player.lives

    for i in range(lives):
        Life((Constants.LIVES_START_X - (i * Constants.LIVES_SPACING),
              Constants.LIVES_PADDING), Constants.LIVES_RADIUS)


def draw(screen, life):
    pygame.draw.circle(screen, life.colour, life.centre, life.radius)


class Life:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

        self.colour = Colours.RED

        GlobalVars.all_overlays.append(("Life", self))