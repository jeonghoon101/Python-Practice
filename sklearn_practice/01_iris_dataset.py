from sklearn.datasets import load_iris

iris = load_iris()

from sklearn.model_selection import train_test_split

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

from sklearn.neighbors import KNeighborsClassifier

"""model = KNeighborsClassifier(n_neighbors=7)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("예측 결과:", y_pred)
print("실제 결과:", y_test)"""

from sklearn.metrics import accuracy_score

"""accuracy = accuracy_score(y_test, y_pred)

print("모델 정확도:", accuracy)
print("정확도 (%) :", accuracy * 100)"""

for k in [1, 3, 5, 7, 9, 11, 15]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"k={k}일 때 모델 정확도: {accuracy:.4f} ({accuracy * 100:.2f}%)")
