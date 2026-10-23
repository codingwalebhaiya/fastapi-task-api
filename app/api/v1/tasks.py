from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy import select
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

#  A router is a way to organize related routes.
router = APIRouter(prefix="/tasks", tags=["tasks"])


#  The get_db function is a dependency that provides a database session for each request.
#  It uses a generator to create and close the session automatically.
#  DependencyInjection is a design pattern that allows you to inject dependencies into a function or class.
def get_db():
    """Provide one database session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#  Annotated[] is used to create a type hint that includes a dependency.
#  Depends() is used to specify that the get_db function should be called to provide the dependency.
#  AsyncSession is the type hint for the database session.
DbSession = Annotated[Session, Depends(get_db)]


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate, db: DbSession):
    task = Task(
        title=task_data.title, description=task_data.description, completed=False
    )

    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: DbSession):
    task = await db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@router.get("/list", response_model=list[TaskResponse])
async def get_tasks(db: DbSession):
    statement = select(Task).order_by(Task.id.desc())
    result = db.scalars(statement).all()
    return result


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: DbSession) -> Response:
    task = await db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    await db.delete(task)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: DbSession,
):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed

    await db.commit()
    await db.refresh(task)
    return task
