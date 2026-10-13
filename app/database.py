import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Hämtar databas-URL från miljövariabler eller använder lokal standard-URL
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:mysecretpassword@localhost:5432/tododb"
)

# Skapa SQLAlchemy-motorn
engine = create_engine(DATABASE_URL)

# Skapa en SessionLocal-klass för varje databasanrop
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Bas-klass för alla SQLAlchemy-modeller
Base = declarative_base()

# Dependency för att hämta en databassession i endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()