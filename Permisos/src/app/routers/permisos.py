from fastapi import Depends, APIRouter, Response, Request   #type: ignore
from fastapi.security import HTTPBearer                     #type: ignore
from typing import Annotated

import app.models.permisos as permisos

router = APIRouter()

security = HTTPBearer()

@router.get("/permisos/", status_code=200)
async def get_permiso(request: Request, arg: str | None = ""):
    return await permisos.Permisos.get_permiso(request, arg)

@router.post("/permisos/", status_code=204)
async def create_permiso(request: Request, args: permisos.Permiso):
    return await permisos.Permisos.create_permiso(request, args)

@router.put("/permisos/", status_code=204)
async def update_permiso(request: Request, guid: str, args: permisos.Update_Permiso | None = ""):
    return await permisos.Permisos.update_permiso(request, guid, args)

@router.delete("/permisos/", status_code=204)
async def delete_permiso(request: Request, guid: str):
    return await permisos.Permisos.delete_permiso(request, guid)