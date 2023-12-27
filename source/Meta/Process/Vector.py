from math import sqrt


# Some maths to work out the unit vector between two positions
def unit_vector(pos1, pos2):
    # Find the vector itself
    vector = _vector_from_pos(pos1, pos2)
    # Then find the magnitude of that vector
    vector_mag = magnitude(vector)
    # Then divide each part of the vector by the magnitude, and return it
    #   (as a float)
    return list(map(lambda x: x/vector_mag, vector))


def distance(pos1, pos2):
    # First find the vector itself
    vector = _vector_from_pos(pos1, pos2)
    # Then find the euclidean distance between the two points
    return magnitude(vector)


# l_or_r = 1 if right, -1 if left
def distance_l_r(moving_point, stationary_point, l_or_r):
    x = moving_point[0] + l_or_r, moving_point[1]
    return distance(x, stationary_point)


def magnitude(vector):
    # Find the euclidean distance between the two points
    return sqrt(vector[0]**2 + vector[1]**2)


def _vector_from_pos(pos1, pos2):
    return pos1[0]-pos2[0], pos1[1]-pos2[1]