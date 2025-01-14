from datetime import timedelta

from app.application.models.response import Response
from app.core.security import hash_password, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.user import User
from app.schemas.user import UserCreate, UserLogin


class AuthCommandService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, command: UserCreate) -> Response:
        existing_user = self.user_repository.get_by_email(email=command.email)
        if existing_user:
            return Response(400, "User with this email already exists.", None)

        hashed_pwd = hash_password(str(command.password))
        new_user = User(
            name=command.name,
            email=str(command.email),
            hashed_password=hashed_pwd
        )
        self.user_repository.add(new_user)
        return Response(200, "Successful", new_user)

    def login(self, user_login: UserLogin) -> Response:
        user = self.user_repository.get_by_email(user_login.email)
        if not user or not verify_password(user_login.password, user.hashed_password):
            return Response(400, "Incorrect email or password", None)
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return Response(200, "Successful", {"access_token": access_token, "token_type": "bearer"})