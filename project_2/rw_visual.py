import matplotlib.pyplot as plt

from random_walk import RandomWalk

# KEEP MAKING NEW WALKS AS LONG AS THE PROGRAM IS ACTIVE
while True:
    # MAKE A RANDOM WALK
    rw = RandomWalk(5000)
    rw.fill_walk()

    # PLOT THE POINTS IN THE WALK
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(30, 18))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # EMPHASIZE THE FIRST AND LAST POINTS
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    # REMOVE THE AXES
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break