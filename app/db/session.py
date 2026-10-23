from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


# engine manages database connectivity and connection pooling.
engine = create_engine(settings.database_url, pool_pre_ping=True)

# SessionLocal creates a database session for each unit of work.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


# NOTE - A SQLAlchemy session is not the same as a database connection. It manages ORM state and transactions 
# while obtaining connections from the engine's pool as needed.
