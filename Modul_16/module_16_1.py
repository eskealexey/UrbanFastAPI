from fastapi import FastAPI
# import uvicorn

app = FastAPI()


@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def adminka() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user(user_id) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user_full(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
