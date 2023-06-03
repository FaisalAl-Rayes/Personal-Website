#!/bin/bash

if [[ -n "${DJANGO_PORT}" ]]; then
    BIND="0.0.0.0:${DJANGO_PORT}"
else
    BIND="unix:/run/gunicorn/gunicorn.sock"
fi

# Serving the site.
/opt/venv/bin/gunicorn MyWebsite.wsgi:application \
                       --bind ${BIND} \
                       --workers 3 \
                       --timeout 120 \
                       --log-level info \
                       --access-logfile /var/log/gunicorn/access.log \
                       --error-logfile /var/log/gunicorn/error.log