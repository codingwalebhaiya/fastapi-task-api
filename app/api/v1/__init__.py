
#  Keep this file simple. It can remain empty, but we'll export the router here for cleaner imports.

from app.api.v1.tasks import router as tasks_router

__all__ = ["tasks_router"]