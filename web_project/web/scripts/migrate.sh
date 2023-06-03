#!/bin/bash

# Migrate to the database.
/opt/venv/bin/python /home/django/my-website-project/manage.py migrate --no-input

# Create the django superuser.
/opt/venv/bin/python /home/django/my-website-project/manage.py createsuperuser --no-input || true

# Release the sensitive data that is no longer needed to reduce the area of exposure of this information.
# In this case it doesn't really do much if someone with knowlege about django gets access to the container.
# However it would make their life a little more difficult .
unset DJANGO_SUPERUSER_USERNAME
unset DJANGO_SUPERUSER_PASSWORD
unset DJANGO_SUPERUSER_EMAIL