from fastapi import FastAPI



app = FastAPI()



@app.get('/')
async def message() -> dict:
  return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin() -> dict:
  return {'admin': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user_id(user_id) -> dict:
  return {'user': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/{username}/{age}')
async def user(username: str, age: int) -> dict:
  return {'user': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}