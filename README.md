### Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source venv/bin/activate
```
### Для корректной работы установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### Выполнить миграции:
```
python3 manage.py migrate
```
### Запустить проект:
```
python3 manage.py runserver
```
### Документация к API проекта:

Перечень запросов к ресурсу можно посмотреть в описании API

```
http://127.0.0.1:8000/redoc/
