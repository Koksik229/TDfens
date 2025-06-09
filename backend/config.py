from datetime import timedelta

class Settings:
    PROJECT_NAME: str = "TowerDefence"
    VERSION: str = "1.0.0"

    # SQLite путь (можно заменить на PostgreSQL позже)
    DATABASE_URL: str = "sqlite:///./db.sqlite3"

    # JWT настройки
    SECRET_KEY: str = "super-secret-key"  # !! замени перед продом
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 неделя

    # CORS настройки (если фронт на другом домене)
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",  # Vite dev
    ]

settings = Settings()
