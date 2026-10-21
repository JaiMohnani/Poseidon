import requests

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
response = requests.get(url)
data = response.json()

# Extract the features list from the GeoJSON response
features = data.get("features", [])

print(f"Displaying the first 10 earthquakes out of {len(features)} total:\n" + "-" * 50)

# Loop over the first 10 features
for i, feature in enumerate(features[:10], 1):
    properties = feature.get("properties", {})
    geometry = feature.get("geometry", {})
    
    place = properties.get("place")
    mag = properties.get("mag")
    
    # HINT: GeoJSON standard specifies coordinates as [longitude, latitude, depth]
    # This is the reverse of the common (latitude, longitude) mapping convention!
    coords = geometry.get("coordinates", [])
    longitude = coords[0] if len(coords) > 0 else None
    latitude = coords[1] if len(coords) > 1 else None

    print(f"{i}. Place     : {place}")
    print(f"   Magnitude : {mag}")
    print(f"   Longitude : {longitude}")
    print(f"   Latitude  : {latitude}")
    print("-" * 50)