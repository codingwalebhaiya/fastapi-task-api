from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func, String  
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


# Define the Task database model
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    


# NOTE - Mapped[str | None] means the Python attribute may contain a string or None.
#  The nullable=True setting allows SQL NULL in the corresponding database column.