from fastapi import FastAPI     #type: ignore

VERSION = "0.1.0"

from .routers.users import router as users_router

app = FastAPI(
    title = "Users-service-Management",
    description = "APIs for users Management",
    version = VERSION,
)

app.include_router(users_router, tags=['Users Management'])