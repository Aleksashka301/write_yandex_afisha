# Проект Write Yandex Afisha
Скрипт показывает на карте маркера интересных мест. При клике на маркер можно ознакомиться с локацией, посмотреть фото,
почитать описание, узнать контакты и перейти по ссылкам с дополнительной информацией. Добавлять новый контент можно
через админ панель. Ознакомиться с сайтом можно по ссылке https://aleksandr301.pythonanywhere.com/
![image](https://github.com/user-attachments/assets/3a7a513b-4f5e-48c4-8c9d-44d426be2f5b)


## Запуск сайта
### GitHub репозиторий
Для начала необходимо скачать репозиторий
```
git clone https://github.com/Aleksashka301/write_yandex_afisha
```
### Виртуальное окружение
Установка виртуального окружения
```python
python -m venv venv
```
Активировать виртуальное окружение
```
venv\Scripts\activate
```
### Зависимости
Установка зависимостей
```python
pip install -r requirements.txt
```
### Переменные окружения
В корневой папке создать файл `.env` и добавить туда переменные окружения
- `SECRET_KEY` - секретный ключ, не обходимый для безопасной работы сервисов сайта
- `DEBUG` - по умолчание стоит значение `True`, если не планируется доработка сайта нужно поставить значение `False`
- `ALLOWED_HOSTS` - по умолчанию стоит локальный сервер, если имеется домен, то его нужно указать в этой переменной
- `DATABASE_NAME` - название БД
### Создание БД
Для создания БД нужно выполнить команду
```python
python manage.py migrate
```
### Запуск сайта
```python
python manage.py runserver
```
Затем перейти по адресу http://127.0.0.1:8000/. Если в переменной окружения `ALLOWED_HOSTS` прописано доменное имя,
то пройти по адресу доменного имени.
## Админ панель
### Создание суперпользователя
```python
python manage.py createsuperuser
```
Затем заполнить нужные поля
- `Login` - обязательное поле
- `Email` - не обязательное поле
- `Password` - обязательное поле

Войти в админ панель можно по адресу `my_domain/admin`
В админ панели можно создавать новые локации с картинками и описанием.
![image](https://github.com/user-attachments/assets/8d992230-36d9-48cf-99d6-b260c038ac06)
## Добавление локаций
Добавлять локации можно не только через админ панель, но и через `json` файлы. Команда для добавления места
```python
python manage.py load_place http://адрес/файл.json
```
Пример `json` файла:
```
{
    "title": "Название локации",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Краткое описание локации",
    "description_long": "Описание локации",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}
```

