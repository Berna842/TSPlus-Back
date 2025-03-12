from fastapi import FastAPI     #type: ignore

VERSION = "0.1.0"

from .routers.puestos import router as puestos_router

app = FastAPI(
    title = "Puestos-service-Management",
    description = "APIs for Puestos Management",
    version = VERSION,
)

app.include_router(puestos_router, tags=['Puestos Management'])