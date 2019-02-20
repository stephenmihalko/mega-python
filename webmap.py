# TODO: pip3 install folium

import pandas
import folium

# Choosing the color of the volcano marker based on elevation.
def pick_color(elevation):
	if elevation < 1000:
		return "green"
	elif elevation < 2000:
		return "yellow"
	elif elevation < 3000:
		return "orange"
	else:
		return "red"

# Create the basemap layer
geographic_center = [39.8285354,-98.579482]	# LAT north, LONG WEST
basemap = folium.Map(location=geographic_center, zoom_start=4, tiles="Mapbox Bright")

# Create a feature group to add markers.
fg = folium.FeatureGroup(name="My Map")

# Get all information as a DataFrame
data = pandas.read_csv("Volcanoes.txt")

# Extract individual columns and store in lists.
lats = list(data["LAT"])
lons = list(data["LON"])
names = list(data["NAME"])
elevs = list(data["ELEV"])

# Zip lists and go through each volcano information.
for lt, ln, nm, el in zip(lats, lons, names, elevs):
	fg.add_child(folium.Marker(location=[lt, ln], popup=("%s is %s m high" % (nm, el)), icon=folium.Icon(color=pick_color(el)))

basemap.add_child(fg)

basemap.save("basemap.html")
