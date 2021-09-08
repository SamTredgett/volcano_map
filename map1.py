import folium
map = folium.Map(location=[51.5074,0.1278], zoom_start=6, tiles="Stamen Terrain")

# Generate Feature Group
fg=folium.FeatureGroup(name="My Map")
# Iterate through a list of coordinates and plot markers in each location with a popup message
for coordinates in [[51.5074,0.1278], [50,0]]:
	fg.add_child(folium.Marker(location=coordinates,popup="I'm a marker!", icon=folium.Icon(color='green')))

# Add the featuregroup of markers to map
map.add_child(fg)

# create map file
map.save("Map1.html")
