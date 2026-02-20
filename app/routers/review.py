from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from .. import models, database, main
from starlette import status
from ..services.ai_service import generate_weekly_review

router = APIRouter()

# Formateando la informacion de la tabla para la IA
def build_weekly_context(sessions):
    context = "Weekly Study Sessions:\n\n"
    
    for session in sessions:
        context += (
            f"- Date: {session.created_at}\n"
            f"  Topic: {session.topic}\n"
            f"  Duration: {session.duration_minutes} minutes\n"
            f"  Notes: {session.notes}\n\n"
        )
    
    return context


@router.get("/weekly-review")
async def get_weekly_review(db:main.db_dependency):

    seven_days_ago = datetime.now() - timedelta(days=7)

    sessions = (
        db.query(models.StudySession)
        .filter(models.StudySession.created_at >= seven_days_ago)
        .order_by(models.StudySession.created_at.desc())
        .all()
    )

    if not sessions:
        return {"message": "No study sessions in the last 7 days."}
    
    context = build_weekly_context(sessions)
    
    ai_review = generate_weekly_review(context)

    return {
        "total_sessions": len(sessions),
        "weekly_review": ai_review
    }