from fastapi import FastAPI
from .database import engine
from .models import Base

app = FastAPI()

# Crea las tablas automaticamente
Base.metadata.create_all(bind=engine)