from fastapi import APIRouter, Depends, HTTPException
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from schemas.user import UserCreate, UserLogin, TokenResponse
from auth.utils import hash_password, verify_password, create_access_token
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

router = APIRouter(prefix="/auth", tags=["auth"])

# Получение сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=TokenResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.login == user_data.login.lower()).first()
    if existing_user:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Такой логин уже существует")

    user = User(
        login=user_data.login.lower(),
        hashed_password=hash_password(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=token)

@router.post("/login", response_model=TokenResponse)
def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.login == user_data.login.lower()).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Неверный логин или пароль")

    token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=token)
