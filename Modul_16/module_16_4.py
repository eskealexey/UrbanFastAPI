from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_user() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def post_user(
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser",
        ),
    ],
    age: int = Path(ge=18, le=120, description="Enter age", example=24),
) -> User:
    if len(users) == 0:
        user_id = 1
    elif len(users) > 0:
        last = users[len(users) - 1]
        last_id = last.id
        user_id = last_id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user
    # return f"User {new_user.id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(
    user_id: int,
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser",
        ),
    ],
    age: int = Path(ge=18, le=120, description="Enter age", example=24),
):
    for user in users:
        if int(user.id) == int(user_id):
            edit_user = user
            edit_user.username = username
            edit_user.age = age
            return edit_user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id):
    indx = 0
    for user in users:
        if int(user.id) == int(user_id):
            users.pop(indx)
            return user
        else:
            indx += 1
    raise HTTPException(status_code=404, detail="User was not found")
