## Проект «API Yatube»
---
Проект для знакомства с API, бибилотекой Django REST Framework, Сериализаторами и JWT.

По адресу http://127.0.0.1:8000/redoc/ доступна документация для API Yatube. В документации описано, как должен работать API данного проекта. Документация представлена в формате Redoc.


**Для его создания использовались следующие технологии:**

*Python 3, Django, Django REST Framework, Simple-JWT*


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:chernyh-mv/api_final_yatube.git
```

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```
```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Cоздать базу данных и выполнить миграции

```
cd yatube_api/
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Запустить сервер 
```
python manage.py runserver
```

___
___
*Автор: [Мария Черных](https://github.com/chernyh-mv)*
