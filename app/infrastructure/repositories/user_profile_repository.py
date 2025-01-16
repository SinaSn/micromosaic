from typing import Optional

from app.domain import UserProfile
from app.infrastructure.repositories.base_repository import BaseRepository

class UserProfileRepository(BaseRepository[UserProfile, int]):
    def __init__(self):
        super().__init__()