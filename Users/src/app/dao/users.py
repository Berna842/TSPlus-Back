import json
import uuid                         
from fastapi import HTTPException   #type:ignore
import logging
import hashlib

async def model_validation(cls, looked):
    try:
        helper = await cls.collection.find_one({looked: {"$exists": True}})
        for key, value in helper.items():
            if looked == key:
                return key
    except:
        raise HTTPException(status_code=500, detail="The model parameter is not matched, please verify with the administrator")

async def get_user(cls, request, arg):
    #token = request.cookies.get("Bearer_Token")
    #if (token):
        documents = []
        if arg == "":
            documents = await cls.collection.find({}, {'_id': 0}).to_list()
            if documents == []:
                raise HTTPException(status_code=500, detail="Documents not found")
            return documents
        else:
            try:
                is_exist = await model_validation(cls, arg.split("=")[0])
                documents = cls.collection.find({is_exist: arg.split("=")[1]}, {'_id': 0})
                if documents ==[]:
                    raise HTTPException(status_code=500, detail="Documents not found")
                return documents
            except:
                raise HTTPException(status_code=400, detail="Advanced filter is not found, please contact with the administrator")
    #else:
    #    raise HTTPException(status_code=500, detail="Expired Token, please loggin again")

async def create_user(cls, request, args):
    try:
        guid = str(uuid.uuid4())
        args = dict(args)
        args['guid'] = guid
        args['contrasena'] = hashlib.sha256(args['contrasena'].encode('ASCII')).hexdigest()
        result = await cls.collection.insert_one(args)
    except:
        raise HTTPException(status_code=500, detail="Service is unable to insert, please contact with the administrator")

async def update_user(cls, request, guid, args):
    #token = request.cookies.get("Bearer_Token")
    #if(token):
        try:
            document = await cls.collection.find_one({"guid": guid}, {'_id': 0})
        except:
            raise HTTPException(status_code=400, detail="The GUID to update is not found it, please review and try again")
        for key,value in args:
            if value != None:
                document[key] = value
        try:
            result = await cls.collection.replace_one({"guid": guid}, dict(document))
        except:
            raise HTTPException(status_code=500, detail="Service is unable to update, plase contact with the administrator")
    #else:
    #    raise HTTPException(status_code=500, detail="Expired Token, please loggin again")

async def delete_user(cls, request, guid):
    #token = request.cookies.get("Bearer_Token")
    #if(token):
        try:
            document = await cls.collection.find_one({"guid": guid}, {'_id': 0})
        except:
            raise HTTPException(status_code=400, detail="The GUID to delete is not found it, please review and try again")
        try:
            result = await cls.collection.delete_one({"guid": guid})
        except:
            raise HTTPException(status_code=500, detail="Service is unable to delete, please contact with the administrator")
    #else:
    #    raise HTTPException(status_code=500, detail="Expired Token, please loggin again")