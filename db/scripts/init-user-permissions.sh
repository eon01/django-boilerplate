#!/bin/bash
set -euxo pipefail

{
    echo "Starting initialization of user permissions on DB"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOF
    \x
    CREATE DATABASE boilerplate;
    CREATE USER boilerplate WITH PASSWORD '$POSTGRES_PASSWORD';
    ALTER ROLE boilerplate SET client_encoding TO 'utf8';
    ALTER ROLE boilerplate SET default_transaction_isolation TO 'read committed';
    ALTER ROLE boilerplate SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE boilerplate TO boilerplate;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO boilerplate;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO boilerplate;
    ALTER USER boilerplate CREATEDB;
EOF
} || {
    echo "Error occurred during initialization of user permissions on DB"
    exit 1
}
