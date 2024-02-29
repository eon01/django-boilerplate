#!/bin/bash
set -euxo pipefail

{
    echo "Starting script execution..."
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOF
    \x
    CREATE DATABASE proj;
    CREATE USER proj WITH PASSWORD '$POSTGRES_PASSWORD';
    ALTER ROLE proj SET client_encoding TO 'utf8';
    ALTER ROLE proj SET default_transaction_isolation TO 'read committed';
    ALTER ROLE proj SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE proj TO proj;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO proj;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO proj;
    ALTER USER proj CREATEDB;
EOF
} &> /var/log/init-user-permissions.log
