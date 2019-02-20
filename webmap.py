# TODO: everything
# 1. pip3 install folium

import folium

# Create the basemap layer
the_geographic_center = [39.8285354,-98.579482]	# LAT north, LONG WEST
# TODO: add zoom_level to Map constructor
basemap = folium.Map(location=the_geographic_center)
basemap.save("basemap.html")
