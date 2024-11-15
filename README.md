### Hexlet tests and linter status:
[![Actions Status](https://github.com/EugeneAnisimov97/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EugeneAnisimov97/python-project-52/actions)

🔗 [Перейти к проекту](https://python-project-52-ho6p.onrender.com/) | 💻 [Render](https://render.com)

**Task Manager** – система управления задачами, подобная [Redmine](http://www.redmine.org/). Она позволяет ставить задачи, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация.

## Перед установкой
Для установки и запуска проекта вам потребуется Python версии  3.10 и выше, инструмент для управления зависимостями Poetry.


## Установка

1. Склонируйте репозиторий с проектом на ваше локальное устройство:
```
git@github.com:EugeneAnisimov97/python-project-52.git
```
2. Перейдите в директорию проекта:
```
cd python-project-52
```
3. Установите необходимые зависимости с помощью Poetry:
```
poetry install
```
4. Создайте файл .env, который будет содержать ваши конфиденциальные настройки:
```
Определите переменные CONFIG_DATABASE_URL, SECRET_KEY, DJANGO_ENV(Для выбора запуска development)
```

5. Выполните команды: 
```
make migrations
make migrate
```

***

## Использование
Для запуска сервера выполните команду:

```
make start - В рабочем режиме.

make dev - В режиме разработки с активным отладчиком.
```
