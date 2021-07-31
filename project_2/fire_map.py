import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

     # GET DATES, LONGITUDE, LATITUDE AND BRIGHTNESS
    dates, lons, lats, brightnesses = [], [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[5], '%Y-%m-%d'))
        lons.append(float(row[1]))
        lats.append(float(row[0]))
        brightnesses.append(float(row[2]))

# SET THE TITLE
title = "World Fires 1 Day 9/22/2019"

# MAP THE FIRES
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.025*bright for bright in brightnesses],
        'color': brightnesses,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')