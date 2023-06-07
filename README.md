# iq_eq_tests
API Сервис для хранения результатов тестов IQ, EQ.
### Возможности
- Создание теста;  
- Передача результатов IQ теста (возможна только 1 раз);  
- Передача результата EQ теста (возможна только 1 раз);  
- Просмотр результатов.

## Зависимости
 - Python 3.10
 - poetry

## Установка (Windows)
Клонируйте репозиторий
```sh
git clone https://github.com/KuzenkovAG/iq_eq_tests.git
```
Перейдите в каталог
```sh
cd iq_eq_tests/
```
Создание виртуального окружения
```sh
poetry install
```
Запуск виртуального окружения
```sh
poetry shell
```
Применение миграций
```sh
python iq_tests/manage.py migrate
```
Запуск сервера
```sh
python iq_tests/manage.py runserver
```

## Использование

1. Создание теста
```sh
GET: http://127.0.0.1:8000/api/v1/tests/
```
Response
```sh
{
    "login": "7Lc8pEgRkk"
}
```
2. Завершение IQ теста
```sh
POST: http://127.0.0.1:8000/api/v1/tests/<str:login>/finish_iq/
```
Payload
```sh
{
    "result": 1
}
```
3. Завершение EQ теста
```sh
POST: http://127.0.0.1:8000/api/v1/tests/<str:login>/finish_eq/
```
Payload
```sh
{
    "result": ["а", "а", "в", "в", "в"]
}
```
4. Просмотр результатов теста
```sh
GET: http://127.0.0.1:8000/api/v1/tests/<str:login>/
```
Response
```sh
{
    "login": "3ACy99JPQW",
    "iq_test": {
        "result": 1,
        "duration": "00:00:13.725276"
    },
    "eq_test": {
        "result": [
            "а",
            "а",
            "в",
            "в",
            "в"
        ],
        "duration": "00:00:25.511571"
    }
}
```