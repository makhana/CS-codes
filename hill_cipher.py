import numpy as np
import sympy as sp
def determinant(matrix):
    # Sarus's rule
    dimension = len(matrix)
    if(dimension != len(matrix[0])): return
    if(dimension == 1):
        return matrix[0][0]
    if(dimension == 2):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    count = 0
    product = 1
    # first pass -> addition
    for num in range(dimension):
        column = count
        row = 0
        count += 1
        for cnt in range(dimension):
            product *= matrix[row][column]
            column = (column+1) % dimension
            row += 1
        det += product
        product = 1
    # second pass -> substraction
    count = dimension - 1
    product = 1
    for num in range(dimension):
        column = count
        row = 0
        count -= 1
        for cnt in range(dimension):
            product *= matrix[row][column]
            column = (column-1) % dimension
            row += 1
        det -= product
        product = 1
    return det

def transpose(matrix):
    dimension = len(matrix)
    j = 0
    while j < dimension - 1:
        i = j + 1
        while i < dimension:
            # swap
            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp
            i += 1
        j += 1

    return matrix

def adjoint(matrix):
    dimension = len(matrix)
    if(dimension == 1):
        return matrix[0][0]

    little_matrix = []
    for i in range(dimension-1):
        little_matrix.append([None for _ in range(dimension-1)])
    new_matrix = []
    for i in range(dimension):
        new_matrix.append([None for _ in range(dimension)])

    cnt = 0
    column = 0
    row = 0
    positive = True
    new_i = 0
    new_j = 0
    while cnt < dimension ** 2:
        little_i = 0
        little_j = 0
        for i in range(len(matrix)):
            if i == row:
                continue
            for j in range(len(matrix[0])):
               if j == column:
                   continue
               else:
                    little_matrix[little_i][little_j]=(matrix[i][j])
                    little_j += 1
                    if(little_j == dimension - 1):
                        little_j %= dimension -1
                        little_i+=1
        if positive:
            new_matrix[new_i][new_j]=(determinant(little_matrix))
            positive = False
        else:
            new_matrix[new_i][new_j]=(-determinant(little_matrix))
            positive = True
        new_j+=1
        if(new_j== dimension):
            new_j%=dimension
            new_i+=1
        column = (column + 1)
        if(column == dimension):
            column = column % dimension
            row += 1
        cnt+=1
    return transpose(new_matrix)
def mul(matrix1, matrix2):

    product_matrix = []
    for i in range(len(matrix1)):
        product_matrix.append([None for _ in range(len(matrix2[0]))])

    product_i = 0
    product_j = 0
    for i in range(len(matrix1)):
        for m2 in range(len(matrix2[0])):
            sum = 0
            for j in range(len(matrix1[0])):
                sum += matrix1[i][j] * matrix2[j][m2]

            product_matrix[product_i][product_j] = sum
            product_j = (product_j + 1) % len(matrix2)
        product_i += 1

    return product_matrix

def modulo_matrix(matrix, mod):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j] % mod

    return matrix

def hill_encrypt(plaintext, key):
    return modulo_matrix(mul(plaintext, key), 26)

def hill_decrypt(ciphertext, key):
    adjoint_key = modulo_matrix(adjoint(key), 26)
    # sympy_key = sp.Matrix(key)
    # sympy_key = sympy_key.inv_mod(26).tolist()
    determinant_key = determinant(key)
    determinant_key = determinant_key % 26
    determinant_key = pow(determinant_key, -1, 26)

    for i in range(len(adjoint_key)):
        for j in range(len(adjoint_key[0])):
            adjoint_key[i][j] = adjoint_key[i][j] * determinant_key

    adjoint_key = modulo_matrix(adjoint_key, 26)
    print(adjoint_key) #inverse matrix of key
    #print(sympy_key)
    return modulo_matrix(mul(ciphertext, adjoint_key), 26)

def main():
    #print(determinant([[2, -3], [5, 3]]))
    #print(transpose([[2, -3, 4], [5, 3, 5], [1, 1, 1]]))
    #print(adjoint([[2, -3, 4], [5, 3, 5], [1, 1, 1]]))
    #print(mul([[2, -3, 4], [5, 3, 5], [1, 1, 1]], [[2, -3, 4], [5, 3, 5], [1, 1, 1]]))
    #print(np.dot([[2, -3, 4], [5, 3, 5], [1, 1, 1]], [[2, -3, 4], [5, 3, 5], [1, 1, 1]]))
    print(hill_encrypt([[24, 14, 20]], [[3, 25, 4], [23, 6, 15], [13, 17, 21]]))
    print(hill_decrypt([[4, 10, 24]], [[3, 25, 4], [23, 6, 15], [13, 17, 21]]))
if __name__ == '__main__':
    main()