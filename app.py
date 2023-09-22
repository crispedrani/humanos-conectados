from flask import Flask, render_template
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

@app.route('/')
def mapa():
    # crea mapa
    #world_map = folium.Map(tiles="openstreetmap")
    f = folium.Figure(height=500,width=520)
    #
    world_map = folium.Map(location=[0,0],tiles="openstreetmap", 
                           zoom_start= 1, min_zoom=1, max_bounds=True).add_to(f)
    # carga los datos
    with open('conectados.txt') as conectados:
        lines = conectados.readlines()
    # mapa vacío.
    marker_cluster = MarkerCluster().add_to(world_map)

    for line in lines:
        line = line.removesuffix("/n")
        latitud, longitud = line.split(';')
        #print("{}   -  {}".format(latitud,longitud))
        folium.CircleMarker(location = [latitud,longitud], radius=5, fill=True).add_to(marker_cluster)
    # muestra el mapa
    return render_template('mapa.html', mi_map=world_map._repr_html_())

if __name__ == "__main__":
    app.run(debug=True)