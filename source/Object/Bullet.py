import pygame

from Meta.Process import UnitVector
from Object import Character
from Setup import Constants, GlobalVars, Colours

active_bullets = []


def move_all():
    for b in active_bullets:

        about_to_collide = b.rect.move(b.velocity).collidelist(GlobalVars.all_objects)
        if about_to_collide != -1: # i.e. if it's about to collide (if it's not going to collide with nothing)
            b.hit(GlobalVars.all_objects[about_to_collide])

        b.pos[0] += b.velocity[0]
        b.pos[1] += b.velocity[1]

        b.rect.update(b.pos, b.size)

        # if it leaves the screen, stop rendering it
        if (
                (b.pos[0] - b.size[0]) < 0 or
                (b.pos[0] + b.size[0]) > Constants.SCREEN_SIZE[0] or
                (b.pos[1] - b.size[1]) < 0 or
                (b.pos[1] + b.size[1]) > Constants.SCREEN_SIZE[1]
        ):
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
        self.rect = pygame.Rect(pos, self.size)

        active_bullets.append(self)


    def __str__(self):
        return f"Bullet at pos {(self.rect.left, self.rect.top)}"


    def shoot(self):
        unit_vector = UnitVector.calculate(self.pos, self.aim)

        self.velocity = [-self.speed * unit_vector[0], -self.speed * unit_vector[1]]


    def hit(self, object_hit):
        if (object_hit != self.shooter) and \
           (object_hit != self):

            if isinstance(object_hit, Character.Character):
                object_hit.is_hit()

            active_bullets.remove(self)
            self._explode()


    def _explode(self):
        pass