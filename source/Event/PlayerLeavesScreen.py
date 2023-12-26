from Setup import GlobalVars
from Object import Character, Bullet


def process(new_level_key, teleports):
    # actually change the current level
    GlobalVars.current_level = int(teleports[new_level_key])
    # remove all bullets
    Bullet.active_bullets = []
    # remove all enemies
    Character.active_enemies = []
    all_objects = GlobalVars.all_objects
    for object_i in all_objects:
        if isinstance(object_i, Character.Character) and object_i.is_enemy:
            GlobalVars.all_objects.remove(object_i)
