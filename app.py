import folium, requests
from flask import Flask, render_template, jsonify
from folium.plugins import MarkerCluster

app = Flask(__name__)


@app.route('/', methods=['GET'])
def mapa():
    # crea mapa
    f = folium.Figure(height=500, width=520)
    #
    world_map = folium.Map(location=[0, 0], tiles="openstreetmap",
                           zoom_start=1, min_zoom=1, max_bounds=True).add_to(f)

    # mapa vacío.
    marker_cluster = MarkerCluster().add_to(world_map)

    # obtiene las coordenadas de la base de datos
    # URL api_db
    db_api_all = 'http://localhost:5002/api/v1/resources/coordenadas/all'
    try:
        # get a todas las coordenadas en la base de datos
        response = requests.get(db_api_all)

        # verificación de la solicitud
        if response.status_code == 200:
            conectados = response.json()
            print(conectados)
        else:
            conectados = response.status_code
        for conectado in conectados:
            latitud, longitud = conectado[0].split(',')
            print(latitud, longitud)
            folium.CircleMarker(location=[latitud, longitud], radius=5, fill=True).add_to(marker_cluster)
        # muestra el mapa
        return render_template('mapa.html', mi_map=world_map._repr_html_())

    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": "Error al conectar a la base"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
