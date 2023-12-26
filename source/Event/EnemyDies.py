from Meta.Process import Level
from Object import Character
from Setup import GlobalVars


def process(enemy, remove_forever=True):
    Character.active_enemies.remove(enemy)
    GlobalVars.all_objects.remove(enemy)

    if remove_forever:
        Level.delete_enemy(enemy.enemy_hash)

