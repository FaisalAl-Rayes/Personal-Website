import os
from .base import *

DEBUG = True

STATIC_ROOT =  "/vol/web/static"

ALLOWED_HOSTS = ["localhost", "web", "proxy"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("PG_DJ_DATABASE", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": config("PG_DJ_USER", default="user"),
        "PASSWORD": config("PG_DJ_PASSWORD", default="password"),
        "HOST": config("DATABASE_HOST", default="localhost"),
        "PORT": config("PGPORT", default="1234")
    }
}