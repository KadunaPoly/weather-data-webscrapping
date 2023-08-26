import json
import urllib.request
import os
import datetime
from cassandra.cluster import Cluster

# Ouvrir une connexion vers le cluster Cassandra
cluster = Cluster(['cassandra-container'])  # Remplacez par le nom du conteneur Cassandra
session = cluster.connect()


# Charger les données des villes depuis le fichier JSON
with open(os.path.join(os.path.dirname(__file__), 'city.list.json'), "r", encoding="utf-8") as file:
    cities_data = json.load(file)

city_ids = []

for city in cities_data:
    country = city["country"]

    if country == "FR":
        city_ids.append(str(city["id"]))

for ids in city_ids:
    user_api = '6e27ee845f9025d79c2c406f5673d6ff'
    unit = 'metric'
    api = 'http://api.openweathermap.org/data/2.5/weather?id='
    full_api_url = api + ids + '&mode=json&units=' + unit + '&APPID=' + user_api

    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()

    data = {
        "id": uuid.uuid1(),
        "city": raw_api_dict.get('name'),
        "country": raw_api_dict.get('sys').get('country'),
        "temperature": raw_api_dict.get('main').get('temp'),
        "temp_max": raw_api_dict.get('main').get('temp_max'),
        "temp_min": raw_api_dict.get('main').get('temp_min'),
        "humidity": raw_api_dict.get('main').get('humidity'),
        "pressure": raw_api_dict.get('main').get('pressure'),
        "sky": raw_api_dict['weather'][0]['main'],
        "sunrise": datetime.datetime.fromtimestamp(int(raw_api_dict.get('sys').get('sunrise'))),
        "sunset": datetime.datetime.fromtimestamp(int(raw_api_dict.get('sys').get('sunset'))),
        "wind": raw_api_dict.get('wind').get('speed'),
        "wind_deg": raw_api_dict.get('wind').get('deg'),
        "dt": datetime.datetime.fromtimestamp(int(raw_api_dict.get('dt'))),
        "cloudiness": raw_api_dict.get('clouds').get('all')
    }

    session.execute("""
        INSERT INTO weather_records (id, city, country, temperature, temp_max, temp_min, humidity, pressure, sky, sunrise, sunset, wind, wind_deg, dt, cloudiness)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data["id"], data["city"], data["country"], data["temperature"], data["temp_max"], data["temp_min"],
        data["humidity"], data["pressure"], data["sky"], data["sunrise"], data["sunset"], data["wind"],
        data["wind_deg"], data["dt"], data["cloudiness"]
    ))

# Fermer la connexion Cassandra
cluster.shutdown()
