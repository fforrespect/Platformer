from Meta.Process import Vector, Vision
from Setup import GlobalVars, Constants


def process(enemy):
    player = GlobalVars.player

    # The processing won't be done at all if the enemy can't see the player
    if enemy.is_dead or not Vision.can_see_each_other(enemy, player):
        return 0, 0, None

    l_or_r = _move_l_r(enemy, player)
    has_jumped = 0
    # If the enemy can see the player, it will try and shoot, no matter what
    # However, it can only shoot every x frames, where x is Constants.ENEMY_SHOOT_BUFFER
    aim = player.bounding_rect.center if not GlobalVars.elapsed_frames % Constants.ENEMY_SHOOT_BUFFER else None

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
