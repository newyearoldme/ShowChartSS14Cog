from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class AdminLog(Base):
    __tablename__ = "admin_log"
    
    admin_log_id: Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True)
    type: Mapped[int] = mapped_column(Integer)
    message: Mapped[str] = mapped_column(String)
    date: Mapped[str] = mapped_column(String)
