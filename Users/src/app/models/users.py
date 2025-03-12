from pydantic import BaseModel  #type: ignore
from typing import Optional

import app.dao.users as users
from app.db.database import db

class Users():

    collection = db['users']

    @classmethod
    async def get_user(cls, request, arg):
        return await users.get_user(cls, request, arg)
    
    @classmethod
    async def create_user(cls, request, args):
        return await users.create_user(cls, request, args)
    
    @classmethod
    async def update_user(cls, request, guid, args):
        return await users.update_user(cls, request, guid, args)
    
    @classmethod
    async def delete_user(cls, request, guid):
        return await users.delete_user(cls, request, guid)
    
class User(BaseModel):
    nombre:             str
    apellido_paterno:   str
    apellido_materno:   str
    correo:             str
    contrasena:         str
    telefono:           Optional[int] | None = None
    foto:               Optional[str] | None = None

class User_Update(BaseModel):
    nombre:             Optional[str] | None = None
    apellido_paterno:   Optional[str] | None = None
    apellido_materno:   Optional[str] | None = None
    correo:             Optional[str] | None = None
    contrasena:         Optional[str] | None = None
    telefono:           Optional[int] | None = None
    foto:               Optional[str] | None = None
