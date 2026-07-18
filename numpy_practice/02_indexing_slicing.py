import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::-1])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[1, 2])
print(matrix[2, 0])
print(matrix[:, 1])
print(matrix[1, :])