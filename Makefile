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
	python manage.py migrate

migrateconfig:
	export DJANGO_ENV=production && python manage.py migrate

trans:
	django-admin makemessages -l ru

shell:
	@$(MANAGE) shell

test:
	python manage.py test