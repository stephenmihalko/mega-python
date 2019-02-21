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

# The coordinates of the geographic center of the continental U.S.
geographic_center = [39.8285354,-98.579482]	# LAT north, LONG WEST
basemap = folium.Map(location=geographic_center, zoom_start=4, tiles="Mapbox Bright")

# Create a feature group to add markers.
fgv = folium.FeatureGroup(name="American Volcanoes")

# Get all information as a DataFrame
data = pandas.read_csv("Volcanoes.txt")

# Extract individual columns and store in lists.
lats = list(data["LAT"])
lons = list(data["LON"])
names = list(data["NAME"])
elevs = list(data["ELEV"])

# Zip lists and go through each volcano information.
for lt, ln, nm, el in zip(lats, lons, names, elevs):
	fgv.add_child(folium.Marker(location=[lt, ln], popup=("%s is %s m high" % (nm, el)), icon=folium.Icon(color=pick_color(el)))

basemap.add_child(fgv)

# Have another feature group for map colors.
fgc = folium.FeatureGroup(name="World Population")
fgc.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read()),
	      style_function=lambda x: {"fillColor":"green"} if x["properties"]["POP2005"] < 20000000 else
	      {"fillColor":"orange") if x["properties"]["POP2005"] < 200000000 else {"fillColor":"red"})
				  
basemap.save("map.html")
