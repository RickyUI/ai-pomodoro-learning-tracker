from fastapi import FastAPI, Depends
from .database import engine, get_db, db_dependency
from .models import Base
from sqlalchemy.orm import Session
from .routers import sessions, stats

app = FastAPI(title="Learning Tracker")

# Crea las tablas automaticamente
Base.metadata.create_all(bind=engine)

# Registrar routers
app.include_router(sessions.router, prefix="", tags=["Study Sessions"])
app.include_router(stats.router, prefix="", tags=["Stats"])
