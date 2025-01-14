from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.domain.base import Base
from app.domain.project_category import project_category


class Category(Base):
    __tablename__ = 'category'
    title = Column(String, unique=True, index=True)

    # Many-to-many relationships
    projects = relationship('Project', secondary=project_category, back_populates='categories')
