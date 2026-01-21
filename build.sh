#!/usr/bin/env bash

# Arrêter le script si une commande échoue
set -e

echo "=== Installation des dépendances ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Collecte des fichiers statiques ==="
python manage.py collectstatic --noinput

echo "=== Appliquer les migrations de la base de données ==="
python manage.py migrate
