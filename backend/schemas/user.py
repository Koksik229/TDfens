from pydantic import BaseModel

# При регистрации
class UserCreate(BaseModel):
    login: str
    password: str

# При логине
class UserLogin(BaseModel):
    login: str
    password: str

# Ответ при успешной авторизации
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
