from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..services.ai_service import generate_summary
from ..database import db_dependency
from typing import List

router = APIRouter()


# Endpoint que devuelve todos los records de la DB
@router.get("/sessions", response_model=List[schemas.StudySession], status_code=status.HTTP_200_OK)
async def read_all_sessions(db: db_dependency):
    return db.query(models.StudySession).all()

    
# Endpoint que recibe POST del usuario y almacena en la DB, ademas devuelve los valores agregados
@router.post("/sessions", response_model=schemas.StudySession, status_code=status.HTTP_201_CREATED)
async def create_study_session(session: schemas.StudySessionCreate, db: db_dependency):
    # Crear objeto de base de datos
    db_session = models.StudySession(**session.model_dump())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    # Llamar a la IA para generar resumen
    ai_summary = generate_summary(db_session.notes)
    db_session.ai_summary = ai_summary
    db.commit()
    db.refresh(db_session)

    # Devolver la sesión completa
    return db_session


