from fastapi import FastAPI #type: ignore

VERSION = "0.1.0"

from .routers.authentication import router as auth_router

app = FastAPI(
    title = "Authentication-service",
    description = "APIs to authenticate all the services",
    version = VERSION,
)

app.include_router(auth_router, tags=['JWT Authentication'])