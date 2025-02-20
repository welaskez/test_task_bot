## Инструкция по настройке

### 1. Настройка переменных окружения

Не забудьте задать переменную BOT_CONFIG__BOT_TOKEN

```bash
mv bot/.env.example bot/.env
```

```bash
mv tests/.env.test.example tests/.env.test
```

```bash
mv pg_db.env.example pg_db.env
```

### 2. Сборка и запуск приложения
Используйте Docker Compose для сборки и запуска приложения:

```bash
docker compose up --build -d
```

### 3. Заполнение базы данных
После запуска приложения заполните базу данных тестовыми данными:

```bash
docker exec -i postgres psql -U test_admin -d test_db < data.sql
```

### 4. Доступ к админке
http://0.0.0.0:8080/admin
