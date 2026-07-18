import numpy as np

scores = np.array([
    [90, 85, 88],
    [70, 75, 80],
    [95, 90, 100]
])

bonus = np.array([5, 10, 0])

print(scores + bonus)

bonus = np.array([
    [5],
    [10],
    [0]
])

print(scores + bonus)