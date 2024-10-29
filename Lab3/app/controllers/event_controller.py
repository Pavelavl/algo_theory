from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.models.event import Event, EventCreate, EventUpdate
from database.setup import EventDB, SessionLocal
from datetime import datetime

# Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_all_events(db: Session):
    return db.query(EventDB).all()

def create_event(event: EventCreate, db: Session) -> Event:
    db_event = EventDB(
        name=event.name,
        date=event.date,
        location=event.location,
        description=event.description
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_event(event_id: int, db: Session) -> Event:
    event = db.query(EventDB).filter(EventDB.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

def update_event(event_id: int, updated_event: EventUpdate, db: Session) -> Event:
    event = db.query(EventDB).filter(EventDB.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event.name = updated_event.name
    event.date = updated_event.date
    event.location = updated_event.location
    event.description = updated_event.description
    db.commit()
    db.refresh(event)
    return event

def delete_event(event_id: int, db: Session) -> None:
    event = db.query(EventDB).filter(EventDB.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
