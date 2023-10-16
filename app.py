import folium
import sqlite3
from flask import Flask, render_template
from folium.plugins import MarkerCluster

app = Flask(__name__)





@app.route('/')
def mapa():
    # crea mapa
    f = folium.Figure(height=500,width=520)
    #
    world_map = folium.Map(location=[0,0],tiles="openstreetmap", 
                           zoom_start= 1, min_zoom=1, max_bounds=True).add_to(f)
    # carga los datos
    # conexion a la base sqlite
    connection_obj = sqlite3.connect('database.db')
    
    # objeto cursor
    cursor_obj = connection_obj.cursor()
    
    # para seleccionar el contenido de la tabla de coordenadas
    sentencia = '''select coord_coord from coordenadas'''
    
    # ejecución de la sentencia y obtención de coordenadas
    cursor_obj.execute(sentencia)
    conectados = cursor_obj.fetchall()
    
    # cierre de conexion a la base
    connection_obj.close()
    # mapa vacío.
    marker_cluster = MarkerCluster().add_to(world_map)

    for conectado in conectados:
        latitud, longitud = conectado[0].split(',')
        print(latitud, longitud)
        #print("{}   -  {}".format(latitud,longitud))
        folium.CircleMarker(location = [latitud,longitud], radius=5, fill=True).add_to(marker_cluster)
    # muestra el mapa
    return render_template('mapa.html', mi_map=world_map._repr_html_())

if __name__ == "__main__":
    app.run(debug=True)