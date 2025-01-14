from fastapi import APIRouter, HTTPException

from app.schemas.user import Token, UserLogin, UserCreate
from app.application.features.auth.command_service import AuthCommandService

router = APIRouter()

auth_command_service = AuthCommandService()

@router.post("/login", response_model=Token)
def login(user_login: UserLogin):
    result = auth_command_service.login(user_login)
    if result.status_code == 200:
        return result.data
    raise HTTPException(status_code=result.status_code, detail=result.message)

@router.post("/register", response_model=Token)
def register(new_user: UserCreate):
    result = auth_command_service.register(new_user)
    if result.status_code == 200:
        return result.data
    raise HTTPException(status_code=result.status_code, detail=result.message)