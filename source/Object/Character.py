import pygame

from Event import EnemyDies, GameOver, EnemyMoves
from Meta.Process import PlatformRects
from Object import Bullet
from Setup import Constants, GlobalVars, Colours


player = []
active_enemies = []


def move_all(inputs, teleports):
    # Run the move function for all characters
    for c in player + active_enemies:
        c.move(inputs, teleports)


def remove_if_dead():
    for c in GlobalVars.all_objects:
        # If an enemy is dead, remove it.
        if isinstance(c, Character) and c.is_enemy and c.is_dead:
            GlobalVars.all_objects.remove(c)


class Character:
    def __init__(self, size, position, speed, level, facing=1, is_enemy=1):
        self.size       = size
        self.position   = position
        self.speed      = speed
        self.level      = level
        self.facing     = facing # 0 is left, 1 is right
        self.is_enemy   = is_enemy # 0 is player, 1 is enemy

        self.velocity   = [0, 0]
        self.colour     = Colours.RED if is_enemy else Colours.GREEN
        self.rect       = pygame.Rect(self.position, self.size)
        self.lives      = 3
        self.is_dead    = False
        self.enemy_hash = (sum(size) + sum(position)) if is_enemy else -1
        print(self.enemy_hash)

        if not is_enemy:
            player.append(self)
        else:
            active_enemies.append(self)


    def __str__(self):
        return ("Player" if self.is_enemy == 0 else "Enemy") + \
               f" of size {self.size}, at pos {(self.rect.left, self.rect.top)}"


    def delete(self):
        active_enemies.remove(self)


    def _is_in_air(self, all_platform_rects):
        # if you're inside a block, you're in the air
        #   (this if statement should actually never return true, but it's just a failsafe)
        if self.rect.move(0, -1).collideobjects(all_platform_rects):
            return True

        # if you're standing on a platform, you're not in the air
        elif self.rect.move(0, 1).collideobjects(all_platform_rects):
            return False
        
        return True

    # direction: -1 is left, 1 is right
    def _move_left_right(self, direction, all_platform_rects):
        self.velocity[0] += (direction * self.speed)

        # check its next position
        about_to_collide = self.rect.move(self.velocity[0], 0).collidelist(all_platform_rects)
        # if it's about to collide (if it's not going to collide with nothing)...
        if about_to_collide != -1:
            # ...stop it
            self.velocity[0] = 0


    def _jump(self, has_jumped, all_platform_rects):

        if not self._is_in_air(all_platform_rects):
            self.velocity[1] -= has_jumped * Constants.PLAYER_JUMP_POWER


        about_to_collide = self.rect.move(self.velocity).collidelist(all_platform_rects)
        # if it's about to collide (if it's not going to collide with nothing)
        if about_to_collide != -1:
            # if the alignment to the ground isn't perfect, snap the player to the ground and stop them moving
            if self.velocity[1] > 0:
                # snap to the top of the platform it's about to collide with...
                snap_to = ((self.rect.move(self.velocity)).collideobjects([all_platform_rects[about_to_collide]])).top
                # ...and stop it moving downwards
                self.velocity[1] = 0

                self.rect.update((self.rect.left, snap_to - self.rect.height), (self.rect.width, self.rect.height))

            # snap the character to the roof then bounce them off of it
            elif self.velocity[1] < 0:
                # snap to the bottom of the platform it's about to collide with...
                plat_to_snap_to = (self.rect.move(self.velocity)).collideobjects([all_platform_rects[about_to_collide]])
                snap_to = plat_to_snap_to.top + plat_to_snap_to.height
                # ...and bounce it backwards
                self.velocity[1] *= -1

                self.rect.update((self.rect.left, snap_to), (self.rect.width, self.rect.height))


    def _shoot(self, pos, aim):
        if aim is None:
            return
        # Initialise a new bullet
        bullet = Bullet.Bullet(self, pos, aim)
        # Let the bullet class do the rest
        bullet.shoot()


    def _leaves_screen(self, teleports):
        level = GlobalVars.current_level

        # Just simplify the direction the player is leaving
        #   into an int 0-3
        if   self.rect.left    <  0:                        direction = 0 # leaves left
        elif self.rect.right   >= Constants.SCREEN_SIZE[0]: direction = 1 # leaves right
        elif self.rect.top     <= 0:                        direction = 2 # leaves up
        elif self.rect.bottom  >  Constants.SCREEN_SIZE[1]: direction = 3 # leaves down
        else: return

        # generates a key for the teleports dictionary
        new_level_key = (level, direction)

        # only change the level if it's a valid teleport point
        #   (if it isn't, the player will just fall off the screen)
        if new_level_key in teleports:
            GlobalVars.current_level = int(teleports[new_level_key])
            # remove all bullets
            Bullet.active_bullets = []
            print("\n"*10 + "NEW LEVEL" + "\n"*10)
        else:
            return

        # Jump the character to the other side of the screen, as soon as the touch the edge
        #   and avoid the edge cases of them being exactly on the edge
        self.rect.move_ip(
            # leaves left
            (Constants.SCREEN_SIZE[0] - Constants.PLAYER_SIZE[0]
             if self.rect.left < 0 else
             # leaves right
             -Constants.SCREEN_SIZE[0] + Constants.PLAYER_SIZE[0]
             if self.rect.right >= Constants.SCREEN_SIZE[0] else
             # doesn't leave
             0),
            # leaves up
            (-Constants.SCREEN_SIZE[1] + Constants.PLAYER_SIZE[1]
             if self.rect.top <= 0 else
             # leaves down
             Constants.SCREEN_SIZE[1] - Constants.PLAYER_SIZE[1]
             if self.rect.bottom > Constants.SCREEN_SIZE[1] else
             # doesn't leave
             0)
        )


    def move(self, inputs, teleports):
        all_platform_rects = PlatformRects.find()
        # Unpack the inputs
        keys, has_clicked = inputs

        # accelerate the character downwards
        self.velocity[1] += Constants.GRAVITY

        # make sure aim has at least some value
        aim = None

        if not self.is_enemy:
            # if left and right cancel each other out, don't move,
            # otherwise, l_or_r = 1 if right, and -1 if left
            l_or_r = (1 if keys[Constants.RIGHT_BUTTON] else -1) \
                        if keys[Constants.RIGHT_BUTTON] - keys[Constants.LEFT_BUTTON] != 0 else 0

            has_jumped = keys[Constants.JUMP_BUTTON]

            if has_clicked:
                aim = list(pygame.mouse.get_pos())
                self._shoot(list(self.rect.center), aim)

        else:
            # outsource it all to the EnemyMoves file
            l_or_r, has_jumped, aim = EnemyMoves.process(self, player[0])

        # perform actions
        self._move_left_right(l_or_r, all_platform_rects)
        self._jump(has_jumped, all_platform_rects)
        self._shoot(list(self.rect.center), aim)

        # check if the player's left the screen
        if not self.is_enemy:
            self._leaves_screen(teleports)

        # check which way the character is facing
        self.facing = 0 if self.velocity[0] < 0 else 1

        # actually move the rectangle and reset the horizontal movement
        self.rect.move_ip(self.velocity)
        self.velocity[0] = 0

        # make sure the player's level is always the current level
        if not self.is_enemy:
            self.level = GlobalVars.current_level




    def is_hit(self):
        self.lives -= 1
        print(f"{str(self)} was hit! {self.lives} lives left!")

        if self.lives == 0:
            self._die()


    def _die(self):
        print(f"{str(self)} died!")
        self.is_dead = True

        # if an enemy dies, remove any memory of them ever existing
        if self.is_enemy:
            # EnemyDies.process(self)
            active_enemies.remove(self)
            GlobalVars.all_objects.remove(self)

        else:
            GameOver.player_dies()
