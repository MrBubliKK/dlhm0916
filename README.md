# Развертывание

### 1. Клонируйте репозиторий

Для начала клонируйте репозиторий к к себе:

```bash
SSH:
git@github.com:MrBubliKK/dlhm0916.git

HTTPS:
https://github.com/MrBubliKK/dlhm0916.git
```

### 2. Создайте и активируйте виртуальное окружение

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка POstgreSQL

Если у вас не установлен PostgreSQL, установить командой:

```
sudo apt install postgresql postgresql-contrib
```

После установки PostgreSQL должен автоматически запуститься. Чтобы проверить, что он работает, введите команду:

```
sudo systemctl status postgresql
```

Если команда ничего не вывела, значит PostgreSQL работает корректно.

### 4. Подготовка базы данных

Нужно создать базу данных и пользователя для проекта:

```
CREATE DATABASE project_db;
CREATE USER project_user WITH PASSWORD '1234';
ALTER ROLE project_user SET client_encoding TO 'utf8';
ALTER ROLE project_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE project_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE project_db TO project_user;
```

### 5. Настройка файла pg_hba.conf

Убедитесь, что в файле pg_hba.conf разрешено подключение для пользователя **project_user**. Откройте этот файл ( обычно находится в директории /etc/postgresql/\<version>/main/pg_hba.conf ). В данном файле должна быть прописана следующая строка:

```
local      all       project_user        md5
```

Эта строка разрешает пользователю project_user подключаться к базе данных

### 6. Перезагрузка PostgreSQL

Нужно перезагрузить PostgreSQL, чтобы изменения применились:

```
sudo systemctl restart postgresql
```

### 7. Установите все зависимости

```
pip install -r requirements.txt
```

### 8. Запустите приложение

```
python run.py
```