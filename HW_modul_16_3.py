from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username:Annotated[str, Path(min_length=6, max_length=15, description="Enter your name:", example="Viktor")],
                      age:Annotated[int, Path(ge=18, le=120, description="Enter your age:", example='24')])->str:
    user_id = str(int(max(users, key=int)) +1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id:Annotated[int, Path(ge=1, le=500, description="Enter userID what you want to edit")], 
                      username:Annotated[str, Path(min_length=6, max_length=15, description="Enter your name:", example="Viktor")],
                      age:Annotated[int, Path(ge=18, le=120, description="Enter your age:", example='24')])->str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The User {user_id} is updated"

@app.delete('/user/{user_id}')
async def user_delete(user_id:Annotated[int, Path(ge=1, le=500, description="Enter userID what you want to edit")])->str:
    users.pop(str(user_id))
    return f"The User {user_id} is deleted"