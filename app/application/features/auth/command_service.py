from datetime import timedelta

from app.application.models.response import Response
from app.core.security import hash_password, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.domain import UserProfile, User
from app.infrastructure.repositories import UserRepository, UserProfileRepository
from app.schemas.user import UserCreate, UserLogin


class AuthCommandService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_profile_repository = UserProfileRepository()


    def register(self, command: UserCreate) -> Response:
        existing_user = self.user_repository.get_by_email(email=command.email)
        if existing_user:
            return Response(400, "User with this email already exists.", None)

        hashed_password = hash_password(str(command.password))
        new_user = User(
            username=command.username,
            email=command.email,
            hashed_password=hashed_password
        )
        self.user_repository.add(new_user)

        new_user_profile = UserProfile(
            user_id=new_user.id,
        )
        self.user_profile_repository.add(new_user_profile)

        access_token = create_access_token(
            data={"sub": new_user.email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return Response(200, "Successful", {"access_token": access_token, "token_type": "bearer"})

    def login(self, user_login: UserLogin) -> Response:
        user = self.user_repository.get_by_email(user_login.email)
        if not user or not verify_password(user_login.password, user.hashed_password):
            return Response(400, "Incorrect email or password", None)
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        print(access_token)
        return Response(200, "Successful", {"access_token": access_token, "token_type": "bearer"})