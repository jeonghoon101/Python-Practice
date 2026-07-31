import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Line")

plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C"], [3, 5, 2])
plt.title("Bar")

plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3], [3, 2, 5])
plt.title("Scatter")

plt.subplot(2, 2, 4)
plt.pie([30, 40, 30], labels=["A", "B", "C"])
plt.title("Pie")

plt.tight_layout()

plt.show()

plt.subplot(2, 2, 1)
plt.plot([1,2,3,4], [2,4,6,8])
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.bar(["Python","AI","CV"], [90,95,88])
plt.title("Bar Chart")

plt.subplot(2,2,3)
plt.scatter([1,2,3,4,5], [60,68,75,84,92])
plt.title("Scatter Plot")

plt.subplot(2,2,4)
plt.pie([40,35,25], labels=["Python","AI","CV"])
plt.title("Pie Chart")

plt.tight_layout()

plt.show()