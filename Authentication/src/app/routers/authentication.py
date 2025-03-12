from fastapi import Depends, APIRouter, Response, Request #type: ignore
from fastapi.security import HTTPBearer #type: ignore
from typing import Annotated

import app.models.authentication as auth

router = APIRouter()

security = HTTPBearer()

@router.get("/authenticate/", status_code=200)
async def get_token_information(request: Request):
    return await auth.Authentication.get_token_information(request)

@router.post("/authenticate/", status_code=200)
async def create_token(response: Response, form_data:Annotated[auth.Credentials, Depends]):
    return await auth.Authentication.create_token(response, form_data)

@router.put("/authenticate/", status_code=204)
async def update_token(request: Request, response: Response):
    return await auth.Authentication.update_token(request, response)

@router.delete("/authenticate/", status_code=204)
async def delete_token(response: Response):
    return await auth.Authentication.delete_token(response)