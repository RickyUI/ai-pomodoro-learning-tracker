from fastapi import FastAPI, Depends
from .database import engine, get_db
from .models import Base
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

db_dependency = Annotated[Session, Depends(get_db)] # Encapsular la dependencia para reutilizar

# Crea las tablas automaticamente
Base.metadata.create_all(bind=engine)