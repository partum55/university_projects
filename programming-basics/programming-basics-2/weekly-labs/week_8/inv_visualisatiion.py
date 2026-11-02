import json
import time
import folium
import requests
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="investor_map")

def get_coordinates(place, retries=3, timeout=10):
    for _ in range(retries):
        try:
            location = geolocator.geocode(place, timeout=timeout)
            if location:
                return location.latitude, location.longitude
        except GeocoderTimedOut:
            time.sleep(1)
    return None, None

m = folium.Map(location=[20, 0], zoom_start=2)
json_files = ['poland.json', 'ukraine.json', 'germany.json']
country_counts = {}
country_mapping = {"United States": "United States of America", "UK": "United Kingdom"}

for file_name in json_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for investor in data.get('result', []):
            skip = False
            for loc in investor.get('locations', []):
                c = loc.get('country', {}).get('name', '')
                if c.lower() == "russia":
                    skip = True
                    break
            if skip:
                continue
            investor_name = investor.get('name', 'Unknown Investor')
            for loc in investor.get('locations', []):
                place = ""
                if loc.get('city') and loc['city'].get('name'):
                    place = loc['city']['name']
                elif loc.get('country') and loc['country'].get('name'):
                    place = loc['country']['name']
                if place:
                    country_name = loc.get('country', {}).get('name', '')
                    mapped_country = country_mapping.get(country_name, country_name)
                    if mapped_country:
                        country_counts[mapped_country] = country_counts.get(mapped_country, 0) + 1
                    lat, lon = get_coordinates(place)
                    if lat and lon:
                        popup_text = f"{investor_name} ({place})"
                        folium.Marker(location=[lat, lon], popup=popup_text, icon=folium.Icon(color="blue", icon="info-sign")).add_to(m)
                    else:
                        print(f"Could not geocode location: {place}")
                else:
                    print(f"No valid location data for investor: {investor_name}")

print("Country counts:", country_counts)
world_geo_url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'
world_geo = requests.get(world_geo_url).json()
df = pd.DataFrame(list(country_counts.items()), columns=['Country', 'Count'])
folium.Choropleth(
    geo_data=world_geo,
    name='Investors Choropleth',
    data=df,
    columns=['Country', 'Count'],
    key_on='feature.properties.name',
    fill_color='Green',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of Investors'
).add_to(m)
folium.LayerControl().add_to(m)
m.save('investor_map.html')
print("Map saved as investor_map.html")
