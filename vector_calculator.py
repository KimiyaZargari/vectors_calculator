import math

def addVectors(vector1, vector2):
    """
    Adds two vectors element-wise.

    Parameters:
    - vector1: The first vector (list of numbers).
    - vector2: The second vector (list of numbers).

    Returns:
    A new vector resulting from the element-wise addition.
    """
    if len(vector1) != len(vector2):
        raise ValueError('Vectors must have the same number of coordinates')
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

def subtractVectors(vector1, vector2):
    """
    Subtracts one vector from another element-wise.

    Parameters:
    - vector1: The vector from which to subtract (list of numbers).
    - vector2: The vector to subtract (list of numbers).

    Returns:
    A new vector resulting from the element-wise subtraction.
    """
    if len(vector1) != len(vector2):
        raise ValueError('Vectors must have the same number of coordinates')
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

def calculateDotProduct(vector1, vector2):
    """
    Calculates the dot product of two vectors.

    Parameters:
    - vector1: The first vector (list of numbers).
    - vector2: The second vector (list of numbers).

    Returns:
    The dot product of the two input vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError('Vectors must have the same number of coordinates')
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

def areOrthogonal(vector1, vector2):
    """
    Checks if two vectors are orthogonal (perpendicular).

    Parameters:
    - vector1: The first vector (list of numbers).
    - vector2: The second vector (list of numbers).

    Returns:
    True if the vectors are orthogonal, False otherwise.
    """
    return calculateDotProduct(vector1, vector2) == 0

def calculateLength(vector):
    """
    Calculates the length (magnitude) of a vector.

    Parameters:
    - vector: The input vector (list of numbers).

    Returns:
    The length of the input vector.
    """
    return math.sqrt(sum(coord**2 for coord in vector))

def calculateAngleBetweenVectors(vector1, vector2):
    """
    Calculates the angle (in degrees) between two vectors.

    Parameters:
    - vector1: The first vector (list of numbers).
    - vector2: The second vector (list of numbers).

    Returns:
    The angle between the two input vectors in degrees.
    """
    length1 = calculateLength(vector1)
    length2 = calculateLength(vector2)
    dotProduct = calculateDotProduct(vector1, vector2)
    cosTheta = dotProduct / (length1 * length2)
    theta = math.acos(cosTheta)
    return math.degrees(theta)

def scalarMultiplication(scalar, vector):
    """
    Performs scalar multiplication on a vector.

    Parameters:
    - scalar: The scalar value (number) by which to multiply the vector.
    - vector: The input vector (list of numbers).

    Returns:
    A new vector resulting from the scalar multiplication.
    """
    return [scalar * coord for coord in vector]

def calculateUnitVector(vector):
    """
    Calculates the unit vector of a given vector.

    Parameters:
    - vector: The input vector (list of numbers).

    Returns:
    The unit vector of the input vector.
    """
    length = calculateLength(vector)
    return scalarMultiplication(1/length, vector)

def areParallel(vector1, vector2):
    """
    Checks if two vectors are parallel.

    Parameters:
    - vector1: The first vector (list of numbers).
    - vector2: The second vector (list of numbers).

    Returns:
    True if the vectors are parallel, False otherwise.
    """
    unit_vector1 = calculateUnitVector(vector1)
    unit_vector2 = calculateUnitVector(vector2)
    return unit_vector1 == unit_vector2
