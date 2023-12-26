import pygame
import numpy as np

from Meta.Process import UnitVector
from Setup import GlobalVars


def process(enemy, player):
    enemy_pos = enemy.rect.center
    player_pos = player.rect.center

    unit_vector = UnitVector.calculate(enemy_pos, player_pos)
    # print(0 in unit_vector)
    # print(enemy.level != player.level)
    # print(enemy.is_dead)
    # print()

    if (0 in unit_vector) or \
        (enemy.level != player.level) or \
         enemy.is_dead:

        return 0, 0, None
    # else:
    #     print("ready to aim!")

    positions_to_check = (np.arange(player_pos[0], enemy_pos[0], unit_vector[0]),
                          np.arange(player_pos[1], enemy_pos[1], unit_vector[1]))

    something_in_way = False

    for i in range(len(positions_to_check[0])):
        current_pos = [positions_to_check[0][i], positions_to_check[1][i]]

        rect = pygame.Rect(current_pos, (10, 10))
        collided = rect.collidelist(GlobalVars.all_objects)

        if (collided == -1) or \
            (GlobalVars.all_objects[collided] is enemy) or \
            (GlobalVars.all_objects[collided] is player):

            continue

        else:
            something_in_way = True


    aim = player_pos if not something_in_way else None


    l_or_r = 0
    has_jumped = 0


    return l_or_r, has_jumped, aim