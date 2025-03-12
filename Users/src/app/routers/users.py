from fastapi import Depends, APIRouter, Response, Request   #type: ignore
from fastapi.security import HTTPBearer                     #type: ignore
from typing import Annotated

import app.models.users as users                            #type: ignore

router = APIRouter()

security = HTTPBearer()

@router.get("/users/", status_code=200)
async def get_user(request: Request, arg: str | None = ""):
    return await users.Users.get_user(request, arg)

@router.post("/users/", status_code=204)
async def create_user(request: Request, args: users.User):
    return await users.Users.create_user(request, args)

@router.put("/users/", status_code=204)
async def update_user(request: Request, guid: str, args: users.User_Update):
    return await users.Users.update_user(request, guid, args)

@router.delete("/users/", status_code=204)
async def delete_user(request: Request, guid: str):
    return await users.Users.delete_user(request, guid)

#docker run -d -p 27017:27017 mongodb/mongodb-community-server:latest
#docker build -t [authentication] -f docker/Dockerfile .
#docker run -d -p 8001:8000 docker.io/library/[authentication]:latest
#docker builder prune