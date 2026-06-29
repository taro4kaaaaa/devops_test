## Effective Mobile DevOps Test

Тестовое задание на позицию DevOps-инженера.

---

## Структура проекта

```text
.
├── backend
│   ├── app.py
│   └── Dockerfile
├── nginx
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

---

## Используемые технологии

* Docker
* Docker Compose
* Nginx
* Python 3.12

---

## Запуск проекта

1. Клонировать репозиторий

```bash
git clone https://github.com/taro4kaaaaa/devops_test
```

2. Перейти в директорию проекта

```bash
cd DevOps_Test
```

3. Запустить контейнеры
```bash
docker compose up --build
```

Проверка работоспособности
После запуска выполните команду:
```bash
curl http://localhost
```
Ожидаемый результат:
```bash
Hello from Effective Mobile!
```

---

## Архитектура
```text

           HTTP Request
                │
                ▼
        +----------------+
        |     Nginx      |
        |    Port 80     |
        +----------------+
                │
                │ proxy_pass
                ▼
        +----------------+
        |    Backend     |
        |   Python App   |
        |   Port 8080    |
        +----------------+
```

---

## Схема работы

1. Пользователь отправляет HTTP-запрос на http://localhost.
2. Контейнер Nginx принимает запрос на порту 80.
3. Nginx перенаправляет запрос в контейнер backend по внутренней Docker-сети.
4. Backend-приложение отвечает строкой:

Hello from Effective Mobile!

---

## Особенности реализации

* Backend работает на Python с использованием встроенного HTTP-сервера.
* Backend доступен только внутри Docker-сети.
* Наружу опубликован только порт 80 контейнера Nginx.
* Для обратного проксирования используется Nginx.
* Оркестрация сервисов выполнена с помощью Docker Compose.

---