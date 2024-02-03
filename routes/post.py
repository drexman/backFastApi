from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from config.database import client
from  auth.auth import verified_user
from fastapi.security import HTTPBearer

post = APIRouter()
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/token")

@post.get('/post/')
async def getPost(value: dict= Depends(verified_user)):
    print(value)
    return {'message': 'sucesso'} 
