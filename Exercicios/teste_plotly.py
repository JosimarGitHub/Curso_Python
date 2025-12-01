import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "tempo": [1,2,3,4,5],
    "temperatura": [22, 24, 23, 26, 28],
    "cidade": ["SP", "SP", "SP", "RJ", "RJ"]
})

fig = px.scatter(
    df,
    x="tempo",
    y="temperatura",
    color="cidade",
    size="temperatura",
    hover_name="cidade"
)

fig.show()
