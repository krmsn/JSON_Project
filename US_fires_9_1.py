# Import modules

import json
import numpy as np
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Read the .json file and write its contents to a duplicate, which wwe will make more eadable using "json.dump."

in_file = open("US_fires_9_1.json", "r")
out_file = open("readable_fire_data_9_1.json", "w")
fire_data = json.load(in_file)
json.dump(fire_data, out_file, indent = 4)

# 

list_of_fires = fire_data[:]

print(type(list_of_fires))
print(len(list_of_fires))

brights, lons, lats, hover_texts = [],[],[],[]

for fire in list_of_fires:
    bright = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]
    if bright > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

print("\nBrightness:")
print(brights)
print("\nLongitudes:")
print(lons)
print("\nLatitudes:")
print(lats)

# Below exists a more primitive list:
# data = [Scattergeo(lon = lons, lat = lats)]

# This modular system is comprised of lists and dictionaries.

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [bright / 40 for bright in brights],
        "color": brights,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Brightness"}
    },
}]

my_layout = Layout(title = "Wildfires")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename = "global_fires.html")
