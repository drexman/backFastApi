from jose import jwt,JWTError 
from datetime import datetime
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, status, HTTPException

from dotenv import dotenv_values

error = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='wrong credentials'
)
auth_scheme = HTTPBearer()

config = dotenv_values(".env")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password) 

def create_access_token(data: dict):
    data['expires'] = datetime.utcnow().strftime('%B %d %Y - %H:%M:%S') + config['JWT_ACCESS_TOKEN_EXP_DAYS']
    data['mode'] = 'refresh_token'
    return jwt.encode(data, config['JWT_SECRET_KEY'], config['JWT_ALGORITHM'])

def create_refresh_token(data: dict):
    data['expires'] = datetime.utcnow().strftime('%B %d %Y - %H:%M:%S') + config['JWT_REFRESH_TOKEN_EXP_DAYS']
    data['mode'] = 'refresh_token'
    return jwt.encode(data, config['JWT_SECRET_KEY'], config['JWT_ALGORITHM'])	

async def authorize(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> dict:
    token = token.credentials
    try:
        data = jwt.decode(token,config['JWT_SECRET_KEY'],config['JWT_ALGORITHM'])
        print(data)
        return {
                
        }
    except JWTError:
        raise error

async def verified_user(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> dict:
    token = token.credentials
    try:
        data = jwt.decode(token,config['JWT_SECRET_KEY'],config['JWT_ALGORITHM'])
        print(data)
        return {
                
        }
    except JWTError:
        raise error