import sys
import pygame

from Meta.Display import Window, Lives
from Meta.Process import Level
from Event import GameOver
from Object import Character, Bullet
from Setup import Constants, GlobalVars


# Initialise global variables
GlobalVars.current_level = level_memory = 0
GlobalVars.game_running = True
GlobalVars.all_objects = []

# Set up pygame
pygame.init()
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock = pygame.time.Clock()

# Initialise character
GlobalVars.player = Character.Character(
    size=Constants.PLAYER_SIZE,
    position=Constants.PLAYER_START_POSITION,
    speed=Constants.PLAYER_SPEED,
    level=GlobalVars.current_level,
    facing=1,
    is_enemy=0
)

# Set up the first level and the level files
decoded_objects, teleports = Level.initialise()

# Logic to make sure only one click is counted at a time
check_click = 0
click = 0

while GlobalVars.game_running:
    clock.tick(Constants.FPS)

    # Checks if the red x has been pressed, and quits the game if so
    if GameOver.quit_pressed(pygame.event.get()):
        break

    # If a new level is reached...
    if level_memory != GlobalVars.current_level:
        # ...decode and store that level
        decoded_objects, teleports = Level.decode()
        level_memory = GlobalVars.current_level

    # Define which objects are on the screen...
    GlobalVars.all_objects = [GlobalVars.player] + decoded_objects + Bullet.active_bullets
    # ...and remove any dead characters
    Character.remove_if_dead()

    keys = pygame.key.get_pressed()

    # Only register a click if in the last frame, a click wasn't registered
    # This prevents holding down left click and creating a stream of bullets
    if pygame.mouse.get_pressed()[0]:
        click = 0 if check_click == 1 else 1
        check_click = 1
    else:
        check_click = 0

    # Pack the registered inputs together for ease of use
    inputs = (keys, click)

    # Move all the movable objects to their new positions
    Character.move_all(inputs, teleports)
    Bullet.move_all()

    Lives.display()

    # And finally, draw everything to the screen
    Window.display(screen)

pygame.quit()
sys.exit()
