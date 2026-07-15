from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.database import Base
from sqlalchemy import ForeignKey


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String)
    interest = Column(String)
    response = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    history_id = Column(Integer, ForeignKey("history.id"))
    rating = Column(String)