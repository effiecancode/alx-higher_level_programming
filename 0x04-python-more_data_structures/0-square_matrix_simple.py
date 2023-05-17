#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in row] for row in matrix]

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            new_matrix[x][y] = matrix[x][y] ** 2

    return(new_matrix)
