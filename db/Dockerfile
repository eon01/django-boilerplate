FROM postgres:9.6-alpine
COPY scripts/entrypoint.sh /docker-entrypoint-initdb.d/init-user-db.sh
COPY scripts/reset.sh /reset.sh
#ENTRYPOINT ["/entrypoint.sh"]
