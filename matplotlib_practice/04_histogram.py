import matplotlib.pyplot as plt

scores = [
    60, 62, 65, 67,
    70, 72, 75, 78,
    80, 82, 85, 88,
    90, 92, 95
]

plt.hist(scores, bins = 10, edgecolor = "black", alpha = 0.7)

plt.title("Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()

scores = [
    55, 60, 62, 65, 67,
    68, 70, 72, 73, 75,
    76, 78, 80, 81, 82,
    84, 85, 87, 88, 90,
    91, 92, 94, 96, 98
]

plt.hist(scores, bins = 8, edgecolor = "black", alpha = 0.7)

plt.title("Exam Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()