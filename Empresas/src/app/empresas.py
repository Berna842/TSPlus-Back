from fastapi import FastAPI     #type: ignore

VERSION = "0.1.0"

from .routers.empresas import router as empresas_router

app = FastAPI(
    title = "Empresas-service-Management",
    description = "APIs for empresas Management",
    version = VERSION,
)

app.include_router(empresas_router, tags=['Empresas Management'])