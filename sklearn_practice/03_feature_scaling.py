from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)

x_test_scaled = scaler.transform(x_test)

print("스케일링 전:", x_train[0])
print("스케일링 후:", x_train_scaled[0])

print("스케일링 후 평균:", x_train_scaled.mean(axis=0))
print("스케일링 후 표준편차:", x_train_scaled.std(axis=0))

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

model_before = KNeighborsClassifier(n_neighbors=5)

model_before.fit(x_train, y_train)

pred_before = model_before.predict(x_test)

acc_before = accuracy_score(y_test, pred_before)

model_after = KNeighborsClassifier(n_neighbors=5)

model_after.fit(x_train_scaled, y_train)

pred_after = model_after.predict(x_test_scaled)

acc_after = accuracy_score(y_test, pred_after)

print(f"스케일링 전 정확도: {acc_before:.4f}")
print(f"스케일링 후 정확도: {acc_after:.4f}")