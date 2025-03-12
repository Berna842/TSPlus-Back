from pydantic import BaseModel  #type: ignore
from typing import Optional

import app.dao.puestos as puestos
from app.db.database import db

class Puestos():

    collection = db['puestos']

    @classmethod
    async def get_puesto(cls, request, arg):
        return await puestos.get_puesto(cls, request, arg)
    
    @classmethod
    async def create_puesto(cls, request, args):
        return await puestos.create_puesto(cls, request, args)
    
    @classmethod
    async def update_puesto(cls, request, guid, args):
        return await puestos.update_puesto(cls, request, guid, args)
    
    @classmethod
    async def delete_puesto(cls, request, guid):
        return await puestos.delete_puesto(cls, request, guid)
    

class Puesto(BaseModel):
    nombre:         str
    descripcion:    str
    empresa:        str
    usuarios:       list[str]
    permisos:       list[str]

class Update_Puesto(BaseModel):
    nombre:         Optional[str]       | None = ""
    descripcion:    Optional[str]       | None = None
    empresa:        Optional[str]       | None = None
    usuarios:       Optional[list[str]] | None = None
    permisos:       Optional[list[str]] | None = None