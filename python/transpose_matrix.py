'''
Transpose means is to interchange rows and columns of a two-dimensional array matrix.

[AT]ij=[A]ji

ie: Formally, the i th row, j th column element of AT is the j th row, i th column element of A:

Example :

[[1,2,3],[4,5,6]].transpose() //should return [[1,4],[2,5],[3,6]]
Write a prototype transpose to array in JS or add a .transpose method in Ruby or create a transpose function in Python so that any matrix of order ixj 2-D array returns transposed Matrix of jxi .

'''

def transpose(arr):
    matrix_T = []
    for index_row, row in enumerate(arr):
        for index_column, column in enumerate(row):
            if index_row != 0:
                matrix_T[index_column].append(column)
            else:
                matrix_T.append([column])

    return matrix_T

print(transpose([[1,2,3],[4,5,6]]))

