from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.domain.base import Base


class User(Base):
    __tablename__ = 'user'
    email = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    display_name = Column(String)
    hashed_password = Column(String)

    # Many-to-one relationship
    projects = relationship("Project", back_populates="user")