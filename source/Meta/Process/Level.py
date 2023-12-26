import os
import shutil

from Object import Character, Platform
from Setup import Constants, GlobalVars


def initialise():
    directories = (Constants.STORED_LEVELS_FP, Constants.ACTIVE_LEVELS_FP)

    # iterate over files in the directories
    for file_name in os.listdir(directories[0]):
        # generate filepaths
        filepaths = list(map(lambda x: os.path.join(x, file_name), directories))
        # create a copy of the file, to be used in the program
        shutil.copyfile(*filepaths)

    return decode()



def decode():
    level_number = GlobalVars.current_level

    level_file = open(f"{Constants.ACTIVE_LEVELS_FP}{level_number}.txt", "r")
    file_lines = list(filter(None, level_file.read().split("\n")))
    level_file.close()

    decoded_objects = []
    dirs = ["L", "R", "U", "D"]
    teleports = {}

    for line in file_lines:
        if line == '':
            continue

        if line[0] in dirs:
            teleports[(level_number, dirs.index(line[0]))] = line[2:]

        elif line[0] == "P":
            data = list(map(int, line[2:].split(", ")))
            decoded_objects.append(Platform.Platform(data[:2], data[2:]))

        elif line[0] == "C":
            pass

        elif line[0] == "E":
            data = list(map(int, line[2:].split(", ")))

            enemy = Character.Character(
                size=Constants.ENEMY_SIZE,
                position=data[:2],
                speed=Constants.ENEMY_SPEED,
                level=level_number,
                facing=data[2]
            )

            decoded_objects.append(enemy)


    return decoded_objects, teleports


def decode_enemy():
    level_number = GlobalVars.current_level

    level_file = open(f"{Constants.ACTIVE_LEVELS_FP}{level_number}.txt", "r")
    file_lines = list(filter(None, level_file.read().split("\n")))
    level_file.close()

    for line in file_lines:
        if line[0] == "E":
            data = list(map(int, line[2:].split(", ")))

            size = Constants.ENEMY_SIZE
            position = data[:2]

            return sum(size) + sum(position)

    return None
