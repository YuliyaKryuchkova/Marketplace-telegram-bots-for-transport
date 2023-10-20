# Marketplace-telegram-bots-for-transport

_Маркетплейс телеграм ботов может помочь облегчить коммуникацию между
пассажирами и транспортными компаниями,
предлагая ассортимент ботов для разных нужд._


### Как запустить проект:

* Форкните и клонируйте репозиторий, перейдите
  в командной строке в submodule backend:

```
https://github.com/Marketplace-telegram-bots-for-transport/bots-for-transport
```

```
cd backend
```

Файл workflow уже написан. Он находится в директории backend/.github/workflows/master.yml

* Добавьте секреты в GitHub Actions:

DOCKER_USERNAME                # имя пользователя в DockerHub

DOCKER_PASSWORD                # пароль пользователя в DockerHub

HOST                           # ip_address сервера

USER                           # имя пользователя

SSH_PASSWORD                   # пароль

* Коммитим и пушим изменения на GitHub.

` git add .`

` git commit -m 'твой коммит'`

` git push`

* Создайте папку .env,
перенесите в нее список (указав свои данные) из файла .env.example 


##### Возможные запросы API:


/api/bots/ список ботов

/api/bots/{bot_id}/ratings/ список категорий ботов

/api/users/ регистрация пользователя

/api/users/reset_password/ восстановление пароля

/api/bots/{id}/shopping_cart/ добавление бота в корзину

/api/bots/{id}/favorite/ добавление бота в избранное


#### Команда авторов проекта:

* Александр Морозов - backend разработчик

* Владислав Бунин - backend разработчик

* Екатерина Тарасенко - backend разработчик

* Павел Сарыгин - backend разработчик

* Эльдар Байбанов  - backend разработчик

* Юлия Крючкова  - backend разработчик, тимлид
