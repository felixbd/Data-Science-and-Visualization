#!/usr/bin/env python3

import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Set the default keymap for navigation
plt.rcParams['keymap.quit'] = ['q', 'escape']


# Load the GeoJSON file
geojson_file = "data/Mobilfunkdaten/Messfahrt1_13.09.2021_HH_Bremen_Direkt_Bremerhaven_Bremen_Direkt_HH/Aussenantennen/data_Bremen_HH/geojson_record_1631542597885_cellular_0.geojson"

# Load the GeoJSON file
gdf = gpd.read_file(geojson_file)

# Plot the GeoJSON data
ax = gdf.plot()

# Add basemap using contextily
ctx.add_basemap(ax,
    # url=ctx.providers.OpenStreetMap.Mapnik,
    crs=gdf.crs)

plt.show()