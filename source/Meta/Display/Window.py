import pygame

from Object import Character, Platform, Bullet
from Setup import Constants, GlobalVars, Colours


def display(screen):
    # Background
    screen.fill(Colours.BLACK)

    # Iterate through the objects, and display them one by one
    for object_i in GlobalVars.all_objects:
        # Give all the characters a bit of rounded corners
        match type(object_i):
            case Character.Character:
                radius = Constants.CHAR_BORDER_RADIUS
            case Platform.Platform:
                radius = Constants.PLATFORM_BORDER_RADIUS
            case Bullet.Bullet:
                radius = Constants.BULLET_SIZE
            case _:
                radius = 0

        # Take the colour and rect properties directly from the objects themselves
        pygame.draw.rect(screen, object_i.colour, object_i.rect, border_radius=radius)

    for object_i in GlobalVars.all_overlays:
        pass

    pygame.display.update()
