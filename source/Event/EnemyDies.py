from Meta.Process import Level
from Object import Character
from Setup import GlobalVars


def process(enemy):
    Character.active_enemies.remove(enemy)
    GlobalVars.all_objects.remove(enemy)

    Level.delete_enemy(enemy.enemy_hash)

