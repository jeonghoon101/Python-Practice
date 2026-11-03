from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=7))
])

pipeline.fit(x_train, y_train)

y_pred = pipeline.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print("Pipeline 구조:", pipeline)
print(f"Pipeline 정확도: {accuracy:.4f}")
print(f"정확도(%): {accuracy * 100:.2f}%")

from sklearn.model_selection import cross_val_score, StratifiedKFold

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    pipeline,
    x_train,
    y_train,
    cv=cv,
    scoring="accuracy"
)

print("각 Fold 정확도:", scores)
print(f"평균 정확도: {scores.mean():.4f}")
print(f"평균 정확도(%): {scores.mean() * 100:.2f}%")

best_k = None
best_score = -1

for k in range(1, 16, 2):
    pipeline.set_params(knn__n_neighbors=k)

    scores = cross_val_score(
        pipeline,
        x_train,
        y_train,
        cv=cv,
        scoring="accuracy"
    )

    mean_score = scores.mean()

    print(f"K={k}, 평균 정확도: {mean_score:.4f}")
    if mean_score > best_score:
        best_score = mean_score
        best_k = k

print("--------------------------")
print(f"최적 K값: {best_k}")
print(f"최고 평균 정확도: {best_score:.4f}")

pipeline.set_params(knn__n_neighbors=best_k)

pipeline.fit(x_train, y_train)

final_pred = pipeline.predict(x_test)

final_accuracy = accuracy_score(y_test, final_pred)

print(f"최종 K값: {best_k}")
print(f"최종 테스트 정확도: {final_accuracy * 100:.2f}%")