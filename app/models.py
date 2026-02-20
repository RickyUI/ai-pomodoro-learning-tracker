from .database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime

# Creando la tabla de "studysessions" dentro de la DB
class studySession(Base):
    __tablename__ = "studysessions"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    notes = Column(Text, nullable=False)
    ai_summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)