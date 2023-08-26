# weather-data-webscrapping
projet data web scrapping

# Projet de Web Scraping et de Base de Données Cassandra

## Introduction
Ce projet vise à démontrer la mise en œuvre du web scraping pour collecter des données météorologiques à partir de sources en ligne et à les stocker dans une base de données Cassandra. Le projet se compose de deux parties principales : un script de web scraping en Python pour collecter les données météorologiques et un environnement Docker contenant une instance de la base de données Cassandra pour stocker ces données.

## Comment Utiliser ce Projet
1. Assurez-vous d'avoir Docker installé sur votre système.
2. Clonez ce dépôt sur votre machine locale.

### Container Cassandra
3. Accédez au dossier "cassandra" et ouvrez le fichier "Dockerfile".
4. Vérifiez que le fichier "database.cql" contient les commandes de création du keyspace et de la table.
5. À l'aide de la commande `docker build`, créez une image Docker pour le conteneur Cassandra.
6. Exécutez le conteneur en utilisant la commande `docker run` et assurez-vous qu'il démarre correctement.

### Crawler Python
7. Accédez au dossier "crawler" et ouvrez le fichier "crawler.py".
8. Assurez-vous que toutes les dépendances requises sont présentes dans le fichier "requirements.txt".
9. Utilisez la commande `pip install -r requirements.txt` pour installer les dépendances.
10. Exécutez le script Python en utilisant la commande `python crawler.py` pour collecter les données météorologiques.

## Conclusion
Ce projet met en évidence l'intégration du web scraping et de la gestion de données à l'aide de Cassandra. En combinant ces technologies, vous pouvez collecter et stocker des données de manière efficace et fiable. N'hésitez pas à explorer et personnaliser ce projet en fonction de vos besoins et à contribuer pour l'améliorer !

Pour toute question ou retour d'information, n'hésitez pas à nous contacter.

