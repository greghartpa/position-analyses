import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel('data/qb-stats.xlsx')

# Primary QB value vs. composite score (passing and rush value)
fig = px.scatter(df, y="AVperFullSeason", x="Composite", hover_data=[df["player"],df["Yr"],df["EPA+CPOE"],df["rushydsper600DB"]],
        trendline="ols", size="base_dropbacks", title="AV per Full Season vs. Passing+Rushing Percentiles")
fig.show()

# Various analyses of QB value vs different metrics
fig = px.scatter(df, y="AVperFullSeason", x="PassComposite", hover_data=[df["player"],df["Yr"],df["EPA+CPOE"],df["rushydsper600DB"]],
        trendline="ols", size="base_dropbacks", title="AV per Full Season vs. Clean Pocket Passer Rating")
fig.show()
fig = px.scatter(df, y="AVperFullSeason", x="CPOE", hover_data=[df["player"],df["Yr"],df["EPA+CPOE"],df["rushydsper600DB"]],
        trendline="ols", size="base_dropbacks", title="AV per Full Season vs. CPOE")
fig.show()
fig = px.scatter(df, y="AVperFullSeason", x="EPA", hover_data=[df["player"],df["Yr"],df["EPA+CPOE"],df["rushydsper600DB"]],
        trendline="ols", size="base_dropbacks", title="AV per Full Season vs. EPA")
fig.show()
fig = px.scatter(df, y="AVperFullSeason", x="EPA+CPOE", hover_data=[df["player"],df["Yr"],df["EPA+CPOE"],df["rushydsper600DB"]],
        trendline="ols", size="base_dropbacks", title="AV per Full Season vs. CPOE+EPA")
fig.show()
