from fastapi.routing import APIRouter
from models.user import UserLoginSchema
from config.database import client
from bson import ObjectId
from fastapi import Depends, status, HTTPException
from jose import JWTError, jwt
from auth.auth import verify_password, create_access_token, create_refresh_token
from schemas.user import serializeDict
from dotenv import dotenv_values

config = dotenv_values(".env")
authRouter = APIRouter()

error = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='wrong credentials'
)

@authRouter.post('/login')
async def login(userLogin: UserLoginSchema):
    user = client.local.user.find_one({"email": userLogin.email})
    if not user:
        raise error
    userDict = serializeDict(user)
    matches = verify_password(userLogin.password, userDict['password'])
    if not matches:
        raise error
    data = {'user_name': userDict['email']}
    accessToken = create_access_token(data)
    refreshToken = create_refresh_token(data)
    
    #update refresh token
    client.local.user.find_one_and_update({'_id': ObjectId(userDict['_id'])},{'$set': {'refresh_token' : refreshToken}})
    
    return { 
        'message' : 'Login Successful',
        'name' : userDict['name'],
        'email' : userDict['email'],
        'accessToken': accessToken,
        'refreshToken': refreshToken,
        'type': 'bearer' 
    }
        