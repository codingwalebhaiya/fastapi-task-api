from fastapi import FastAPI

app = FastAPI(
    title="Task Manager Api", description="API for managing tasks", version="1.0.0"
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "welcome to the task manager api"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"message": "ok"}


# - FastAPI(...) creates the application instance.
# - @app.get("/") registers a GET route.
# - def root() is a Python function that handles the request.
# - -> dict[str, str] is a return type hint.
# - Returning a dictionary allows FastAPI to serialize it into JSON.
# This is similar to defining a GET route in Express, but FastAPI uses Python functions and decorators.
