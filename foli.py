import folium, pandas
map=folium.Map(location=[21.958016,79.744033], zoom_start=5, tiles='Aakash', attr="hello")
# map=folium.Map(location=[12.958016,77.744033],zoom_start=200,tiles="max")
map.save("mapdraw.html")

