import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.n
rw = RandomWalk(1000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(19, 10), dpi=92)
point_numbers = range(rw.num_points)
#ax.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.cool,edgecolors=None, s=1)
ax.plot(rw.x_values, rw.y_values, 'r', linewidth=1)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_aspect('equal')

plt.show()