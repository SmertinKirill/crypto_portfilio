# Crypto Portfolio

Crypto Portfolio - это проект, который позволяет пользователям создавать виртуальные портфели и отслеживать динамику их криптовалютных активов. С помощью этого пользователи могут добавлять свои транзакции, включая покупки и продажи криптовалют, и получать полезную информацию о своих портфелях.

## Основные возможности

- Регистрация и аутентификация пользователей: Пользователи могут создавать учетные записи и входить в систему для доступа к своим портфелям.
- Добавление транзакций: Пользователи могут добавлять свои транзакции, указывая детали операции, такие как валюта, количество, цена и тип операции (покупка или продажа).
- Отслеживание динамики активов: Пользователи могут видеть актуальные цены криптовалют и отслеживать динамику изменения стоимости своих активов в портфеле.
- Расчет общего профита и убытка: Приложение предоставляет информацию о общем профите или убытке пользователя на основе его транзакций.

### Техническое описание проекта
+ http://127.0.0.1/ - сам проект
+ http://127.0.0.1/admin/ - админ панель


## Технологии:
![Django](https://img.shields.io/badge/Django-3.2-44B78B?logo=django)
![Django REST framework](https://img.shields.io/badge/Django%20REST%20framework-3.12.4-EBB639?logo=django)
![Python](https://img.shields.io/badge/Python-3.7.16-3776AB?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-20.10.7-2496ED?logo=docker)
![CoinMarketCap](https://img.shields.io/badge/CoinMarketCap-API-FF6F00?logo=coinmarketcap)

### Порядок установки
1. В папке инфра создайте файл .env
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME= имя базы данных
POSTGRES_USER= логин для подключения к базе данных
POSTGRES_PASSWORD= пароль для подключения к БД (установите свой)
DB_HOST= название сервиса (контейнера)
DB_PORT=порт для подключения к БД 
SECRET_KEY = секретный ключ
API_KEY = ключ для работы с API CoinMarketCap(https://pro.coinmarketcap.com/account)
```
2. В папке infra выполните команду ```docker-compose up -d --buld```
3. Выполните миграции ```docker-compose exec web python manage.py migrate```
4. Создайте суперпользователя ```docker-compose exec web python manage.py createsuperuser```
5. Соберите статику ```docker-compose exec web python manage.py collectstatic --no-input```
6. Заполните базу криптовалют ```docker-compose exec web python manage.py filldb```

## Разработчик
- [SmertinKirill](https://github.com/SmertinKirill)

