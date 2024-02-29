FROM postgres:16.2-bookworm
RUN apt-get update && apt-get install -y vim curl
COPY scripts/init-user-permissions.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init-user-permissions.sh
