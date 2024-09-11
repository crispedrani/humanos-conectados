
import sqlite3
from flask import Flask

api_db = Flask(__name__)


@api_db.route('/api/v1/resources/coordenadas/all', methods=['GET'])
def api_db_all():
    # con = sqlite3.connect('database.db')
    # cur = con.cursor()
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
    return conectados


api_db.run(debug=True)
