# Marketplace-telegram-bots-for-transport

_Маркетплейс телеграм ботов может помочь облегчить коммуникацию между
пассажирами и транспортными компаниями,
предлагая ассортимент ботов для разных нужд._


### Как запустить проект на данном этапе:

* Клонируйте репозиторий и перейдите
  в командной строке в submodule backend:

```
https://github.com/Marketplace-telegram-bots-for-transport/bots-for-transport
```

```
cd backend
```

* Cоздать и активировать виртуальное окружение:

* Если у вас Linux/macOS

```
python3 -m venv env
```

```
source env/bin/activate
```

* Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

* Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python3 manage.py migrate
```

* Запустить локально сервер:

```
python3 manage.py runserver
```

* Cоздать и активировать виртуальное окружение:

* Если у вас windows

```
python -m venv env
```

```
source env/scripts/activate
```

* Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

* Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python manage.py migrate
```

* Запустить локально сервер:

```
python manage.py runserver
```

* Создайте папку .env,
перенесите в нее список для восстановления пароля
(указав свои данные) из файла .env.example 


##### Возможные запросы API:


/api/bots/ список ботов

/api/bots/{bot_id}/ratings/ список категорий ботов

/api/users/ регистрация пользователя

/api/users/reset_password/ восстановление пароля

/api/bots/{id}/shopping_cart/ добавление бота в корзину

/api/bots/{id}/favorite/ добавление бота в избранное


#### Команда авторов проекта:

* Александр Морозов - backend разработчик

* Екатерина Тарасенко - backend разработчик

* Павел Сарыгин - backend разработчик

* Байбанов Эльдар - backend разработчик

* Крючкова Юлия - backend разработчик, тимлид
