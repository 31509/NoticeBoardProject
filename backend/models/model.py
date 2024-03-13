from sqlalchemy import Column, Integer, String, Date, ForeignKey, update, select
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class BOARD(Base):
    __tablename__ = 'board_tbl'
    board_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(100))
    writer = Column(String(50))
    content = Column(String(1000))

class USER(Base):
    __tablename__ = 'user_tbl'
    user_id = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)