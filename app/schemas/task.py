from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from pydantic.error_wrappers import ValidationError



# Pydantic schemas (used for validation and serialization)
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=500)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=500)
    completed: bool | None = Field(default=None)


# Define the fields returned to the client
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)



# NOTE - ConfigDict is used to configure Pydantic models.
# from_attributes=True allows the model to be initialized from a SQLAlchemy model instance.