# Using Folium to create webmap in Python3

folium module imported and installed

## Map needs to instantiated with location in terms of lat and long

map = folium.map(location=[lon,lat])

## Folium can export the html required to show this with save method

map.save("map.html")

### Base map layer comes from Open Street map
This can be changed using the tile parameter.

## Adding markers
This can be done individually:

map.add_child(folium.Marker(location=[lon,lat],popup="label", icon=folium.Icon(color='color')))

Or a feature group can be constructed and then added to the map.

fg = folium.FeatureGroup(name="Fun places")
fg.add_child(folium.Marker(location=[lon,lat],popup="label", icon=folium.Icon(color='color')))

map.add_child(fg)
