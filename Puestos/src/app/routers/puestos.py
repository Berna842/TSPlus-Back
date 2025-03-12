from fastapi import Depends, APIRouter, Response, Request   #type: ignore
from fastapi.security import HTTPBearer                     #type: ignore
from typing import Annotated

import app.models.puestos as puestos

router = APIRouter()

security = HTTPBearer()

@router.get("/puestos/", status_code=200)
async def get_puesto(request: Request, arg: str | None = ""):
    return await puestos.Puestos.get_puesto(request, arg)

@router.post("/puestos/", status_code=204)
async def create_puesto(request: Request, args: puestos.Puesto):
    return await puestos.Puestos.create_puesto(request, args)

@router.put("/puestos/", status_code=204)
async def update_puesto(request: Request, guid: str, args: puestos.Update_Puesto):
    return await puestos.Puestos.update_puesto(request, guid, args)

@router.delete("/puestos/", status_code=204)
async def delete_puesto(request: Request, guid: str):
    return await puestos.Puestos.delete_puesto(request, guid)