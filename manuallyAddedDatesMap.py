# Interactive Corona virus world map
# ITSC 3155 Final Project
# Team Tire Swing (#11): Steven Marsh, Harrison Lee, David Olive, and Alyssa Alameda
# Code modified by Team Tire Swing

import plotly.graph_objects as go
import pandas as pd

####################################################################################################################
# Map Settings
####################################################################################################################

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

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

#Array to store trace names
nameList = []
#January
i = 22
while(i < 31):
    fig.add_trace(go.Choropleth(
        locations=df['Country/Region'], #Set location country/region name in csv file
        z = df['1/' + str(i) + '/20'].astype(int), # Data to be color-coded
        locationmode = 'country names', #set of locations match entries in `locations`
        colorscale = 'RdBu',
        colorbar_title = "Recovered Cases",
        name='1/' + str(i) + '/20'
    ))
    nameList.append('1/' + str(i) + '/20')
    i+=1

#February
i = 1
while(i < 29):
    fig.add_trace(go.Choropleth(
        locations=df['Country/Region'], #Set location country/region name in csv file
        z = df['2/' + str(i) + '/20'].astype(int), # Data to be color-coded
        locationmode = 'country names', #set of locations match entries in `locations`
        colorscale = 'RdBu',
        colorbar_title = "Recovered Cases",
        name='2/' + str(i) + '/20'
    ))
    nameList.append('2/' + str(i) + '/20')
    i+=1

#March
i = 1
while(i < 31):
    fig.add_trace(go.Choropleth(
        locations=df['Country/Region'], #Set location country/region name in csv file
        z = df['3/' + str(i) + '/20'].astype(int), # Data to be color-coded
        locationmode = 'country names', #set of locations match entries in `locations`
        colorscale = 'RdBu',
        colorbar_title = "Recovered Cases",
        name='3/' + str(i) + '/20'
    ))
    nameList.append('3/' + str(i) + '/20')
    i+=1

#April
i = 1
while(i < 17):
    fig.add_trace(go.Choropleth(
        locations=df['Country/Region'], #Set location country/region name in csv file
        z = df['4/' + str(i) + '/20'].astype(int), # Data to be color-coded
        locationmode = 'country names', #set of locations match entries in `locations`
        colorscale = 'RdBu',
        colorbar_title = "Recovered Cases",
        name='4/' + str(i) + '/20'
    ))
    nameList.append('4/' + str(i) + '/20')
    i+=1

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="restyle",
        args=["visible", [False] * len(fig.data)],
        label = nameList[i],
    )
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
# Final Layout Stuff and Map Print
####################################################################################################################

fig.update_layout(
    title_text = 'Coronavirus Recovery 2020 - Team 11'
)

fig.show()