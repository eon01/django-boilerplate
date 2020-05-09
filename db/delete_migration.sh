find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

