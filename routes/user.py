from fastapi import APIRouter, status, HTTPException
from models.user import User
from typing import List
from config.database import client
from bson import ObjectId
from schemas.user import serializeDict, serializeList
from auth.auth import pwd_context
user = APIRouter()

@user.get('/users/')
async def find_all_users():
    return serializeList(client.local.user.find()) 

@user.post('/users/', status_code=status.HTTP_201_CREATED)
async def create(user: User):
    # encrypt password
    user.password = pwd_context.hash(user.password)
    
    #check if email already exists
    existing = client.local.user.find_one({'email': user.email})
    if  existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    client.local.user.insert_one(dict(user))
    return serializeList(client.local.user.find())

@user.put('/users/{id}')
async def update(id: str, user: User):
    client.local.user.find_one_and_update({"_id": ObjectId(id)},{
        "$set":dict(user)  
    })
    return serializeDict(client.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/users/{id}')
async def delete(id: str, user: User):
    return serializeDict(client.local.user.find_one_and_delete({"_id": ObjectId(id)}))