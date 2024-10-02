MANAGE := poetry run python manage.py

.PHONY: migrate shell

install:
	poetry install

dev:
	python3 manage.py runserver

lint:
	poetry run flake8

start:
	export DJANGO_ENV=production && poetry run gunicorn --bind 0.0.0.0:8000 task_manager.wsgi:application

genmigrate:
	@$(MANAGE) makemigrations

migrate:
	@$(MANAGE) migrate --database=default 

migrateconfig:
	@$(MANAGE) migrate --database=config

shell:
	@$(MANAGE) shell