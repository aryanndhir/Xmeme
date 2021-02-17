#!/bin/bash

cd src/django_project

# Setup DB or any other environment variables you want to setup.

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 8081