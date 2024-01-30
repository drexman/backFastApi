from fastapi import APIRouter
from models.user import User
from typing import List

user = APIRouter()

usersDb: List[User] = [] 

@user.get('/find_all_users/')
async def find_all_users():
    return usersDb; 

@user.post('/users/')
async def create_user(user: User):
    usersDb.append(user)
    return {'message': 'new user created successfully' }
