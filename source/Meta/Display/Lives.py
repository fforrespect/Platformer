from Setup import GlobalVars, Colours


def display():
    lives = GlobalVars.player.lives

    life = Life((0, 0), 200)


class Life:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

        self.colour = Colours.RED

        GlobalVars.all_overlays.append("c", )