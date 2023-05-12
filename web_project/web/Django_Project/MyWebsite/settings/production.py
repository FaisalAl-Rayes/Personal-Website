import os
from .base import *
from decouple import config

DEBUG = False

STATIC_ROOT =  "/vol/web/static"

ALLOWED_HOSTS = ["localhost"]

DATABASES = {
    "default": {
        "ENGINE": config("DATABASE_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DATABASE_NAME", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": config("DATABASE_USER", default="user"),
        "PASSWORD": config("DATABASE_PASSWORD", default="password"),
        "HOST": config("DATABASE_HOST", default="localhost"),
        "PORT": config("DATABASE_PORT", default="1234")
    }
}

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

# SECURE_BROWSER_XSS_FILTER = True