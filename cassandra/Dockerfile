# Utilisez l'image officielle Cassandra
FROM cassandra:latest

# Copiez le fichier base.cql dans le conteneur
COPY database.cql /docker-entrypoint-initdb.d/

# Exposez le port Cassandra
EXPOSE 9042

