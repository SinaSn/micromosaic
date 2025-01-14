from datetime import datetime

from sqlalchemy import Column, BigInteger, Boolean, DateTime
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    id = Column(BigInteger, primary_key=True, index=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime(timezone=True), nullable=True)

    __name__: str
