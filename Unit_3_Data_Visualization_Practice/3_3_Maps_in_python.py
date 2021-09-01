# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Maps in Python

# %% import modules
import pyproj
import folium
import pandas as pd
import json
import requests

## Transformation

# %% initialize two different coordinate reference systems
wgs84=pyproj.crs.CRS("EPSG:4326")
utm2=pyproj.crs.CRS("EPSG:25832")

# print the transformation from WGS 84 coordinate to UTM zone 2 coordinate
print(pyproj.transform(wgs84, utm2, 63.983, -19.700))

'''(-867097.0776402762, 7411959.0010131905)'''

## Simple markers

# %% center coordinates of map [latitude, longitude]
coords = [52.520008, 13.404954]

# %% Create the map
map = folium.Map(location = coords)

# %% show the map
map

# %% Save the map
map.save("map.html")

# %% create the map
map = folium.Map(location = coords, tiles = 'Stamen Toner')

# %% generate coordinates for markers
marker1 = [52.515816, 13.454293]
marker2 = [52.48388, 13.3477]

# %% add markers
folium.Marker(marker1, popup = 'Marker 1').add_to(map)

# %% add polygon markers
folium.RegularPolygonMarker(marker2, \
    popup = 'Marker 2').add_to(map)

# %% show the map
map

## Polygons

# the data for this example were downloaded from:
# https://github.com/python-visualization/folium/tree/master/examples/data
# on 20.08.2021
# Here is a copy of the license:
# Copyright (C) 2013, Rob Story

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# %% specify the url for the sample data
url = "https://raw.githubusercontent.com/"
url += "python-visualization/folium/"
url += "master/examples/data/"

# %% load geo-data
geo_json_data = json.loads(requests.get(url + "us-states.json").text)

# %% socio-economic data
tab_data = pd.read_csv(url + "US_Unemployment_Oct2012.csv")

# %% create map with specific zoom
map = folium.Map(location=[48, -102], zoom_start=3)

# %% choropleth layer
folium.Choropleth(geo_data=geo_json_data, name="choropleth", \
    data=tab_data,  columns=["State", "Unemployment"], \
    key_on="feature.id", fill_color="YlGn", \
    fill_opacity=0.7, line_opacity=0.2, \
    legend_name="Unemployment Rate (%)").add_to(map)

# %%add layer control
folium.LayerControl().add_to(map)

# %% show the map
map

# %%