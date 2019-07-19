from sqlalchemy import (
    Column, String, Integer,
    DateTime, Date, Boolean
)

from . import Base


class LogFile(Base):
    __tablename__ = 'logs'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    date = Column(Date)

    def __repr__(self):
        return 