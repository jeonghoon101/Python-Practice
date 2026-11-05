import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(42)

hours = np.linspace(1, 12, 60)
noise = rng.normal(0, 5, size=60)

x = hours.reshape(-1, 1)
y = 35 + 4 * hours + noise

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("학습 데이터:", x_train.shape)
print("테스트 데이터:", x_test.shape)

print("실제 점수:", np.round(y_test[:5], 2))
print("예측 점수:", np.round(y_pred[:5], 2))

print(f"기울기: {model.coef_[0]:.4f}")
print(f"절편: {model.intercept_:.4f}")

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\n=== Regression Evaluation ===")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")

import matplotlib.pyplot as plt

plt.scatter(
    x_test[:, 0],
    y_test,
    color="blue",
    label="Actual Scores"
)

plt.plot(
    x,
    model.predict(x),
    color="red",
    linewidth=2,
    label="Regression Line"
)

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("linear_regression.png", dpi=300)

plt.show()