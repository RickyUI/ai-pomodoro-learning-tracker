from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StudySessionCreate(BaseModel):
    topic: str
    duration_minutes: int
    notes: str

class StudySessionUpdate(BaseModel):
    notes: Optional[str] = None
    user_summary: Optional[str] = None
    ai_summary: Optional[str] = None

# Clase para la respuesta completa
class StudySession(StudySessionCreate):
    id: int
    ai_summary: Optional[str] = None
    user_summary: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
    
class StudyStats(BaseModel):
    total_sessions: int
    total_minutes: int
    average_duration: float