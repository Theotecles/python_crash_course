import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='Blue', cmap=plt.cm.Blues, s=10)

# SET CHART TITLE AND LABELS
ax.set_title("Scatter plot of numbers 1 through 5 and their cubes", fontsize=18)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# SET SIZE OF TICK LABELS
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

import matplotlib.pyplot as plt

x_values = range(1, 5001d)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax1 = plt.subplots()
ax1.scatter(x_values, y_values, c='Blue', cmap=plt.cm.Blues, s=10)

# SET CHART TITLE AND LABELS
ax1.set_title("Scatter plot of numbers 1 through 5 and their cubes", fontsize=18)
ax1.set_xlabel("Value", fontsize=14)
ax1.set_ylabel("Square of Value", fontsize=14)

# SET SIZE OF TICK LABELS
ax1.tick_params(axis='both', which='major', labelsize=14)

plt.show()