from math import sqrt


# Some maths to work out the unit vector between two positions
def calculate(pos1, pos2):
    # First find the vector itself
    vector = (pos1[0]-pos2[0], pos1[1]-pos2[1])
    # Then find the magnitude of that vector
    mag_of_vector = sqrt(vector[0]**2 + vector[1]**2)
    # Then finally divide each part of the vector by the magnitude, and return it
    #   (as a float)
    return list(map(lambda x: x/mag_of_vector, vector))