import pygame

from Setup import GlobalVars, Colours


def display(screen):
    # Background
    screen.fill(Colours.BLACK)

    # Iterate through the objects, and display them one by one
    for item in GlobalVars.all_objects + GlobalVars.all_overlays:
        item.draw(screen)

    pygame.display.update()
