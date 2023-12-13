def addVectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise IndexError('Vectors must have the same numbers of coordinates')   
    else:
        result = []
        for coordinatesTuple in zip(vector1, vector2):
            result.append(sum(coordinentsTuple))
        return result

