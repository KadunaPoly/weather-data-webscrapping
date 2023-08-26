-- Création du keyspace
CREATE KEYSPACE IF NOT EXISTS weather_data WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};


-- Création de la table pour stocker les données météo
CREATE TABLE IF NOT EXISTS weather_records (
    id UUID PRIMARY KEY,
    city TEXT,
    country TEXT,
    temperature FLOAT,
    temp_max FLOAT,
    temp_min FLOAT,
    humidity INT,
    pressure INT,
    sky TEXT,
    sunrise TIMESTAMP,
    sunset TIMESTAMP,
    wind FLOAT,
    wind_deg FLOAT,
    dt TIMESTAMP,
    cloudiness INT
);
