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
    # just pull the current level from the GlobalVars store
    level_number = GlobalVars.current_level

    # gets all the lines of the level file, and makes them ready to process
    with open(f"{Constants.ACTIVE_LEVELS_FP}{level_number}.txt", "r") as level_file:
        file_lines = list(filter(None, level_file.read().split("\n")))

    decoded_objects = []
    # will be used later to determine which direction the player can go
    directions = ("L", "R", "U", "D")
    teleports = {}

    for line in file_lines:
        # just a failsafe in case there's a blank line in the file
        if line == '':
            continue

        match line[0]:
            # add to the teleports dictionary
            case direction if direction in directions:
                teleports[(level_number, directions.index(direction))] = line[2:]

            # Platform
            case "P":
                # process the platform information
                data = list(map(int, line[2:].split(", ")))
                # add the platform to the objects list
                decoded_objects.append(Platform.Platform(data[:2], data[2:]))

            # Player (Character)
            case "C":
                pass

            # Enemy
            case "E":
                # process the enemy information...
                data = list(map(int, line[2:].split(", ")))

                # ...and instantiate the enemy with that info
                enemy = Character.Character(
                    size=Constants.ENEMY_SIZE,
                    position=data[:2],
                    speed=Constants.ENEMY_SPEED,
                    level=level_number,
                    facing=data[2]
                )

                # finally, add the newly created enemy to the objects list
                decoded_objects.append(enemy)

    return decoded_objects, teleports


# Delete an enemy from the file,
#   never to be used in this game again
def delete_enemy(enemy_to_delete_hash):
    level_number = GlobalVars.current_level
    current_filepath = f"{Constants.ACTIVE_LEVELS_FP}{level_number}.txt"

    with open(current_filepath, "r") as level_file_r:
        file_lines = level_file_r.readlines()

    for line_i in range(len(file_lines)):
        # if there's an enemy line in the file...
        if file_lines[line_i][0] == "E":
            # ...process its info
            data = list(map(int, file_lines[line_i][2:].split(", ")))

            size = Constants.ENEMY_SIZE
            position = data[:2]

            current_enemy_hash = sum(size) + sum(position)

            # if its hash is the same as the one you want to delete...
            if enemy_to_delete_hash == current_enemy_hash:
                # ...remove the enemy from the file
                del file_lines[line_i]

                # then write the new data, without the enemy, to the active file
                with open(current_filepath, "w") as level_file_w:
                    level_file_w.writelines(file_lines)

                # no need for more processing
                return
