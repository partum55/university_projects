import pandas as pd
import geopandas as gpd
import folium

data = pd.read_csv("tn_nashville_2020_04_01.csv")

m = folium.Map(location=[data['lat'].mean(), data['lng'].mean()], zoom_start=12)

for index, row in data.iterrows():
    folium.Marker(
        [row['lat'], row['lng']],
        popup=f"{row['date']} - {row['violation']} - {row['outcome']}"
    ).add_to(m)

m.save('nashville_map.html')
