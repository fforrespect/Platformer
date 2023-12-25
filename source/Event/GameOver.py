import pygame

from Setup import GlobalVars


def quit_pressed(events):
    for event in events:
        if event.type == pygame.QUIT:
            GlobalVars.game_running = False
            return True
    return False



def player_dies():

    pass