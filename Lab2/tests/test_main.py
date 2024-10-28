import pytest
import pytest_asyncio
from httpx import AsyncClient
from main import app

@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://localhost:8081") as client:
        yield client

@pytest.mark.asyncio
async def test_add_reader(async_client):
    response = await async_client.post("/add_reader/", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json() == {"message": "Reader John Doe added", "id": 1}

@pytest.mark.asyncio
async def test_add_book(async_client):
    # Сначала добавляем читателя, чтобы получить reader_id = 1
    await async_client.post("/add_reader/", json={"name": "John Doe"})

    # Добавляем книгу, привязывая ее к reader_id = 1
    response = await async_client.post(
        "/add_book/",
        json={"title": "Test Book", "author": "Test Author", "pages": 300, "reader_id": 1}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Book Test Book by Test Author added"}


@pytest.mark.asyncio
async def test_calculate_statistics_free_subscription(async_client):
    # Сначала добавляем читателя и сохраняем его ID
    response = await async_client.post("/add_reader/", json={"name": "Jane Doe"})
    assert response.status_code == 200
    reader_id = response.json().get("id")
    
    # Добавляем книгу, привязывая ее к полученному reader_id
    response = await async_client.post(
        "/add_book/",
        json={"title": "Test Book", "author": "Test Author", "pages": 100, "reader_id": reader_id}
    )
    assert response.status_code == 200

    # Отправляем запрос на расчет статистики с телом JSON
    response = await async_client.post(
        "/calculate_statistics/",
        json={"reader_id": reader_id, "subscription_type": "Free", "max_pages": 200},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total_pages_read"] == 100
    assert data["remaining_pages"] == 100
    assert data["subscription_type"] == "Free"

@pytest.mark.asyncio
async def test_calculate_statistics_paid_subscription(async_client):
    # Сначала добавляем читателя и книгу
    response = await async_client.post("/add_reader/", json={"name": "Jane Smith"})
    assert response.status_code == 200
    reader_id = response.json().get("id")
    response = await async_client.post("/add_book/", json={"title": "Advanced Book", "author": "Advanced Author", "pages": 250, "reader_id": reader_id})
    assert response.status_code == 200

    # Отправляем запрос на расчет статистики с телом JSON
    response = await async_client.post(
        "/calculate_statistics/",
        json={"reader_id": reader_id, "subscription_type": "Paid"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total_pages_read"] == 250
    assert data["subscription_type"] == "Paid"

@pytest.mark.asyncio
async def test_generate_report_docx(async_client):
    response = await async_client.get("/generate_report/", params={"format": "docx"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    assert response.headers["content-disposition"] == 'attachment; filename="report.docx"'

@pytest.mark.asyncio
async def test_generate_report_xlsx(async_client):
    response = await async_client.get("/generate_report/", params={"format": "xlsx"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert response.headers["content-disposition"] == 'attachment; filename="report.xlsx"'
