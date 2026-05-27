from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
<<<<<<< HEAD
        db.close()
=======
        db.close()
>>>>>>> 2c4f512 (Final Financial Health Monitor)
