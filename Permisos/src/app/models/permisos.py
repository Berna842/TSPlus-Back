from pydantic import BaseModel  #type: ignore
from typing import Optional

import app.dao.permisos as permisos
from app.db.database import db

class Permisos():

    collection = db['permisos']

    @classmethod
    async def get_permiso(cls, request, arg):
        return await permisos.get_permiso(cls, request, arg)
    
    @classmethod
    async def create_permiso(cls, request, args):
        return await permisos.create_permiso(cls, request, args)
    
    @classmethod
    async def update_permiso(cls, request, guid, args):
        return await permisos.update_permiso(cls, request, guid, args)
    
    @classmethod
    async def delete_permiso(cls, request, guid):
        return await permisos.delete_permiso(cls, request, guid)
    

class Permiso(BaseModel):
    nombre:         str
    descripcion:    str
    endpoint:       str
    shortname:      str
    method:         str
    service:        str

class Update_Permiso(BaseModel):
    nombre:         Optional[str] | None = ""
    descripcion:    Optional[str] | None = None
    endpoint:       Optional[str] | None = None
    shortname:      Optional[str] | None = None
    method:         Optional[str] | None = None
    service:        Optional[str] | None = None
    