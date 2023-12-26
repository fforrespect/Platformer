import pygame

from Setup import GlobalVars, Colours, Constants


def display():
    # How many lives the player has
    lives = GlobalVars.player.lives

    for i in range(lives):
        Life(i)


class Life:
    def __init__(self, number):
        self.centre = (Constants.LIVES_START_X - (number * Constants.LIVES_SPACING), Constants.LIVES_PADDING)
        self.radius = Constants.LIVES_RADIUS

        self.colour = Colours.RED

        GlobalVars.all_overlays.append(self)


    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.centre, self.radius)