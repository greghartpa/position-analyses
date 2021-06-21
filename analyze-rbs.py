import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel('data/rb-stats.xlsx')

# Filter out unwanted (low volume) records
df = df[df.Att >= 50]
df = df[df.AVper16G > 0]

# Enrich dataset with 2020 offensive line ranks
data = {
    'Tm':['ARI','ATL','BAL','BUF','CAR',
    'CHI','CIN','CLE','DAL','DEN',
    'DET','GNB','HOU','IND','JAX',
    'KAN','LAC','LAR','MIA','MIN',
    'NOR','NWE','NYG','NYJ','LVR',
    'PHI','PIT','SEA','SFO','TAM',
    'TEN','WAS'],
    'Yr':[2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,
    2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,
    2020,2020,2020,2020,2020,2020,2020,2020],
    'OLRnk':[24,22,14,15,19,
    16,21,1,29,28,
    13,7,27,3,25,
    12,32,4,30,18,
    8,6,23,20,26,
    17,31,9,2,11,
    5,10]}
olrankdf = pd.DataFrame(data)

# Primary model of RB AV vs. Rush YAC + Receiving YAC
fig = px.scatter(df, y="AVper16G", x="RushYAC/RecYAC", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="pctRYOE", trendline="ols", title="RB Value vs. Rush Yds After Contact and Receiving Yards After Catch")
fig.show()

# Compare RB performance to OL rank
df = pd.merge(df, olrankdf, how="left", left_on=["Tm","Yr"], right_on=["Tm","Yr"])
df = df[df.Yr >= 2020]
fig = px.scatter(df, y="YAC/Att", x="OLRnk", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="RYOE", trendline="ols", title="RB YBC vs. RYOE")
fig.show()
fig = px.scatter(df, y="YBC/Att", x="OLRnk", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="RYOE", trendline="ols", title="RB YAC vs. RYOE")
fig.show()
# Team level view of OL rank vs. all RB YBC and YAC
P = df.groupby(['Tm','Yr'])['YBC','YAC'].sum().reset_index()
P = pd.merge(P, olrankdf, how="left", left_on=["Tm","Yr"], right_on=["Tm","Yr"])
P = P[P.Yr >= 2020]
fig = px.bar(P, y="YBC", x="OLRnk", hover_data=[P["Tm"]],
        title="OL Rank vs. YBC")
fig.show()
fig = px.bar(P, y="YAC", x="OLRnk", hover_data=[P["Tm"]],
        title="OL Rank vs. YAC")
fig.show()
# Sorted box plots of team-level YBC and YAC performance
fig = px.box(df, x="Tm", y="YBC/Att", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        title="RB Metrics")
sortedteamsdf = df.groupby(['Tm'], as_index=False)["YBC/Att"].apply(lambda x : x.astype(float).median())
sortedteamsdf.sort_values(by=['YBC/Att'], inplace=True, ascending=False)
tm_array = sortedteamsdf[['Tm']].to_numpy()
fig.update_xaxes(categoryorder='array', categoryarray=tm_array)
fig.show()
fig = px.box(df, x="Tm", y="YAC/Att", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        title="RB Metrics")
sortedteamsdf = df.groupby(['Tm'], as_index=False)["YAC/Att"].apply(lambda x : x.astype(float).median())
sortedteamsdf.sort_values(by=['YAC/Att'], inplace=True, ascending=False)
tm_array = sortedteamsdf[['Tm']].to_numpy()
fig.update_xaxes(categoryorder='array', categoryarray=tm_array)
fig.show()
fig.show()

# Other various analyses
fig = px.scatter(df, y="AVper16G", x="ROE%", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="pctRYOE", trendline="ols", title="RB Value vs. Rush Yds After Contact and Receiving Yards After Catch")
fig.show()
fig = px.scatter(df, y="AVper16G", x="BrkTkl", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="pctRYOE", trendline="ols", title="RB Value vs. Rush Yds After Contact and Receiving Yards After Catch")
fig.show()
fig = px.scatter(df, y="YAC/Att", x="RYOE", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="AVper16G", trendline="ols", title="RB YBC vs. RYOE")
fig.show()
fig = px.scatter(df, y="YBC/Att", x="RYOE", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="AVper16G", trendline="ols", title="RB YAC vs. RYOE")
fig.show()
fig = px.scatter(df, y="AVper16G", x="YBC", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="Rec Value", trendline="ols", title="RB Metrics")
fig.show()
fig = px.scatter(df, y="AVper16G", x="YAC", hover_data=[df["Player"],df["Yr"],df["Att"],df["Yds"]],
        size="Rec Value", trendline="ols", title="RB Metrics")
fig.show()
