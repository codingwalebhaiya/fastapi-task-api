from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.base import Base 
from app.db.session import engine
from  app.models.task import Task

# lifespan manages the lifecycle of the application
# context manager is used to manage the state of the application
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application is starting")
    Base.metadata.create_all(bind=engine)
    yield
    print("Application is shutting down")


app = FastAPI(
    title="Task Manager Api", description="API for managing tasks", version="1.0.0", lifespan=lifespan
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "welcome to the task manager api"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


# - FastAPI(...) creates the application instance.
# - @app.get("/") registers a GET route.
# - def root() is a Python function that handles the request.
# - -> dict[str, str] is a return type hint.
# - Returning a dictionary allows FastAPI to serialize it into JSON.
# This is similar to defining a GET route in Express, but FastAPI uses Python functions and decorators.


# NOTE - Here, Task is imported so SQLAlchemy knows about the model before create_all() runs.
# The lifespan handler initializes the database tables when the application starts.
