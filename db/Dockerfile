FROM postgres:16.2-bookworm
COPY scripts/init-user-permissions.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init-user-permissions.sh
