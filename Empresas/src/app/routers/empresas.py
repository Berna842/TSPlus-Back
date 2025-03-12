from fastapi import Depends, APIRouter, Response, Request   #type: ignore
from fastapi.security import HTTPBearer                     #type: ignore
from typing import Annotated

import app.models.empresas as empresas

router = APIRouter()

security = HTTPBearer()

@router.get("/empresas/", status_code=200)
async def get_empresa(request: Request, arg: str | None = ""):
    return await empresas.Empresas.get_empresa(request, arg)

@router.post("/empresas/", status_code=204)
async def create_empresa(request: Request, args: empresas.Empresa):
    return await empresas.Empresas.create_empresa(request, args)

@router.put("/empresas/", status_code=204)
async def update_empresa(request: Request, guid: str, args: empresas.Update_Empresa | None = ""):
    return await empresas.Empresas.update_empresa(request, guid, args)

@router.delete("/empresas/", status_code=204)
async def delete_empresa(request: Request, guid: str):
    return await empresas.Empresas.delete_empresa(request, guid)