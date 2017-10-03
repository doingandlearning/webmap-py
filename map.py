import folium

map = folium.Map(location=[50.822530,-0.137163], zoom_start=10, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Fun places")

for 
fg.add_child(folium.Marker(location=[50.816856,-0.136738], popup="Brighton Pier", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save('map.html')