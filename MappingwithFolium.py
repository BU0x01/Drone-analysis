import folium

# Simulated location and vegetation percentage
lat, lon = 38.7946, -89.9934  # Replace with real GPS
green_percent = 42.5

m = folium.Map(location=[lat, lon], zoom_start=18)
popup_text = f"Vegetation Health: {green_percent}%"
folium.Marker(location=[lat, lon], popup=popup_text).add_to(m)

m.save("campus_map.html")
