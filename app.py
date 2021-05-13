import folium
import pandas as pandas
import webbrowser
import pathlib

map = folium.Map(location=[41.5, -115], zoom_start=6)
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


#featureGroup = folium.FeatureGroup(name="My Map")
#map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi, I am a Maker", icon=folium.Icon(color='red')))
#map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi, I am a Maker", icon=folium.Icon(color='red')))
#for coords in [[38.8, -100],[39.0,-101]]:
#    featureGroup.add_child(folium.Marker(location=coords, popup="Hi I am a marker", icon= folium.Icon(color='green')))

def openMap():
    url = str(pathlib.Path("Map3.html").parent.absolute())
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open("file:///" + url + "/Map3.html")

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif elevation<3000:
        return 'orange'
    else:
        return 'red' 


for lt, ln, el in zip(lat, lon, elev):
    if ln>-113.0:
        color = 'blue'
    elif ln>-120:
        color='red'
    else:
        color='green'
    map.add_child(folium.CircleMarker(location=[lt, ln], popup="Earthquake at: lat: %s, long: %s, elevation: %s"%(lt,ln,el) ,radius=6,opacity=0.5, fill_opacity= 0.7, fill_color=color_producer(el)))

#map.add_child(featureGroup)
map.save("Map3.html")
openMap()




