# schemas/level.py

from pydantic import BaseModel
from typing import Optional

class LevelBase(BaseModel):
    id: int
    name: str
    max_stars: int
    difficulty_required: int
    stars: int = 0  # сколько набрано пользователем

    class Config:
        orm_mode = True
