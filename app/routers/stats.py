from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, database, schemas, main
from starlette import status

router = APIRouter()

@router.get("/stats", response_model=schemas.StudyStats, status_code=status.HTTP_200_OK)
def get_stats(db: main.db_dependency):

    total_sessions = db.query(func.count(models.StudySession.id)).scalar()

    total_minutes = db.query(
        func.sum(models.StudySession.duration_minutes)
    ).scalar()

    average_duration = db.query(
        func.avg(models.StudySession.duration_minutes)
    ).scalar()

    return {
        "total_sessions": total_sessions or 0,
        "total_minutes": total_minutes or 0,
        "average_duration": round(average_duration or 0, 2)
    }