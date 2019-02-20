# TODO: everything
# 1. pip3 install folium

import folium

# Create the basemap layer
geographic_center = [39.8285354,-98.579482]	# LAT north, LONG WEST
basemap = folium.Map(location=geographic_center, zoom_start=4, tiles="Mapbox Bright")
basemap.save("basemap.html")
