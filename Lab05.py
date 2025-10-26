#lab Task 01

import numpy as np


arr = np.array([[0, 1], [2, 3]])

print("Original flattened array:")
print(arr)


flatarr = arr.flatten()


max = flatarr.max()
min = flatarr.min()


print("Maximum value of the above flattened array:", max)
print("Minimum value of the above flattened array:", min)

#Lab Task 02

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)

print("3x3 Matrix with values from 2 to 10:")
print(matrix)

#Lab Task 03

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

float_arr = arr.astype(float)
print("Array converted to a float type:", float_arr)

#Lab Task o4

import numpy as np

M1 = np.array([[5, 5],
               [1, 2]])

M2 = np.array([[0, 1],
               [1, 0]])

result = np.dot(M1, M2)

transpose_result = result.T

print("Matrix M1:")
print(M1)

print("\nMatrix M2:")
print(M2)

print("\nResult of M1 x M2:")
print(result)

print("\nTranspose of the Result:")
print(transpose_result)

#Lab task 05

import numpy as np

A = np.array([
    [6, 1, 1, 3],
    [4, -2, 5, 1],
    [2, 8, 7, 6],
    [3, 1, 9, 7]
])

print("Original Matrix:")
print(A)

A_inv = np.linalg.inv(A)

print("\nInverse of the Matrix:")
print(A_inv)

