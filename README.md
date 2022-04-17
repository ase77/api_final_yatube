# API Yatube
## Описание:
API (от англ. Application Programming Interface, «программный интерфейс приложения») — это интерфейс для обмена данными. Слово «программный» означает, что API служат в первую очередь для взаимодействия программ: с системой взаимодействует не разработчик, а код, написанный им.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git

cd kittygram2plus
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

source env/bin/activate

python3 -m pip install --upgrade pip
```

Установить зависимости из файла `requirements.txt`:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

После запуска проекта, документация к API будет доступна по адресу:


[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Примеры запросов к API:

Получить список всех публикаций. При указании параметров limit и offset выдача будет работать с пагинацией:

```
GET http://127.0.0.1:8000/api/v1/posts/
GET http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=3

{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": "string",
    "group": 0
}
```

Добавление новой публикации. Анонимные запросы запрещены:

```
POST http://127.0.0.1:8000/api/v1/posts/

{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Обновление публикации по id. Обновить публикацию может только автор публикации:

```
PUT http://127.0.0.1:8000/api/v1/posts/{id}/

{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Частичное обновление публикации по id. Обновить публикацию может только автор публикации:

```
PATCH http://127.0.0.1:8000/api/v1/posts/{id}/

{
    "text": "string"
}
```

Удаление публикации по id. Удалить публикацию может только автор публикации:

```
DELETE http://127.0.0.1:8000/api/v1/posts/{id}/
```

Получение всех комментариев к публикации:

```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0

}
```

Добавление нового комментария к публикации. Анонимные запросы запрещены:

```
POST http://127.0.0.1:8000/api/v1/posts/{id}/

{
    "text": "string"
}
```

Получение списка доступных сообществ:

```
GET http://127.0.0.1:8000/api/v1/groups/

{
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
}
```

Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены:

```
GET http://127.0.0.1:8000/api/v1/follow/

{
    "user": "string",
    "following": "string"
}
```

Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены:

```
POST http://127.0.0.1:8000/api/v1/follow/

{
    "following": "string"
}
```

Получение JWT-токена:

```
POST http://127.0.0.1:8000/api/v1/jwt/create/

{
    "username": "string",
    "password": "string"
}
```
