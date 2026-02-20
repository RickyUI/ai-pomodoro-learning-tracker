from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./study_tracker.db" # Creamos la URL de la database

# Se crea el engine para pasar como parametro a "declarative_base"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} # Necesario para SQLite
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# Dependency para usar en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()