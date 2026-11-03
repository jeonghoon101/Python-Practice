from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for k in range(1, 16, 2):
    model = KNeighborsClassifier(n_neighbors=k)

    scores = cross_val_score(
        model,
        x_train,
        y_train,
        cv=cv,
        scoring="accuracy"
    )

    print(f"K={k}, 평균 정확도: {scores.mean():.4f}")

from sklearn.metrics import accuracy_score

final_model = KNeighborsClassifier(n_neighbors=5)

final_model.fit(x_train, y_train)

y_pred = final_model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print("최종 모델 K:", 5)
print(f"최종 테스트 정확도: {accuracy:.4f}")
print(f"정확도(%): {accuracy * 100:.2f}%")