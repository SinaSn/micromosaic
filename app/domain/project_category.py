from sqlalchemy import Table, UUID, Column, ForeignKey

from app.domain.base import Base

project_category = Table(
    "project_category",
    Base.metadata,
    Column("project_id", UUID, ForeignKey("project.id"), primary_key=True),
    Column("category_id", UUID, ForeignKey("category.id"), primary_key=True),
)