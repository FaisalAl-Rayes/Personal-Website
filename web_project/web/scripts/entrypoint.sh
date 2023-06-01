#!/bin/bash

# Serving the site.
/opt/venv/bin/gunicorn MyWebsite.wsgi:application \
                       --bind unix:/run/gunicorn/gunicorn.sock \
                       --workers 3 \
                       --timeout 120 \
                       --log-level info \
                       --access-logfile /var/log/gunicorn/access.log \
                       --error-logfile /var/log/gunicorn/error.log