from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=3))
])

pipeline.fit(x_train, y_train)

y_pred = pipeline.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

print(f"모델 정확도: {accuracy * 100:.2f}%")
print("Confusion Matrix:")
print(cm)
print("클래스 이름:", iris.target_names)

from sklearn.metrics import classification_report

report = classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)

print("\nClassification Report:")
print(report)

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    display_labels=iris.target_names,
    cmap="Blues",
    values_format="d"
)

plt.title("Iris Confusion Matrix")
plt.tight_layout()
plt.savefig("iris_confusion_matrix.png", dpi=300)
plt.show()