from sqlalchemy import Table, BigInteger, Column, ForeignKey

from app.domain.base import Base

project_category = Table(
    "project_category",
    Base.metadata,
    Column("project_id", BigInteger, ForeignKey("project.id"), primary_key=True),
    Column("category_id", BigInteger, ForeignKey("category.id"), primary_key=True),
)