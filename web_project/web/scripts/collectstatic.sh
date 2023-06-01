#!/bin/bash

# Collecting static files to gather up at the static root which is the static files volume.
/opt/venv/bin/python /home/django/my-website-project/manage.py collectstatic --noinput