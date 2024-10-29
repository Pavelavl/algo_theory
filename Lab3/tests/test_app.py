import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.setup import Base, get_db

# Настройка тестовой базы данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_events.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Используем тестовую базу данных для тестов
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Создание тестового клиента
client = TestClient(app)

# Фикстура для настройки базы данных перед тестами
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Создаем таблицы
    yield
    Base.metadata.drop_all(bind=engine)  # Удаляем таблицы после тестов

# 1. Тест создания события
def test_create_event():
    response = client.post("/events/", json={
        "name": "Test Event",
        "date": "2024-12-01T00:00:00",
        "location": "Test Location",
        "description": "This is a test event"
    })
    assert response.status_code == 200
    data = response.json()
    assert "event_id" in data  # Проверяем, что ключ 'event_id' присутствует
    assert data["name"] == "Test Event"
    assert data["location"] == "Test Location"
    assert data["description"] == "This is a test event"

# 2. Тест получения события
def test_get_event():
    # Создаем событие для тестирования
    response = client.post("/events/", json={
        "name": "Get Event",
        "date": "2024-12-01T00:00:00",
        "location": "Location",
        "description": "Event to retrieve"
    })
    assert response.status_code == 200
    data = response.json()
    assert "event_id" in data  # Проверяем, что ключ 'event_id' присутствует
    event_id = data["event_id"]

    # Получаем событие
    response = client.get(f"/events/{event_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Get Event"
    assert data["description"] == "Event to retrieve"

# 3. Тест обновления события
def test_update_event():
    # Создаем событие для тестирования
    response = client.post("/events/", json={
        "name": "Update Event",
        "date": "2024-12-01T00:00:00",
        "location": "Location",
        "description": "Event to update"
    })
    event_id = response.json()["event_id"]

    # Обновляем событие
    response = client.put(f"/events/{event_id}", json={
        "name": "Updated Event",
        "date": "2024-12-02T00:00:00",
        "location": "New Location",
        "description": "Updated description"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Event"
    assert data["location"] == "New Location"
    assert data["description"] == "Updated description"

# 4. Тест удаления события
def test_delete_event():
    # Создаем событие для тестирования
    response = client.post("/events/", json={
        "name": "Delete Event",
        "date": "2024-12-01T00:00:00",
        "location": "Location",
        "description": "Event to delete"
    })
    event_id = response.json()["event_id"]

    # Удаляем событие
    response = client.delete(f"/events/{event_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Event deleted"}

    # Проверяем, что событие больше не существует
    response = client.get(f"/events/{event_id}")
    assert response.status_code == 404
