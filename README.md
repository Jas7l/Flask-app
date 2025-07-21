## Содержимое проекта
### Flask: port 5000
```
@user_bp.route("/api/user/login", methods=["POST"]) - вход пользователя в учётную запись
@user_bp.route("/api/user/logout", methods=["POST]) - выход пользователя из учётно записи
@user_bp.route("/api/user/register", methods=["POST"]) - создание учётной записи и добавление её в базу данных
@user_bp.route("/api/user/info", methods=["GET"]) - возвращает JSON по авторизованному пользователю 
@user_bp.route("/api/user/update/<int:orbis_id>", methods=["PATCH"]) - обновить информацию о пользователе
@user_bp.route("/api/user/delete/<int:orbis_id>", methods=["DELETE"]) - устанавливает поле пользователя active в False, что не даёт авторизироваться
@user_bp.route("/api/user/email", methods=["POST"]) - отправка отчёта на email
```

### Postgres data base: port 5432
#### Настройка в .env

### pgAdmin 4: port 8080
#### Для просмотра базы данных и взаимодействия с ней

## Установка и запуск
### Клонирование репозитория
```bash
git clone https://github.com/Jas7l/Flask-app.git
cd Flask-app
```

### Настройка .env
#### Создание .env
```bash
New-Item -Name ".env" -ItemType "File"
```
#### Настройки .env для дебага
```bash
POSTGRES_USER=str
POSTGRES_PASSWORD=str
POSTGRES_DB=str
POSTGRES_HOST=db
POSTGRES_PORT=5432

SECRET_KEY=str
DEBUG=True

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=yourmail@gmail.com
MAIL_PASSWORD=password_for_app
MAIL_DEFAULT_SENDER=yourmail@gmail.com
MAIL_SUPPRESS_SEND=True
```

### Запуск Docker
```bash
docker compose build --no-cache
docker compose up
```

