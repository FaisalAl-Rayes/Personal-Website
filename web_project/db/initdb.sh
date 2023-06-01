#!/bin/bash

# This is mainly used to practice working with postgres and can be substituted by an out of the box solution,
# such as supplying the POSTGRES_USER and POSTGRES_DB environment variables to get the database for the django website.

set -e

# Create the django user with a set password then create the database.
# Grant privileges and ownership of the database to the django user.
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER $PG_DJ_USER WITH PASSWORD '$PG_DJ_PASSWORD';
	CREATE DATABASE $PG_DJ_DATABASE;
	GRANT ALL PRIVILEGES ON DATABASE $PG_DJ_DATABASE TO $PG_DJ_USER;
	ALTER DATABASE $PG_DJ_DATABASE OWNER TO $PG_DJ_USER;
EOSQL