import matplotlib.pyplot as plt

subjects = ["Python", "AI", "CV", "ML"]
scores = [90, 95, 88, 85]

plt.bar(subjects, scores, color="skyblue", edgecolor= "black")

plt.title("AI Study Scores")
plt.xlabel("Subject")
plt.ylabel("Score")

plt.grid(axis="y")

plt.savefig("ai_study_scores.png", dpi=300)

plt.show()