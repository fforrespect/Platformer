from Meta.Process import Vector, Vision
from Setup import GlobalVars


def process(enemy):
    # Just a failsafe, in case this is run by mistake
    if enemy.is_dead:
        return 0, 0, None

    player = GlobalVars.player

    can_see = Vision.can_see_each_other(enemy, player)

    l_or_r = 0 # _move_l_r(enemy_pos, player_pos)
    has_jumped = 0
    # If the enemy can see the player, it will shoot, no matter what
    aim = player.bounding_rect.center if can_see else None

    # return the results of all the processing
    return l_or_r, has_jumped, aim


def _move_l_r(enemy, player):
    enemy_pos = enemy.bounding_rect.center
    player_pos = player.bounding_rect.center

    current_distance = Vector.distance(enemy_pos, player_pos)

    # If the enemy moved ..., would it be closer to the player or not?:
    # If so, move in that direction
    # ...left...
    if Vector.distance_l_r(enemy_pos, player_pos, -1) < current_distance:
        return -1
    # ...right...
    elif Vector.distance_l_r(enemy_pos, player_pos, 1) < current_distance:
        return 1
    return 0
