import plotly.express as px

from die import Die

#Make a six-side Die
die1 = Die()
die2 = Die(num_sides=10)

# Make some rolls, and store results in a list.
results = []

title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}

for roll in range(50001):
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

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

#df = px.data.tips()
#fig = px.pie(df, values=frequencies, names=poss_results)

#fig.show()

fig.write_image('/home/dev_net/Desktop/Curso_Python/files/D6D10_2.pdf', 'pdf')

#fig.write_json('/home/dev_net/Desktop/Curso_Python/files/D6D10_1.json')

