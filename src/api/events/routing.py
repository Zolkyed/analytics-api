import os
from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema
router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    print(os.environ.get("DATABASE_URL"))
    return EventListSchema(results=[EventSchema(id=i) for i in [1, 2, 3]], count=3)


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id)


@router.post("/")
def create_event(data: dict = {}) -> EventSchema:
    print(data)
    return EventSchema(id=12)
