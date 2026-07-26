import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7]
scores = [55, 60, 68, 75, 82, 90, 95]

plt.scatter(study_hours, scores, color = "red", marker = "o", s = 50)

plt.title("Study Hours vs Score")
plt.xlabel("study_hours")
plt.ylabel("scores")

plt.show()

temperature = [18, 20, 22, 24, 26, 28, 30]
ice_cream_sales = [45, 52, 60, 66, 73, 80, 90]

plt.scatter(temperature, ice_cream_sales, color = "red", marker = "o", s = 50)

plt.title("Temperature vs Ice Cream Sales")
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales")

plt.show()