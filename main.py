from fastapi import FastAPI
from routes.events import router as events_router
from routes.auth import router as auth_router
from routes.registrations import router as registration_router
from services.hubspot_service import upsert_contact

app = FastAPI()

app.include_router(events_router)
app.include_router(auth_router)
app.include_router(registration_router)