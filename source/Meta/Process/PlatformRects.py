from Object import Platform
from Setup import GlobalVars


def find():
    # generate a list of the pg.rects of all platforms in the game
    all_platform_rects = []
    for object_i in GlobalVars.all_objects:
        if isinstance(object_i, Platform.Platform):
            all_platform_rects.append(object_i.rect)

    return all_platform_rects