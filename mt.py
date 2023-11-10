from matplotlib import pyplot as plt

x_index = range(1, 1001)
y_index = [x**2 for x in x_index]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_index, y_index, c=(0.8, 0.2, 0.2), s=10)
# ax.plot(input_index, squares, linewidth=3)

# Set chart title and label the axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()