from Meta.Process import Level
from Object import Character
from Setup import GlobalVars


def process(enemy, player_has_left_screen=False):
    Character.active_enemies.remove(enemy)
    GlobalVars.all_objects.remove(enemy)

    if not player_has_left_screen:
        Level.delete_enemy(enemy.enemy_hash)

