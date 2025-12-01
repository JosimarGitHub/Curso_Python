import plotly.express as px
import matplotlib.pyplot as plt
import mplcursors
import numpy as np


from die import Die

#Make a six-side Die
die1 = Die()
die2 = Die()

# Make some rolls, and store results in a list.
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}

results = [die1.roll() + die2.roll() for roll in range(1001)]

# Analyze the results.
max_results = die1.num_sides + die2.num_sides
poss_results = range(2, (max_results + 1))

frequencies = [results.count(value) for value in poss_results ]
max_y = max(frequencies)

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(19, 10), dpi=92)
barras = ax.bar(poss_results, frequencies, width=0.8,color='steelblue', edgecolor='white', linewidth=0.1)


ax.set(xlim=(0, max_results+1), xticks=np.arange(2, max_results+1),
       ylim=(0, max_y + 10), yticks=np.arange(1, max_y,10))

ax.set_title(title, fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

cursor = mplcursors.cursor(barras, hover=True)

@cursor.connect("add")
def on_hover(sel):
    index = sel.index
    nome_x = poss_results[index]
    valor_y = frequencies[index]

    # Texto personalizado
    sel.annotation.set_text(f"Result: {nome_x}\nFrequency of Result: {valor_y}")
    sel.annotation.get_bbox_patch().set(fc="steelblue", ec="black", alpha=0.9)

@cursor.connect("remove")
def on_leave(sel):
    # some totalmente
    sel.annotation.set_visible(False)

plt.show()

'''# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()'''

