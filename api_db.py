
import sqlite3
from flask import Flask, request, jsonify, g


api_db = Flask(__name__)

DATABASE = 'database.db'


# función para conectar a la base de datos
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # para que los resultados se conviertasn en diccionarios
        db.row_factory = sqlite3.Row
    return db


# Convierte filas en diccionarios
def row_to_dict(row):
    return dict(row)


# Cierra la conexion a la base cuando temina la solicitud
@api_db.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def db_init():
    with api_db.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE coordenadas(
            coord_id INTEGER PRIMARY KEY AUTOINCREMENT,
            coord_coord TEXT,
            coord_tiempo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    with open('conectados.txt') as conectadosf:
        conectados = conectadosf.readlines()
    for conectado in conectados:
        db.execute("INSERT INTO coordenadas (coord_coord) VALUES(?)", (conectado.removesuffix("\n")))
    db.commit()


# agregar coordenada
@api_db.route('/api/v1/resources/coordenadas/coord', methods=['POST'])
def post_coord():
    db = get_db()
    nueva_coord = request.json
    coord = nueva_coord.get('coord')

    if not coord:
        return jsonify({"error": "Es necesario ingresar la latitud, coma, la longitud"}), 400

    try:
        db.execute('INSERT INTO coordenadas (coord_coord) VALUES (?)', (coord,))
        db.commit()
        return jsonify({"message":"coordenada agregada correctamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "se debe ingresar latitud y longitud, separadas por coma"}), 400


@api_db.route('/api/v1/resources/coordenadas/coords', methods=['GET'])
def api_db_coords():
    # con = sqlite3.connect('database.db')
    # cur = con.cursor()
    # carga los datos
    # conexion a la base sqlite
    db = get_db()

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
    return conectados


api_db.run(debug=True, port=5002)
