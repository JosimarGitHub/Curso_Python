import matplotlib.pyplot as trend

x_values = range(1,5000)
y_values = [x**3 for x in x_values]

fig, ax = trend.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=trend.cm.cool, linewidth=1)

#Set chart title and label axes
ax.set_title("Cubos", fontsize=24)
ax.set_xlabel("Numeros", fontsize=14)
ax.set_ylabel("Cubo dos Numeros", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

trend.show()

