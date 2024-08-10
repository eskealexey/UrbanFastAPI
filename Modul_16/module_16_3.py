from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Exemple, возраст: 18"}


# возвращает словарь users.
@app.get("/users")
async def get_user():
    return users


# добавляет в словарь по максимальному значению ключа значение строки "Имя: {username}, возраст: {age}".
# И возвращает строку "User <user_id> is registered".
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
):
    new_id = int(max(users, key=users.get)) + 1
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


# обновляет значение из словаря users под ключом user_id
# на строку "Имя: {username}, возраст: {age}".
# И возвращает строку "The user <user_id> is registered"
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
    if str(user_id) in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is registered"
    else:
        return False


# удаляет из словаря users по ключу user_id пару.
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if str(user_id) in users:
        del users[user_id]
        return f"Удаление по ключу {user_id} прошло успешно"
    else:
        return f"Not delete"
