import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(42)

study_hours = rng.uniform(1, 10, 120)
attendance = rng.uniform(60, 100, 120)
assignment = rng.uniform(40, 100, 120)

x = np.column_stack((
    study_hours,
    attendance,
    assignment
))

noise = rng.normal(0, 4, 120)

y = (
    10
    + 3.0 * study_hours
    + 0.25 * attendance
    + 0.35 * assignment
    + noise
)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("전체 데이터 크기:", x.shape)
print("학습 데이터 크기:", x_train.shape)
print("테스트 데이터 크기:", x_test.shape)

print("기울기:", np.round(model.coef_, 4))
print("절편:", round(model.intercept_, 4))

print("실제 점수:", np.round(y_test[:5], 2))
print("예측 점수:", np.round(y_pred[:5], 2))

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

simple_model = LinearRegression()

simple_model.fit(x_train[:, [0]], y_train)

simple_pred = simple_model.predict(x_test[:, [0]])

multiple_pred = y_pred

for name, pred in [
    ("Simple Regression", simple_pred),
    ("Multiple Regression", multiple_pred)
]:
    mae = mean_absolute_error(y_test, pred)
    mse = mean_squared_error(y_test, pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, pred)

    print(f"\n=== {name} ===")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²: {r2:.4f}")

import matplotlib.pyplot as plt

plt.scatter(
    y_test,
    simple_pred,
    color="red",
    marker="o",
    s=50,
    alpha=0.7,
    label="Simple Regression"
)

plt.scatter(
    y_test,
    multiple_pred,
    color="blue",
    marker="o",
    s=50,
    alpha=0.7,
    label="Multiple Regression"
)

min_value = min(y_test.min(), simple_pred.min(), multiple_pred.min())
max_value = max(y_test.max(), simple_pred.max(), multiple_pred.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    color="black",
    linestyle="--",
    label="Perfect Prediction"
)

plt.title("Simple vs Multiple Linear Regression")
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("multiple_regression_comparison.png", dpi=300)
plt.show()