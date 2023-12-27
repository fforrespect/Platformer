import pygame
import numpy as np

from Meta.Process import Vector
from Object import Bullet
from Setup import GlobalVars


def can_see_each_other(object1, object2):
    # if they're not on the same level, they obv can't see each other
    if object1.level != object2.level:
        return False

    pos1 = object1.bounding_rect.center
    pos2 = object2.bounding_rect.center

    # standardise the direction you're looking
    unit_vector = Vector.unit_vector(pos1, pos2)

    # Prevents div by 0 errors
    if 0 in unit_vector:
        return False

    # essentially the range function, but moves by floats instead of ints
    positions_to_check = (np.arange(pos2[0], pos1[0], unit_vector[0]),
                          np.arange(pos2[1], pos1[1], unit_vector[1]))

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
        # 4. ...or if it just collided with a bullet (we can consider bullets to be invisible)...
        if (collided == -1) or \
                (GlobalVars.all_objects[collided] is object1) or \
                (GlobalVars.all_objects[collided] is object2) or \
                (isinstance(collided, Bullet.Bullet)):

            # ...then something_in_way remains false
            continue

        # but if there is something in the way...
        else:
            # ...they can't see each other
            return False

    return True
