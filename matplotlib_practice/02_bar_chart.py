import matplotlib.pyplot as plt

subjects = ["Python", "AI", "Math", "English"]
scores = [90, 95, 80, 85]

bars =plt.bar(subjects, scores, color = ["red", "blue", "green", "orange"], 
              edgecolor = "black")

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha = "center",
        va = "bottom"
    )

plt.title("Student Scores")
plt.xlabel("Subject")
plt.ylabel("Score")

plt.grid(axis = "y")

plt.show()

subjects = [
    "Computer Vision",
    "Machine Learning",
    "Deep Learning",
    "NLP"
]

scores = [95, 90, 88, 85]

bars = plt.barh(subjects, scores, color = "skyblue", edgecolor = "black")

for bar in bars:
    width = bar.get_width()

    plt.text(
        width + 1,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.0f}",
        va = "center"
    )

plt.title("AI Skills")
plt.xlabel("Score")
plt.ylabel("Skill")

plt.show()