

# Utilisez l'image de base Python 3
FROM python:3

# Définissez l'étiquette du mainteneur
LABEL maintainer="projet_web-scrapping"

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt crawler.py city.list.json /app/

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev

# Installez les dépendances spécifiées dans requirements.txt
RUN pip install -r requirements.txt

# Commande à exécuter lorsque le conteneur démarre
CMD ["python", "./crawler.py"]
