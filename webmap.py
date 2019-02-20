# TODO: everything
# 1. pip3 install folium

import folium

# Create the basemap layer
geographic_center = [39.8285354,-98.579482]	# LAT north, LONG WEST
basemap = folium.Map(location=geographic_center, zoom_start=4, tiles="Mapbox Bright")

# Create a feature group to add markers.
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[39, -99], popup="Marker message!", icon=folium.Icon(color="blue")))

basemap.add_child(fg)

basemap.save("basemap.html")
