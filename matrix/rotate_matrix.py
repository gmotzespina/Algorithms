

def rotate(matrix, degrees = 90):

    rows = len(matrix)
    cols = len(matrix[0])

    r_matrix = [[0 for j in range(cols)] for i in range(rows)]
   
    for times in range(degrees//90):
        for i in range(rows):
            for j  in range(cols):
                r_matrix[j][rows-1-i] = matrix[i][j]
        matrix = r_matrix[:]
    return r_matrix

def rotate_inplace(matrix, degrees = 90):
    pass

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)

matrix = rotate(matrix)

print(matrix)
