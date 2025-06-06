# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from database import Base, engine
from auth.routes import router as auth_router

# Создание таблиц в БД
Base.metadata.create_all(bind=engine)

# Инициализация приложения
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# CORS (для фронтенда)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутов
app.include_router(auth_router)
