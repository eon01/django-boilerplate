psql -h 127.0.0.1 -U postgres <<EOF
\x
REVOKE CONNECT ON DATABASE boilerplate FROM public;  DROP DATABASE boilerplate;  CREATE DATABASE boilerplate;  CREATE USER boilerplate WITH PASSWORD '5726127e9c457001c1075e14078662de';  ALTER ROLE boilerplate SET client_encoding TO 'utf8'; ALTER ROLE boilerplate SET default_transaction_isolation TO 'read committed';  ALTER ROLE boilerplate SET timezone TO 'UTC';  GRANT ALL PRIVILEGES ON DATABASE boilerplate TO boilerplate;
EOF