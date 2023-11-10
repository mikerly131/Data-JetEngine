from matplotlib import pyplot as plt

x_index = range(1, 1001)
y_index = [x**3 for x in x_index]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_index, y_index, c=y_index, cmap=plt.cm.Reds, s=5)
# ax.plot(input_index, squares, linewidth=3)

# Set chart title and label the axes
ax.set_title("Cube Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000000])

# Set size of tick labels
# ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
# plt.savefig('matplotlib_fig_example.png', bbox_inches='tight')