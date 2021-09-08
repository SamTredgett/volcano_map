import folium, pandas

data_frame = pandas.read_csv('Volcanoes.txt')
map = folium.Map(location=[37.7749,-122.4914], zoom_start=6, tiles="Stamen Terrain")

# pulling information from the data frame into python list objects for the sake of speed. 
lat = list(data_frame['LAT'])
lon = list(data_frame['LON'])
volcano_names = list(data_frame['NAME'])
status = list(data_frame['STATUS'])
elevation = list(data_frame['ELEV'])
volcano_type = list(data_frame['TYPE'])

def color_decider(elevation:float):
	'''
	The color_decider function returns a string to define which colour a marker will be
	when it is attached to an instance of a volcano in the data set. This is decided against
	the value of the elevation of the volcano. 
	'''
	if elevation in range(0,1500):
		return 'green'
	elif elevation in range(1500,3000):
		return 'orange'
	else:
		return 'red'


# Generate Feature Group
fg=folium.FeatureGroup(name="My Map")
# Iterate through a list of coordinates and plot markers in each location with a popup message
for latitude, longitude, name, stat, elev, volc_type in zip(lat,lon,volcano_names,status,elevation,volcano_type):
	# Popup string generation
	popup_info : str = f'This volcano is called {name}, and is a {volc_type} that stands at {elev}m tall. ({stat})'
	# Add the marker
	fg.add_child(folium.CircleMarker(location=[latitude,longitude],radius=8.0,popup=popup_info, fill_color=color_decider(elev), fill_opacity=0.8))
fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))

# Add the featuregroup of markers to map
map.add_child(fg)

# create map file
map.save("Map1.html")
