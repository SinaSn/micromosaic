from sqlalchemy import Column, Integer, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from app.domain.base import Base


class UserProfile(Base):
    __tablename__ = 'user_profile'
    cover_image = Column(String, nullable=True)
    profile_image = Column(String, nullable=True)
    gender = Column(Integer, nullable=True)
    user_id = Column(UUID, ForeignKey('user.id'))
