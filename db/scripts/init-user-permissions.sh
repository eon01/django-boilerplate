#!/bin/bash
set -euxo pipefail


{
    echo "Starting script execution..."
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    \x
        CREATE DATABASE skriptshift;
        CREATE USER skriptshift WITH PASSWORD '$POSTGRES_PASSWORD';
        ALTER ROLE skriptshift SET client_encoding TO 'utf8';
        ALTER ROLE skriptshift SET default_transaction_isolation TO 'read committed';
        ALTER ROLE skriptshift SET timezone TO 'UTC';
        GRANT ALL PRIVILEGES ON DATABASE skriptshift TO skriptshift;
        GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO skriptshift;
        GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO skriptshift;
        ALTER USER skriptshift CREATEDB;
    EOSQL
} &> /var/log/init-user-permissions.log
