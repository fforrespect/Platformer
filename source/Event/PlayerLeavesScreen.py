from Event import EnemyDies
from Setup import GlobalVars
from Object import Character, Bullet


def process(new_level_key, teleports):
    # actually change the current level
    GlobalVars.current_level = int(teleports[new_level_key])
    # remove all bullets
    Bullet.active_bullets = []
    # remove all enemies using the EnemyDies.process function
    #   however, remove_forever is false, since you can come back to that screen
    map(lambda x: EnemyDies.process(x, False), Character.active_enemies)
    Character.active_enemies = []