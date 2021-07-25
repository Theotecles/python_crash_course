import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0.3, 0, 0.3), s=10)

# SET CHART TITLE AND LABEL AXES
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# SET SIZE OF TICK LABELS
ax.tick_params(axis='both', which='major', labelsize=14)

#SET THE RANGE FOR EACH AXIS
ax.axis([0, 1100, 0, 1100000])

plt.show()