import plotly.express as px

from die import Die

#Make a six-side Die
die1 = Die(8)
die2 = Die(8)

# Make some rolls, and store results in a list.
results = []

title = "Results of Rolling a two D8 1,000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}

for roll in range(1001):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die1.num_sides + die2.num_sides
poss_results = range(2, (max_results + 1))

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
#df = px.data.tips()
#fig = px.pie(df, values=frequencies, names=poss_results)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

