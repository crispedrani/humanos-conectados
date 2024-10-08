# ref: https://flask.palletsprojects.com/en/3.0.x/tutorial/database/
import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'], 
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('shema.sql') as f:
        db.exe(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """ limpia los datos existentes y crea nuevas tablas"""
    init_db()
    click.echo('Base de datos inicializada')

    