REM Set up the website.
START /B /WAIT docker compose up -d --build

REM Collect the static files for the visuals.
START /B /WAIT docker exec -it django-server sh /home/django/my-website-project/collectstatic.sh

REM Migrate to the database and create a django superuser.
START /B /WAIT docker exec -it django-server sh /home/django/my-website-project/migrate.sh