import math

def addVectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('Vectors must have the same number of coordinates')
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

def subtractVectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('Vectors must have the same number of coordinates')
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

def calculateDotProduct(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('Vectors must have the same number of coordinates')
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

def areOrthogonal(vector1, vector2):
    return calculateDotProduct(vector1, vector2) == 0

def calculateLength(vector):
    return math.sqrt(sum(coord**2 for coord in vector))

def calculateAngleBetweenVectors(vector1, vector2):
    length1 = calculateLength(vector1)
    length2 = calculateLength(vector2)
    dotProduct = calculateDotProduct(vector1, vector2)
    cosTheta = dotProduct / (length1 * length2)
    theta = math.acos(cosTheta)
    return math.degrees(theta)

def scalarMultiplication(scalar, vector):
    return [scalar * coord for coord in vector]

def calculateUnitVector(vector):
    length = calculateLength(vector)
    return scalarMultiplication(1/length, vector)

def areParallel(vector1, vector2):
    unit_vector1 = calculateUnitVector(vector1)
    unit_vector2 = calculateUnitVector(vector2)
    return unit_vector1 == unit_vector2
