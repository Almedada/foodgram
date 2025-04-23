🍲 Foodgram — дипломный проект

Foodgram — это веб-приложение для публикации и обмена кулинарными рецептами. Пользователи могут добавлять рецепты, подписываться на авторов, добавлять рецепты в избранное, формировать список покупок по ингредиентам.

🚀 Стек технологий
Backend: Django, Django REST Framework
Database: PostgreSQL
CI/CD: GitHub Actions
Containerization: Docker, Docker Compose
Web Server: Gunicorn + Nginx

📦 Установка и запуск проекта
1. Переменные окружения
Для запуска проекта необходимо создать файл .env в корне проекта со следующими переменными:
<pre lang="env"><code> POSTGRES_DB=example_db_name POSTGRES_USER=example_user POSTGRES_PASSWORD=example_password DB_HOST=db DB_PORT=5432</code></pre>

2. Секреты GitHub (для деплоя)
В разделе Settings > Secrets and variables > Actions необходимо добавить следующие переменные:

DOCKER_LOGIN — логин Docker Hub
DOCKER_PASSWORD — пароль Docker Hub
HOST — IP-адрес сервера
USER — имя пользователя на сервере
SSH_KEY — приватный SSH-ключ для доступа к серверу
SSH_PASSPHRASE — пароль к SSH-ключу (если требуется)

3. CI/CD
При пуше в ветку main будет автоматически выполнен:
Тестирование кода
Сборка и публикация Docker-образов backend и frontend
Копирование конфигурации Nginx и docker-compose-файла на сервер
Деплой на удалённый сервер

4. Запуск
<pre lang="env"><code> docker compose -f infra/docker-compose.local.yml up --build </code></pre>
