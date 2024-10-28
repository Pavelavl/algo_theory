# Электронная библиотека

## Описание
**Электронная библиотека** - это приложение для отслеживания количества прочитанных страниц, управления читателями, книгами и абонементами. С помощью приложения можно добавлять новых читателей и книги, рассчитывать статистику по прочитанным страницам для различных типов абонементов, а также генерировать отчеты в формате `.docx` или `.xlsx`.

## Структура проекта
./
├── Dockerfile
├── data
│   ├── library.db
│   └── library_test.db
├── docker-compose.yaml
├── library
│   ├── \_\_init\_\_.py
│   ├── book.py
│   ├── reader.py
│   └── subscription.py
├── main.py
├── migrations.sql
├── pytest.ini
├── readme.md
├── requirements.txt
└── tests
    ├── conftest.py
    └── test_main.py

## Функциональность приложения

- **Добавление читателя**: Создание нового пользователя библиотеки.
- **Добавление книги**: Добавление информации о новой книге.
- **Расчет статистики**: Подсчет общего количества прочитанных страниц и оставшихся страниц для бесплатного абонемента.
- **Генерация отчета**: Формирование отчета с данными библиотеки в формате `.docx` или `.xlsx`.

## Зависимости и запуск
```bash
cd .\Lab2
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8081
```

## Тестирование
```bash
pytest --disable-warnings --maxfail=1
```

## Разворачивание в Docker (тесты + приложение)
```bash
docker-compose up --build -d
```

## API-эндпоинты
1. Добавление читателя
> **POST /add_reader/**
> 
> Создает нового читателя в базе данных.
> 
> **Тело запроса:**
> {
>  "name": "Имя читателя"
> }
> **Пример запроса:**
> ```curl -X POST "http://localhost:8000/add_reader/" -H "Content-Type: application/json" -d "{\"name\": \"John Doe\"}"```
> **Ответ:**
> {
>  "message": "Reader John Doe added"
> }

2. Добавление книги
> **POST /add_book/**
> 
> Добавляет новую книгу в базу данных.
> 
> **Тело запроса:**
> {
>  "title": "Название книги",
>  "author": "Автор книги",
>  "pages": 300,
>  "reader_id": 1
> }
> **Пример запроса:**
> ```curl -X POST "http://localhost:8081/add_book/" -H "Content-Type: application/json" -d "{\"title\": \"Test Book\", \"author\": \"Test Author\", \"pages\": 300, \"reader_id\": 1}"```
> **Ответ:**
> {
>   "message": "Book Test Book by Test Author added"
> }


3. Расчет статистики
> **GET /calculate_statistics/**
> 
> Рассчитывает количество прочитанных страниц для читателя и оставшиеся страницы в рамках абонемента.
> 
> **Параметры запроса:**
> reader_id (int): ID читателя.
> subscription_type (string): Тип абонемента (Free или Paid).
> max_pages (int, optional): Максимальное количество страниц для Free абонемента.
> **Пример запроса:**
> ```curl -X GET "http://localhost:8000/calculate_statistics/?reader_id=1&subscription_type=Free&max_pages=200"```
> **Ответ (для Free абонемента):**
> {
>  "total_pages_read": 100,
>  "remaining_pages": 100,
>  "subscription_type": "Free"
> }

4. Генерация отчета
> **GET /generate_report/**
>
>Создает отчет о читателях в формате .docx или .xlsx.
>
>**Параметры запроса:**
>format (string): Формат отчета (docx или xlsx).
>**Пример запроса**
> ```curl -X GET "http://localhost:8000/generate_report/?format=docx" --output report.docx```
> Ответ: Отчет будет сохранен в указанном формате на вашем устройстве.

