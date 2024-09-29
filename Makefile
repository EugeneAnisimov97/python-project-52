MANAGE := poetry run python manage.py

.PHONY: migrate shell

install:
	poetry install

dev:
	python3 manage.py runserver

lint:
	poetry run flake8

start:
	poetry run gunicorn --bind 0.0.0.0:8000 task_manager.wsgi:application

genmigrate:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate --database=default 

migrateconfig:
	poetry run python manage.py migrate --database=config

shell:
	@$(MANAGE) shell