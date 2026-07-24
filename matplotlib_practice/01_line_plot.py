import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color = "red", linewidth = 3, marker = "o", linestyle = "--")

plt.title("My First Graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)

plt.show()

x = [1, 2, 3, 4, 5]
math = [70, 75, 80, 85, 90]
english = [65, 72, 78, 82, 88]

plt.plot(x, math, marker = "o", label = "Math")
plt.plot(x, english, marker = "s", label = "English")

plt.title("Score Comparison")
plt.xlabel("Test")
plt.ylabel("Score")

plt.grid(True)
plt.legend()

plt.show()

x = [1, 2, 3, 4, 5]
python_scores = [60, 70, 75, 85, 90]
ai_scores = [55, 68, 80, 83, 95]

plt.plot(x, python_scores, marker = "o", label = "Python")
plt.plot(x, ai_scores, marker = "s", label = "AI")

plt.title("Python and AI Scores")
plt.xlabel("Test")
plt.ylabel("Score")

plt.grid(True)
plt.legend()

plt.show()