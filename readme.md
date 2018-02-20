# uWSGI приложение
небольшое приложение с использованием uWSGI

### Установка
Создаем virtualenv

````
python -m venv /path/to/new/venv
````

активация окружения
````
cd /path/to/new/venv
. bin/activate
````
установка uWSGI
````
apt-get install python3-dev
pip install uwsgi
````
**!uWSGI Не работает на Windows машинах**

### Запуск
Необходимо запустиь uWSGI с указанием порта скрипта server.py

`uwsgi --http :9090 --wsgi-file server.py`

Запуск из браузера

`http://localhost:9090`
