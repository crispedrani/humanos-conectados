DROP TABLE IF EXISTS coordenadas;


CREATE TABLE coordenadas (
  coord_id INTEGER PRIMARY KEY AUTOINCREMENT,
  coord_coord TEXT,
  coord_tiempo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

