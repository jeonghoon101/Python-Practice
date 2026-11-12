import torch

a = torch.tensor([1, 2, 3, 4, 5])

b = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

zeros = torch.zeros((2, 3))
ones = torch.ones((3, 2))

torch.manual_seed(42)
random_tensor = torch.rand((2, 3))

print("1차원 Tensor:", a)
print("2차원 Tensor:\n", b)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Random:\n", random_tensor)

c = torch.tensor([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Shape of c:", c.shape)
print("Number of dimensions of c:", c.ndim)
print(c[1, 1])
print(c[2, :])
print(c[:, 1])

A = torch.tensor([
    [1, 2],
    [3, 4]
])

B = torch.tensor([
    [5, 6],
    [7, 8]
])

print(A + B)
print(A * B)
print(torch.matmul(A, B))
print(torch.matmul(A, B).shape)
print(A @ B)
