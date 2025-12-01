import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    # Make a random walk.n
    rw = RandomWalk(10_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(19, 10), dpi=92)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.cool,edgecolors=None, s=1)
    ax.scatter(0, 0,c='green',  edgecolors=None, s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],c='red', edgecolors=None, s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')

    plt.show()

    keep_running = input("Make another walk ? (y/n): ")
    if keep_running == 'n':
        break