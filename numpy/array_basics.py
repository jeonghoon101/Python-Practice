import numpy as np

# arr = np.array([10, 20, 30])
# print(arr+5)
# print(arr-5)
# print(arr/10)
# print(arr**2)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a+b)
# print(a*b)

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr.shape)

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])
# print(arr[2])
# print(arr[-1])
# print(arr[1:4])
# print(arr[:3])
# print(arr[2:])
# print(arr[::-1])

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(arr[1, 2])
# print(arr[2, 0])

# scores = np.array([
#     [90, 85, 88],
#     [70, 75, 80],
#     [95, 90, 100]
# ])

# print(scores.shape)
# print(scores.ndim)
# print(scores[0])
# print(scores[:, 0])
# print(scores[-1])
# print(scores + 5)

scores = np.array([
    [90, 85, 88],
    [70, 75, 80],
    [95, 90, 100]
])

bonus = np.array([
    [5],
    [10],
    [0]
])

print(scores + bonus)