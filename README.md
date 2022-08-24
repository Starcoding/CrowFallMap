# CrowFallMap
Фан проект для создания карты с отметками для добычи ресурсов.

## Установка
Нужно установить Docker Compose и запустить команду ```docker compose up -d --build```

### .env файл
В корневой папке необходимо создать .env файл
Его содержимое:
- ```DEBUG=True```
- ```DATABASE_URL="postgres://crow_user:crow_password@db:5432/crow_maps"```
- ```POSTGRES_USER="crow_user"```
- ```POSTGRES_PASSWORD="crow_password"```
- ```POSTGRES_DB="crow_maps"```

## Настройка
После запуска проекта в докере, необходимо выполнить следующие команды:
- ```docker compose exec web python3 manage.py migrate```
- ```docker compose exec web python3 manage.py collectstatic --no-input```
