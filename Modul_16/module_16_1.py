from fastapi import FastAPI
# import uvicorn


app = FastAPI()


@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def adminka() -> str:
    return "Вы вошли как администратор"

@app.get("/user")
async def user_full(username: str = "Alex", age: int = 50) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/user/{user_id}")
async def user(user_id) -> str:
    return f"Вы вошли как пользователь № {user_id}"

