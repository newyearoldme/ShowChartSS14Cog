from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class AdminLog(Base):
    __tablename__ = 'admin_log'
    admin_log_id = Column(Integer, primary_key=True)
    type = Column(Integer)
    message = Column(String)
    date = Column(String)
