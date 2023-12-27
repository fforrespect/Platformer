import pygame

from Setup import GlobalVars, Constants


def display():
    # How many lives the player has
    lives = GlobalVars.player.lives

    for i in range(lives):
        Life(i)


class Life:
    def __init__(self, number):
        self.x = Constants.LIVES_START_X - (number * Constants.LIVES_SPACING)
        self.y = Constants.LIVES_PADDING

        self.image = pygame.image.load(f"{Constants.IMAGES_FP}life.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        GlobalVars.all_overlays.append(self)


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))