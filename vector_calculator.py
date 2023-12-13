import math

#adds vector1 and vector2 and returns the result
def addVectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise IndexError('Vectors must have the same numbers of coordinates')   
    else:
        result = []
        for coordinatesTuple in zip(vector1, vector2):
            result.append(sum(coordinatesTuple))
        return result

#adds vector2 from vector1 and returns the result   
def subtractVectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise IndexError('Vectors must have the same numbers of coordinates')   
    else:
        result = []
        for coordinatesTuple in zip(vector1, vector2):
            result.append(coordinatesTuple[0] - coordinatesTuple[1])
        return result

#returns the dot product of vector1 and vector2
def calculateDotProduct(vector1, vector2):
     if len(vector1) != len(vector2):
        raise IndexError('Vectors must have the same numbers of coordinates')   
     else:
        result = 0
        for coordinatesTuple in zip(vector1, vector2):
            result += coordinatesTuple[0] * coordinatesTuple[1]
        return result
#returns whether the two input vectors are orthogonal 
def areOrthogonal(vector1, vector2):
    if calculateDotProduct(vector1, vector2) == 0:
        return True
    return False

#returns the lebgth of the input vector
def calculateLength(vector):
    length = 0
    for coordinate in vector: 
        length += coordinate * coordinate
    return math.sqrt(length)

#return the angle between the two vectors in degrees
def calculateAngleBetweenVectors(vector1, vector2):
    length1 = calculateLength(vector1)
    length2 = calculateLength(vector2)
    dotProduct = calculateDotProduct(vector1, vector2)
    cosTheta = dotProduct / (length1 * length2)
    theta =  math.acos(cosTheta)
    return theta * 180 / math.pi

