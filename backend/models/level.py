# models/level.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_stars = Column(Integer, default=3)
    difficulty_required = Column(Integer, default=1)  # позже может быть enum


class UserLevelProgress(Base):
    __tablename__ = "user_level_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False)
    stars = Column(Integer, default=0)
    last_played = Column(DateTime, default=datetime.utcnow)
