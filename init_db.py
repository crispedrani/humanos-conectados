# adpatado de https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    

cur = connection.cursor()

with open('conectados.txt') as conectadosf:
    conectados = conectadosf.readlines()

for conectado in conectados:
    cur.execute("INSERT INTO coordenadas (coord_coord) VALUES(?)",(((conectado.removesuffix("/n"),))))

connection.commit()
connection.close