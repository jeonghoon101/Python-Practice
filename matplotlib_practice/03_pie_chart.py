import matplotlib.pyplot as plt

subjects = ["Python", "AI", "Math", "English"]
study_time = [4, 3, 2, 1]

explode = [0.1, 0, 0, 0]
colors = ["skyblue", "orange", "green", "pink"]

plt.pie(study_time, labels = subjects, autopct = "%1.1f%%", 
        startangle = 90, counterclock = False, explode = explode,
        shadow = True, colors = colors)

plt.title("Study Time")

plt.show()

subjects = ["Python", "AI", "Math", "English"]
study_time = [12, 18, 7, 5]

explode = [0, 0.1, 0, 0]
colors = ["skyblue", "orange", "green", "pink"]

plt.pie(study_time, labels = subjects, autopct = "%1.1f%%",
        startangle = 90, counterclock = False, explode = explode,
        colors = colors)

plt.title("Weekly Study Time")

plt.show()