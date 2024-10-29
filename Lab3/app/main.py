from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.controllers import event_controller
from app.models.event import Event, EventCreate, EventUpdate
from sqlalchemy.orm import Session
from database.setup import get_db, init_db
from typing import List

app = FastAPI()

# Инициализация базы данных
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("app/static/index.html")

@app.post("/events/", response_model=Event)
async def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return event_controller.create_event(event, db)

@app.get("/events/", response_model=List[Event])
async def get_all_events(db: Session = Depends(get_db)):
    return event_controller.get_all_events(db)

@app.get("/events/{event_id}", response_model=Event)
async def read_event(event_id: int, db: Session = Depends(get_db)):
    return event_controller.get_event(event_id, db)

@app.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    return event_controller.update_event(event_id, event, db)

@app.delete("/events/{event_id}")
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    event_controller.delete_event(event_id, db)
    return {"detail": "Event deleted"}
