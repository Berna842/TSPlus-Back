from pydantic import BaseModel  #type: ignore
from typing import Optional

import app.dao.empresas as empresas
from app.db.database import db

class Empresas():

    collection = db['empresas']

    @classmethod
    async def get_empresa(cls, request, arg):
        return await empresas.get_empresa(cls, request, arg)
    
    @classmethod
    async def create_empresa(cls, request, args):
        return await empresas.create_empresa(cls, request, args)
    
    @classmethod
    async def update_empresa(cls, request, guid, args):
        return await empresas.update_empresa(cls, request, guid, args)
    
    @classmethod
    async def delete_empresa(cls, request, guid):
        return await empresas.delete_empresa(cls, request, guid)
    

class Empresa(BaseModel):
    nombre:         str
    descripcion:    str
    logo:           str
    proveedor:      str
    servidores:     list[str]
    token:          str

class Update_Empresa(BaseModel):
    nombre:         Optional[str] | None = ""
    descripcion:    Optional[str] | None = None
    logo:           Optional[str] | None = None
    proveedor:      Optional[str] | None = None
    servidores:     Optional[list[str]] | None = None
    token:        Optional[str] | None = None
    