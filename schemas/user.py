def userEntity(item) -> dict:
    return {
        "id": item["_id"],
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
        "is_admin": item["is_admin"],
        "role": item["role"],
        "created_at": item["created_at"],
        "updated_at": item["updated_at"]     
    }
def usersEntity(entity) -> list: 
    return [userEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]