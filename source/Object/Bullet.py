import pygame

from Meta.Process import UnitVector
from Object import Character
from Setup import Constants, GlobalVars, Colours

active_bullets = []


# Process the moving of all active bullets
def move_all():
    for b in active_bullets:
        about_to_collide = b.rect.move(b.velocity).collidelist(GlobalVars.all_objects)
        # If it's about to collide (if it's not going to collide with nothing)
        if about_to_collide != -1:
            # The bullet has hit something
            b.hit(GlobalVars.all_objects[about_to_collide])

        # Calculate the new position of the bullet
        b.pos[0] += b.velocity[0]
        b.pos[1] += b.velocity[1]

        # Move the rectangle to that position
        b.rect.update(b.pos, (b.size, b.size))

        # If it leaves the screen, stop rendering it
        if (
                (b.pos[0] - b.size) < 0 or
                (b.pos[0] + b.size) > Constants.SCREEN_SIZE[0] or
                (b.pos[1] - b.size) < 0 or
                (b.pos[1] + b.size) > Constants.SCREEN_SIZE[1]
        ):
            # The try/catch is just to make sure we aren't trying to remove a bullet that doesn't exist
            try:
                active_bullets.remove(b)
            except ValueError:
                pass


class Bullet:
    def __init__(self, shooter, pos, aim):
        self.shooter = shooter
        self.pos = pos
        self.aim = aim

        self.size = Constants.BULLET_SIZE
        self.speed = Constants.BULLET_SPEED
        self.velocity = [None, None]
        self.colour = Colours.MAROON
        self.rect = pygame.Rect(pos, (self.size, self.size))

        # Make sure evey bullet that's instantiated is added to the list of active bullets
        active_bullets.append(self)


    def __str__(self):
        return f"Bullet at pos {(self.rect.left, self.rect.top)}"


    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=self.size)


    def shoot(self):
        unit_vector = UnitVector.calculate(self.pos, self.aim)

        # the speed * the unit vector is how much it should move that frame
        self.velocity = list(map(lambda x: -self.speed*x, unit_vector))


    def hit(self, object_hit):
        # If it hit something that wasn't itself or the character that shot it
        if (object_hit != self.shooter) and \
           (object_hit != self):

            # If it hit a character...
            if isinstance(object_hit, Character.Character):
                # ...and that character wasn't itself...
                if object_hit.is_enemy and object_hit.enemy_hash == self.shooter.enemy_hash:
                    return
                else:
                    # ...run the Character.self.is_hit() function
                    object_hit.is_hit()

            # Regardless of what it hit, it doesn't exist anymore
            active_bullets.remove(self)
            self._explode()

    # To be used later for animation et.
    def _explode(self):
        pass
