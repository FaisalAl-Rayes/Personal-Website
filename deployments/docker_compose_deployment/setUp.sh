#!/bin/bash

# Set up the website.
docker compose up -d --build

# Collect the static files for the visuals.
docker exec -it django-server sh /home/django/my-website-project/collectstatic.sh

# Migrate to the database and create a django superuser.
docker exec -it django-server sh /home/django/my-website-project/migrate.sh