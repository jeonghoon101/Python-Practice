import torch

"""
x = torch.tensor(3.0, requires_grad=True)

y = 3 * x ** 2 + 2 * x + 1

y.backward()

print("x", x.item())
print("y", y.item())
print("dy/dx", x.grad.item())
"""

x = torch.tensor(2.0)
target = torch.tensor(10.0)

w = torch.tensor(3.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)

learning_rate = 0.1

y_pred = w * x + b
loss = (y_pred - target) ** 2

print("업데이트 전 Loss:", loss.item())

loss.backward()

with torch.no_grad():
    w -= learning_rate * w.grad
    b -= learning_rate * b.grad

new_pred = w * x + b
new_loss = (new_pred - target) ** 2

print("업데이트 후 w:", w.item())
print("업데이트 후 b:", b.item())
print("업데이트 후 예측값:", new_pred.item())
print("업데이트 후 Loss:", new_loss.item())