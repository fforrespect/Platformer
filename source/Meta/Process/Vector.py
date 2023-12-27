from math import sqrt


# Some maths to work out the unit vector between two positions
def unit_vector(pos1, pos2):
    # Find the vector itself
    vector = (pos1[0]-pos2[0], pos1[1]-pos2[1])
    # Then find the magnitude of that vector
    vector_mag = magnitude(vector)
    # Then divide each part of the vector by the magnitude, and return it
    #   (as a float)
    return list(map(lambda x: x/vector_mag, vector))


def distance(pos1, pos2):
    # First find the vector itself
    vector = (pos1[0]-pos2[0], pos1[1]-pos2[1])
    # Then find the euclidean distance between the two points
    return magnitude(vector)


def magnitude(vector):
    # Find the euclidean distance between the two points
    return sqrt(vector[0]**2 + vector[1]**2)