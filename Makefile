MANAGE := poetry run python manage.py

.PHONY: migrate shell

install:
	poetry install

dev:
	export DJANGO_ENV=development && python manage.py runserver

lint:
	poetry run flake8

start:
	export DJANGO_ENV=production && gunicorn task_manager.wsgi:application

genmigrate:
	@$(MANAGE) makemigrations

migrate:
	python manage.py migrate

migrateconfig:
	export DJANGO_ENV=production && python manage.py migrate

trans:
	django-admin makemessages -l ru

transsave:
	django-admin compilemessages

shell:
	@$(MANAGE) shell

test:
	python manage.py test