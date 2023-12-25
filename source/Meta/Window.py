import pygame

from Object import Character
from Setup import Constants, GlobalVars, Colours


def display(screen):
    # Background
    screen.fill(Colours.BLACK)

    # Iterate through the objects, and display them one by one
    for object_i in GlobalVars.all_objects:
        # Give all the characters a bit of rounded corners
        radius = Constants.CHAR_BORDER_RADIUS if isinstance(object_i, Character.Character) \
            else Constants.PLATFORM_BORDER_RADIUS
        # Take the colour and rect properties directly from the objects themselves
        pygame.draw.rect(screen, object_i.colour, object_i.rect, border_radius=radius)

    pygame.display.update()
