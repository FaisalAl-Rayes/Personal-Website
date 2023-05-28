import os
from .base import *
from decouple import config

DEBUG = False

STATIC_ROOT =  "/vol/web/static"

ALLOWED_HOSTS = ["localhost", "web", "proxy"]

DATABASES = {
    "default": {
        "ENGINE": config("DATABASE_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("PG_DJ_DATABASE", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": config("PG_DJ_USER", default="user"),
        "PASSWORD": config("PG_DJ_PASSWORD", default="password"),
        "HOST": config("DATABASE_HOST", default="localhost"),
        "PORT": config("PGPORT", default="1234")
    }
}

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

# SECURE_BROWSER_XSS_FILTER = True