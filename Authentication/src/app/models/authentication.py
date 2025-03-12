from pydantic import BaseModel  #type: ignore
import os

import app.dao.authentication as auth
from app.db.database import db

class Authentication():

    collection = db['users']

    secret = os.getenv("JWT_SECRET", "secret")
    algorithm = os.getenv("JWT_ALGORITHM", "HS256")
    expiration = os.getenv("JWT_EXPIRATION", 3600)
    expiration_refresh = os.getenv("JWT_EXPIRATION_REFRESH", 7200)

    @classmethod
    async def get_token_information(cls, request):
        return await auth.get_token_information(cls, request)
    
    @classmethod
    async def create_token(cls, response, args):
        return await auth.create_token(cls, response, args)
    
    @classmethod
    async def update_token(cls, request, response):
        return await auth.update_token(cls, request, response)
    
    @classmethod
    async def delete_token(cls, response):
        return await auth.delete_token(cls, response)
    
class Credentials(BaseModel):
    correo: str
    contrasena: str