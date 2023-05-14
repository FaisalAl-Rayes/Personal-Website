import os
from .base import *

DEBUG = True

STATIC_ROOT =  "/vol/web/static"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}