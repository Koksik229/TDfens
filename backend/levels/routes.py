from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from models.level import Level, UserLevelProgress
from models.user import User
from schemas.level import LevelBase
from auth.utils import decode_access_token
from typing import List

router = APIRouter(prefix="/levels", tags=["levels"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Header(...), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Неверный токен")
    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не найден")
    return user

@router.get("/", response_model=List[LevelBase])
def get_levels(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    levels = db.query(Level).all()
    progress = db.query(UserLevelProgress).filter(UserLevelProgress.user_id == current_user.id).all()
    progress_map = {p.level_id: p.stars for p in progress}

    result = []
    for lvl in levels:
        lvl_data = LevelBase.from_orm(lvl)
        lvl_data.stars = progress_map.get(lvl.id, 0)
        result.append(lvl_data)

    return result
