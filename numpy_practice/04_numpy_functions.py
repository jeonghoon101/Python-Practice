import numpy as np

scores = np.array([
    [90, 85, 88],
    [70, 75, 80],
    [95, 90, 100]
])

print(scores.sum())
print(scores.mean())
print(scores.max())
print(scores.min())
print(scores.mean(axis=0))
print(scores.sum(axis=1))
print(scores[1].mean())

a = np.zeros((3, 4))
print(a)

b = np.ones((2, 3))
print(b)

print(np.arange(5))
print(np.arange(2, 8))
print(np.arange(0, 10, 2))

c = np.arange(12)
print(c)
d = c.reshape((3, 4))
print(d)

import sys

print("Python:", sys.executable)
print("NumPy 위치:", np.__file__)
print("NumPy 버전:", np.__version__)