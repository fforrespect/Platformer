import pygame
import numpy as np

from Meta.Process import Vector
from Setup import GlobalVars


def process(enemy):
    player = GlobalVars.player

    enemy_pos = enemy.rect.center
    player_pos = player.rect.center

    # standardise the direction the bullet's travelling in
    unit_vector = Vector.unit_vector(enemy_pos, player_pos)
    # 1. prevents div by 0 errors
    # 2. if the enemy and player are on different levels, don't shoot
    # 3. don't shoot if the enemy's dead
    if (0 in unit_vector) or \
            (enemy.level != player.level) or \
            enemy.is_dead:
        return 0, 0, None

    # essentially the range function, but moves by floats instead of ints
    positions_to_check = (np.arange(player_pos[0], enemy_pos[0], unit_vector[0]),
                          np.arange(player_pos[1], enemy_pos[1], unit_vector[1]))

    something_in_way = False

    # iterate through all positions and check if there's anything in the way
    for i in range(len(positions_to_check[0])):
        position_i = [positions_to_check[0][i], positions_to_check[1][i]]

        # check every position between the player and the enemy,
        #   create a rect at that position, and...
        rect = pygame.Rect(position_i, (10, 10))
        # check if it collides with anything on the screen (i.e. if anything's in the way)
        collided = rect.collidelist(GlobalVars.all_objects)

        # 1. if nothing's in the way...
        # 2. ...or if just itself is in the way...
        # 3. ...or if just the player is in the way...
        if (collided == -1) or \
                (GlobalVars.all_objects[collided] is enemy) or \
                (GlobalVars.all_objects[collided] is player):

            # ...then something_in_way remains false
            continue

        # but if there is something in the way...
        else:
            something_in_way = True

    # ...don't shoot,
    #   otherwise, aim at the player
    aim = player_pos if not something_in_way else None

    l_or_r = 0
    has_jumped = 0

    # return the results of all the processing
    return l_or_r, has_jumped, aim
