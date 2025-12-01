import plotly.express as px

from die import Die

#Make a six-side Die
die = Die()

# Make some rolls, and store results in a list.
results = []

title = "Results of Rolling One D6 1,000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}

for roll in range(1001):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []

poss_results = range(1, die.num_sides+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
#df = px.data.tips()
#fig = px.pie(df, values=frequencies, names=poss_results)
fig.show()

