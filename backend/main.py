import os
from fastapi import FastAPI
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.api import router as api_router

def cors_origins():
    raw = settings.CORS_ORIGINS
    return [o.strip() for o in raw.split(",") if o.strip()]

app = FastAPI(title="RoadBuddy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}