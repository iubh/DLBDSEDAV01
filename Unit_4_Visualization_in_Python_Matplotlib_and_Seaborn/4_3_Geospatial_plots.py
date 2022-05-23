# IU - International University of Applied Science
# Exploratory Data Analysis and Visualization
# Course Code: DLBDSEDAV01

# Geo-spatial Plots

# %% import modules
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

## Projections

# %% create visualizations for coastline of the world
# using different projections
fig = plt.figure(figsize=(14, 10))

ax1 = plt.subplot(221, projection=ccrs.PlateCarree())
ax1.coastlines()
ax1.set_title("Plate Carree")

ax2 = plt.subplot(222, projection=ccrs.AlbersEqualArea())
ax2.coastlines()
ax2.set_title("Albers Equal Area")

ax3 = plt.subplot(223, projection=ccrs.LambertCylindrical())
ax3.coastlines()
ax3.set_title("Lambert Cylindrical")

ax4 = plt.subplot(224, projection=ccrs.Mercator())
ax4.coastlines()  
ax4.set_title("Mercator")

plt.show()

## Connection lines in different coordinate systems

# %% create the map
fig = plt.figure(figsize=(14, 6))

# set map projection
ax = plt.axes(projection=ccrs.PlateCarree())

# load basemap
ax.stock_img()

# define coordinates
berlin_lon, berlin_lat = 13.4, 52.5
shanghai_lon, shanghai_lat = 121.4, 31.2

# add annotation for Berlin
plt.text(berlin_lon - 3, berlin_lat - 3, \
    'Berlin', horizontalalignment='right', \
    transform=ccrs.Geodetic(), fontsize=15)

# add annotation for Shanghai
plt.text(shanghai_lon + 3, shanghai_lat - 3, \
    'Shanghai', horizontalalignment='left', \
    transform=ccrs.Geodetic(), fontsize=15)

# plot line using a geodetic transformation
plt.plot([berlin_lon, shanghai_lon], \
    [berlin_lat, shanghai_lat], \
    color='blue', linewidth=2, marker='o', \
    transform=ccrs.Geodetic())

plt.plot([berlin_lon, shanghai_lon], \
    [berlin_lat, shanghai_lat], \
    color='gray', linestyle='--', \
    transform=ccrs.PlateCarree())

plt.show()

## Choropleth map

# %% import modules
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

# %% load sample data
contiguous_usa = gpd.read_file(gplt.datasets.get_path('contiguous_usa'))

# %% create the map
fig = plt.figure(figsize=(14, 6))

# create the choropleth map
ax = gplt.choropleth(contiguous_usa, hue='population', \
    projection=gcrs.AlbersEqualArea(), edgecolor='white', \
    linewidth=1, cmap='Greens', legend=True, scheme='FisherJenks', \
    legend_labels=['<3 million', '3-6.7 million', \
        '6.7-12.8 million', '12.8-25 million', '25-37 million'])

# add a title and show the map
plt.title("Choropleth for population of states of USA")
plt.show()

## Cartogram

# %% create a cartogram
ax = gplt.cartogram(contiguous_usa, scale='population', \
    projection=gcrs.AlbersEqualArea(), limits=(0.2, 1.2), \
    edgecolor='None')

# add county boundaries
gplt.polyplot(contiguous_usa, edgecolor='gray', ax=ax)

## Interactive map

# %% import modules
import folium
import pandas as pd

# %% create the map
m = folium.Map(location=[34.05, -118.24], \
    tiles="cartodbpositron", zoom_start=7)

# save the map to HTML file
m.save("index.html")

# %% Create a data frame with German cities
# with moe than 1 million inhabitants
data = pd.DataFrame({ \
    'lat':[52.31, 53.33, 48.8, 50.56], \
    'lon':[13.23, 10.0, 11.34, 6.57], \
    'name':['Berlin', 'Hamburg', 'Munich', 'Cologne']}, \
        dtype=str)

# %% create empty map
m = folium.Map(location=[50,10], zoom_start=5)

# %% loop through data set and add marker for each city
for i in range(0,len(data)):
    folium.Marker( \
        location=[data.iloc[i]['lat'], \
        data.iloc[i]['lon']], \
        popup=data.iloc[i]['name']).add_to(m)

# save to HTML file
m.save("index.html")

# %%
