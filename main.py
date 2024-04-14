#!/usr/bin/env python3

import os

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx

from tqdm import tqdm

#%%

plt.rcParams['keymap.quit'] = ['q', 'escape']

#%%

# list all files in the directory
path = "data/Mobilfunkdaten/"

gdf = gpd.GeoDataFrame()

paths = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".geojson"):
            current_path = os.path.join(root, file)

            if not "Aussenantennen" in current_path:  # Aussenantennen or "Innenraum" in current_path:
                continue

            print(f"{current_path = }")
            paths.append(current_path)

for current_path in tqdm(paths):
    temp = gpd.read_file(current_path)
    gdf = pd.concat([gdf, temp], ignore_index=True)

# gdf

#%%

# geojson_file = ("data/Mobilfunkdaten/Messfahrt1_13.09.2021_HH_Bremen_Direkt_Bremerhaven_Bremen_Direkt_HH/"
#                 "Aussenantennen/data_Bremen_HH/geojson_record_1631542597885_cellular_0.geojson")
# gdf = gpd.read_file(geojson_file)

print(f"{gdf.shape = }")  # (518875, 17)

#%%

# gdf

#%%

# plot the geodataframe (with rssi as color)
ax = gdf.plot(column='rssi', legend=True)

# add a basemap
ctx.add_basemap(ax,
                # url=ctx.providers.OpenStreetMap.Mapnik,
                crs=gdf.crs
                )
plt.show()


#%%

# plot the geodataframe (with cell_id as color)
ax = gdf.plot(column='cell_id', legend=True)

# add a basemap
ctx.add_basemap(ax,
                # url=ctx.providers.OpenStreetMap.Mapnik,
                crs=gdf.crs
                )

plt.show()
