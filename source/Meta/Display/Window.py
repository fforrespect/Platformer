import pygame

from Meta.Display import Lives
from Object import Character, Platform, Bullet
from Setup import Constants, GlobalVars, Colours


def display(screen):
    # Background
    screen.fill(Colours.BLACK)

    # Iterate through the objects, and display them one by one
    for object_ in GlobalVars.all_objects:
        # Determine how rounded everything's corners should be
        match type(object_):
            case Character.Character:
                radius = Constants.CHAR_BORDER_RADIUS
            case Platform.Platform:
                radius = Constants.PLATFORM_BORDER_RADIUS
            case Bullet.Bullet:
                # Makes it a circle
                radius = Constants.BULLET_SIZE
            case _:
                radius = 0

        # Take the colour and rect properties directly from the objects themselves
        pygame.draw.rect(screen, object_.colour, object_.rect, border_radius=radius)

    for overlay in GlobalVars.all_overlays:
        match overlay[0]:
            case "Life":
                Lives.draw(screen, overlay[1])





    pygame.display.update()
