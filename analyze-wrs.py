import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("data/wr-efficiency.csv")
df['Tm'] = "League"
df.Tm.where((df.TEAM != "PHI"), "PHI", inplace=True)

# Primary WR value vs. composite metric representing WR efficiency (separation + catch % + YAC)
fig = px.scatter(df, y="Composite", x="AdjPositionPct", hover_data=[df["Player"], df["pctAYSEP"], df["pctCTCH"], df["pctYAC"]],
        text="Player", title="WR Player Value vs. Separation/Catch/YAC Score", color="Tm")
fig.update_traces(textposition='top center')
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.add_hline(y=0.50, line_width=1, line_color="grey")
fig.add_vline(x=50, line_width=1, line_color="grey")
fig.update_traces(marker={'size': 10})

fig.update_layout(
    xaxis_title="Separation / Catch / YAC",
    yaxis_title="Player Value Percentile")

fig.show()
