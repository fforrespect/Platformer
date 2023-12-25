from math import sqrt


def calculate(pos1, pos2):
    vector = (pos1[0]-pos2[0], pos1[1]-pos2[1])
    mag_vector = sqrt(vector[0]**2 + vector[1]**2)
    return list(map(lambda x: x/mag_vector, vector))