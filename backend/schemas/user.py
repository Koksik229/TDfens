from pydantic import BaseModel, Field

# При регистрации
class UserCreate(BaseModel):
    login: str = Field(..., min_length=3, max_length=30)
    password: str = Field(..., min_length=6, max_length=100)

# При логине
class UserLogin(BaseModel):
    login: str
    password: str

# Ответ при успешной авторизации
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
