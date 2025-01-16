from sqlalchemy import Column, String, UUID, ForeignKey, Boolean, SmallInteger
from sqlalchemy.orm import relationship

from app.domain.project_category import project_category
from app.domain.base import Base


class Project(Base):
    __tablename__ = 'project'
    title = Column(String, index=True)
    is_published = Column(Boolean, default=True)
    content_type = Column(SmallInteger)
    unique_identifier = Column(String)
    cover_url = Column(String, nullable=True)
    visibility = Column(SmallInteger)
    tags = Column(SmallInteger)
    user_id = Column(UUID, ForeignKey('user.id'))

    # One-to-many relationship
    user = relationship("User", back_populates="projects")

    # Many-to-many relationships
    categories = relationship('Category', secondary=project_category, back_populates='projects')
