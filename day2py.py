import requests

# USGS GeoJSON feed for all earthquakes in the past day
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

# Make the HTTP GET request
response = requests.get(url)

# Print the HTTP status code (200 means success)
print("HTTP Status Code:", response.status_code)

# Parse the response as JSON and print its top-level keys
data = response.json()
print("Top-level keys:", list(data.keys()))