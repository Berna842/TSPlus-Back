from fastapi import FastAPI     #type: ignore

VERSION = "0.1.0"

from .routers.permisos import router as permisos_router

app = FastAPI(
    title = "Permisos-service-Management",
    description = "APIs for permisos Management",
    version = VERSION,
)

app.include_router(permisos_router, tags=['Permisos Management'])