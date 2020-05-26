#jupyter
# https://blog.prototypr.io/interactive-maps-with-python-part-1-aa1563dbe5a9
# https://nbviewer.jupyter.org/github/vincentropy/python_cartography_tutorial/blob/master/part1_basic_folium_maps.ipynb

# Importing packages
import pandas as pd
import folium
from folium import IFrame
import base64
# from PIL import Image

width, height = 100, 30

# Create the folium map given the locations, zoom and the tiles
folium_map = folium.Map(location=[39.8283, -98.5795],
                        zoom_start=4,
                        tiles="OpenStreetMap")

#Get data from .csv
employee_data = pd.read_csv('VolunCheers Interactive Map.csv')

for index, row in employee_data.iterrows():

    lineLength = 0
    longitude = float(row['Longitude'])
    latitude = float(row['Latitude']) * -1
    info = str(row['Information'])

    breaks = info.count('<br>')

    #print(info.split('<br>'))

    for line in info.split('<br>'):
        if(len(line) > lineLength):
            lineLength = len(line)

    print(lineLength)


    html = "<p style='font-family: Helvetica; font-size: 12pt;'> {} </p>"
    html = html.format(info)

    iFrame = IFrame(html, width=width + (7 * lineLength), height=height + (18 * breaks))

    popup = folium.Popup(iFrame, max_width=2650)

    folium.CircleMarker(location=[longitude, latitude], radius=5,
                        popup=popup, color='#a91f24', fill=True).add_to(folium_map)


# Save the map as html
folium_map.save("SouthernGlazersMap.html")
