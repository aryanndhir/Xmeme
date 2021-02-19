#!/bin/bash

cd django_project/

# Setup DB or any other environment variables you want to setup.

source virtual_env.sh

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

sudo ufw allow 8081

python manage.py runserver localhost:8081
