import math

def add_vectors(vector_a, vector_b):
    """
    Adds two vectors element-wise.

    Parameters:
    - vector_a: The first vector (list of numbers).
    - vector_b: The second vector (list of numbers).

    Returns:
    A new vector resulting from the element-wise addition.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError('Vectors must have the same number of coordinates')
    return [a + b for a, b in zip(vector_a, vector_b)]

def subtract_vectors(vector_a, vector_b):
    """
    Subtracts one vector from another element-wise.

    Parameters:
    - vector_a: The vector from which to subtract (list of numbers).
    - vector_b: The vector to subtract (list of numbers).

    Returns:
    A new vector resulting from the element-wise subtraction.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError('Vectors must have the same number of coordinates')
    return [a - b for a, b in zip(vector_a, vector_b)]

def dot_product(vector_a, vector_b):
    """
    Calculates the dot product of two vectors.

    Parameters:
    - vector_a: The first vector (list of numbers).
    - vector_b: The second vector (list of numbers).

    Returns:
    The dot product of the two input vectors.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError('Vectors must have the same number of coordinates')
    return sum(a * b for a, b in zip(vector_a, vector_b))

def are_orthogonal(vector_a, vector_b):
    """
    Checks if two vectors are orthogonal (perpendicular).

    Parameters:
    - vector_a: The first vector (list of numbers).
    - vector_b: The second vector (list of numbers).

    Returns:
    True if the vectors are orthogonal, False otherwise.
    """
    return dot_product(vector_a, vector_b) == 0

def vector_length(vector):
    """
    Calculates the length (magnitude) of a vector.

    Parameters:
    - vector: The input vector (list of numbers).

    Returns:
    The length of the input vector.
    """
    return math.sqrt(sum(coord**2 for coord in vector))

def angle_between_vectors(vector_a, vector_b):
    """
    Calculates the angle (in degrees) between two vectors.

    Parameters:
    - vector_a: The first vector (list of numbers).
    - vector_b: The second vector (list of numbers).

    Returns:
    The angle between the two input vectors in degrees.
    """
    length_a = vector_length(vector_a)
    length_b = vector_length(vector_b)
    dot_product_value = dot_product(vector_a, vector_b)
    cos_theta = dot_product_value / (length_a * length_b)
    theta = math.acos(cos_theta)
    return math.degrees(theta)

def scalar_multiply(scalar, vector):
    """
    Performs scalar multiplication on a vector.

    Parameters:
    - scalar: The scalar value (number) by which to multiply the vector.
    - vector: The input vector (list of numbers).

    Returns:
    A new vector resulting from the scalar multiplication.
    """
    return [scalar * coord for coord in vector]

def unit_vector(vector):
    """
    Calculates the unit vector of a given vector.

    Parameters:
    - vector: The input vector (list of numbers).

    Returns:
    The unit vector of the input vector.
    """
    length = vector_length(vector)
    return scalar_multiply(1/length, vector)

def are_parallel(vector_a, vector_b):
    """
    Checks if two vectors are parallel.

    Parameters:
    - vector_a: The first vector (list of numbers).
    - vector_b: The second vector (list of numbers).

    Returns:
    True if the vectors are parallel, False otherwise.
    """
    unit_vector_a = unit_vector(vector_a)
    unit_vector_b = unit_vector(vector_b)
    return unit_vector_a == unit_vector_b

def project_a_to_b(vector_a, vector_b):
    """
   Calculates the projection of vector_a onto vector_b.

     Parameters:
    - vector_a: The vector to be projected (list of numbers).
    - vector_b: The vector onto which to project (list of numbers).


    Returns:
    The projection of vector_a onto vector_b.
    """
    unit_vector_b = unit_vector(vector_b)
    result = scalar_multiply(dot_product(vector_a, unit_vector_b), unit_vector_b)
    return result

def orthogonal_component_of_a_onto_b(vector_a, vector_b):
    """
    Calculates the orthogonal component of vector_a onto vector_b.

    Parameters:
    - vector_a: The vector to be decomposed (list of numbers).
    - vector_b: The vector along which to find the orthogonal component (list of numbers).

    Returns:
    The orthogonal component of vector_a onto vector_b.
    """
    projection_of_a_onto_b = project_a_to_b(vector_a, vector_b)
    orthogonal_component = subtract_vectors(vector_a, projection_of_a_onto_b)
    return orthogonal_component
def cross_product(vector_a, vector_b):
    """
    Calculates the cross product of two 3D vectors.

    Parameters:
    - vector_a: The first 3D vector (list of numbers with length 3).
    - vector_b: The second 3D vector (list of numbers with length 3).

    Returns:
    The cross product of vector_a and vector_b.
    """
    if len(vector_a) != 3 or len(vector_b) != 3:
        raise ValueError('Cross product is defined only for 3D vectors')
    
    result = [
        vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1],
        vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2],
        vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    ]
    
    return result

