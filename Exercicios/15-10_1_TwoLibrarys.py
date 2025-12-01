import plotly.express as px
import pandas as pd

from random_walk import RandomWalk

# Make a random walk.n
rw = RandomWalk(10_000)
rw.fill_walk()

title = "Results of Random Walk"

df = pd.DataFrame({"x" : rw.x_values,
                  "y" : rw.y_values})

#Visualize the results.
fig = px.scatter(df, x="x", y="y", title=title, color_discrete_sequence=["steelblue"])

fig.update_xaxes(visible=False)
fig.update_yaxes(visible=False)

fig.show()