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
        self.image = f"{Constants.IMAGES_FP}life.png"

        GlobalVars.all_overlays.append(self)


    def draw(self, screen):
        life_img = pygame.image.load(self.image)
        life_img = pygame.transform.scale(life_img, (50, 50))

        screen.blit(life_img, (self.x, self.y))