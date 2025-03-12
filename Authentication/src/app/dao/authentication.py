import jwt #type: ignore
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException #type: ignore
import json
import hashlib
import logging

async def get_token_information(cls, request, token="Bearer_Token"):
    try:
        token = request.cookies.get(token)
        information = jwt.decode(token, cls.secret.encode('ASCII'), algorithms=[cls.algorithm])
        return information
    except:
        raise HTTPException(status_code=500, detail="Token expired")

async def create_token(cls, response, args):
    payload = {}
    try:
        args = dict(args)
        user = await cls.collection.find_one({"correo": args['correo']}, {'_id':0})
    except:
        raise HTTPException(status_code=400, detail="User not found, please review and try again")
    try:
        if(hashlib.sha256(args['contrasena'].encode('ASCII')).hexdigest() == user['contrasena']):
            for key,value in user.items():
                payload[key] = value
            payload['exp'] = datetime.now(tz=timezone.utc) + timedelta(seconds=cls.expiration)
            encoded_jwt = jwt.encode(payload, cls.secret, algorithm=cls.algorithm)
            refresh_jwt = jwt.encode({
                                        "Bearer_Token": encoded_jwt,
                                        "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=cls.expiration_refresh)
                                    },
                                    cls.secret, algorithm = cls.algorithm)
            response.set_cookie(
                key = "Bearer_Token",
                value = encoded_jwt,
                httponly = True,
                secure = False, #TODO when in production change to True with HTTPS only
                samesite = "Lax"
            )
            response.set_cookie(
                key = "Refresh_Token",
                value = refresh_jwt,
                httponly = True,
                secure = False,
                samesite = "Lax"
            )
            return {"Bearer_Token": encoded_jwt, "Refresh_Token": refresh_jwt}
        else:
            raise HTTPException(status_code=500, detail="Wrong Password or Email")
    except:
        raise HTTPException(status_code=500, detail="Service unable to authenticate, if you forgot your password please contact the administrator")

async def update_token(cls, request, response):
    try:
        information = await get_token_information(cls, request, "Refresh_Token")
        payload = jwt.decode(information['Bearer_Token'], cls.secret, algorithms=[cls.algorithm])
        payload['exp'] = datetime.now(tz = timezone.utc) + timedelta(seconds=cls.expiration) 
        encoded_jwt = jwt.encode(payload, cls.secret, algorithm = cls.algorithm)
        refresh_jwt = jwt.encode({
                                    "Bearer_Token": encoded_jwt,
                                    "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=cls.expiration_refresh)
                                    },
                                    cls.secret, algorithm = cls.algorithm)
        response.set_cookie(
            key = "Bearer_Token",
            value = encoded_jwt,
            httponly = True,
            secure = False, #TODO when in production change to True with HTTPS only
            samesite = "Lax"
        )
        response.set_cookie(
            key = "Refresh_Token",
            value = refresh_jwt,
            httponly = True,
            secure = False,
            samesite = "Lax"
        )
    except:
        raise HTTPException(status_code = 400, detail="Invalid Refresh Token")
    

async def delete_token(cls, response):
    try:
        response.set_cookie(
            key="Bearer_Token",
            value="",
            httponly=True,
            secure=False,
            samesite="Lax",
            expires=0
        )
        response.set_cookie(
            key="Refresh_Token",
            value="",
            httponly=True,
            secure=False,
            samesite="Lax",
            expires=0
        )
    except:
        raise HTTPException(status_code = 666, detail="Something really bad is about to happend :(")