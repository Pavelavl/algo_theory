const apiUrl = "http://127.0.0.1:8000";

// Функция для получения всех событий
async function fetchEvents() {
    const response = await fetch(`${apiUrl}/events/`);
    const events = await response.json();
    const eventsBody = document.getElementById("events-body");
    eventsBody.innerHTML = ""; // Очищаем таблицу

    events.forEach(event => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${event.event_id}</td>
            <td>${event.name}</td>
            <td>${new Date(event.date).toLocaleDateString()}</td>
            <td>${event.location}</td>
            <td>${event.description}</td>
            <td>
                <button onclick="editEvent(${event.event_id})">Edit</button>
                <button onclick="deleteEvent(${event.event_id})">Delete</button>
            </td>
        `;
        eventsBody.appendChild(row);
    });
}

// Функция для добавления нового события
async function addEvent() {
    const name = document.getElementById("name").value;
    const date = document.getElementById("date").value;
    const location = document.getElementById("location").value;
    const description = document.getElementById("description").value;

    const event = { event_id: Date.now(), name, date, location, description };
    await fetch(`${apiUrl}/events/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(event)
    });
    fetchEvents(); // Обновляем таблицу
}

// Функция для удаления события
async function deleteEvent(event_id) {
    await fetch(`${apiUrl}/events/${event_id}`, { method: "DELETE" });
    fetchEvents(); // Обновляем таблицу
}

let currentEditEventId = null; // Хранение ID события, которое редактируем

// Функция для открытия модального окна редактирования
function openEditModal(event) {
    document.getElementById("edit-name").value = event.name;
    document.getElementById("edit-date").value = new Date(event.date).toISOString().split("T")[0];
    document.getElementById("edit-location").value = event.location;
    document.getElementById("edit-description").value = event.description;
    currentEditEventId = event.event_id; // Сохраняем ID текущего редактируемого события
    document.getElementById("edit-event-modal").style.display = "block";
}

// Функция для закрытия модального окна
function closeEditModal() {
    document.getElementById("edit-event-modal").style.display = "none";
    currentEditEventId = null;
}

// Функция для вызова редактирования события
async function editEvent(event_id) {
    // Получаем событие с сервера для заполнения формы
    const response = await fetch(`${apiUrl}/events/${event_id}`);
    const event = await response.json();
    openEditModal(event);
}

// Функция для сохранения изменений
async function saveEditedEvent() {
    const name = document.getElementById("edit-name").value;
    const date = document.getElementById("edit-date").value;
    const location = document.getElementById("edit-location").value;
    const description = document.getElementById("edit-description").value;

    const updatedEvent = { name, date, location, description };

    await fetch(`${apiUrl}/events/${currentEditEventId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedEvent)
    });

    closeEditModal(); // Закрываем модальное окно после сохранения
    fetchEvents(); // Обновляем таблицу
}


// Загрузка событий при загрузке страницы
window.onload = fetchEvents;
