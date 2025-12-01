import plotly.express as px

from die import Die

#Make a six-side Die
die1 = Die()
die2 = Die()

# Make some rolls, and store results in a list.
title = "Results of Rolling a two D8 1,000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}

#Normal Loop
'''results = []
for roll in range(1001):
    result = die1.roll() * die2.roll()
    results.append(result)'''

#List Comprehensions
results = [die1.roll() * die2.roll() for roll in range(101) ]

# Analyze the results.
max_results = die1.num_sides * die2.num_sides
poss_results = range(2, (max_results + 1))

#Normal Loop
'''frequencies = []
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)'''

#List Comprehensions
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

