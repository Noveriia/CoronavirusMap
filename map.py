# Interactive Corona virus world map
# ITSC 3155 Final Project
# Team Tire Swing (#11): Steven Marsh, Harrison Lee, David Olive, and Alyssa Alameda
# Code modified by Team Tire Swing

import plotly.graph_objects as go
import pandas as pd

####################################################################################################################
# Date Code
####################################################################################################################
def getDate(total):
    day = 0
    month = 1
    dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while total > 0:
        if total > dates[month-1]:
            total -= dates[month-1]
            month += 1
        else:
            day = total
            total = 0

    return str(month) + "/" + str(day) + "/20"


####################################################################################################################
# Map Settings
####################################################################################################################
urlfile="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
df = pd.read_csv(urlfile)

fig = go.Figure(data=go.Choropleth(
    locations=df['Country/Region'], #Set location country/region name in csv file
    #z = df['3/29/20'].astype(int), # Data to be color-coded
    #locationmode = 'country names', #set of locations match entries in `locations`
    #colorscale = 'Greens',
    colorbar_title = "Recovered Cases",
))

####################################################################################################################
# Slider Code
####################################################################################################################

fig = go.Figure()

# Add traces, one for each slider step
# I know all the repetition and if statements are really ugly looking but
# I couldn't figure out how to parse the CSV based on column headers and
# set slider traces based on different columns

for i in range((len(df.iloc[0]))-4):
    fig.add_trace(go.Choropleth(
        locations=df['Country/Region'],  # Set location country/region name in csv file
        z=df[getDate(i+22)].astype(int),  # Data to be color-coded
        locationmode='country names',  # set of locations match entries in `locations`
        colorscale='Greens',#getDate(i+22)
        colorbar_title="Recovered Cases",
        name=getDate(i+22)
    ))

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="restyle",
        args=["visible", [False] * len(fig.data)],
        label = getDate(i+22),
        )
    print("once")
    print(step)
    step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Date: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

####################################################################################################################
# Button Code
####################################################################################################################


####################################################################################################################
# Final Layout Stuff and Map Print
####################################################################################################################

fig.update_layout(
    title_text = 'Coronavirus Recovery 2020'
)

fig.show()
