import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    # ax.scatter(rw.x_index, rw.y_index, s=15)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_index, rw.y_index, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_index[-1], rw.y_index[-1], c='red', edgecolors='none', s=100)

    # Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break