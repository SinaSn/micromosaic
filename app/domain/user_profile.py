from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.domain.base import Base


class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
