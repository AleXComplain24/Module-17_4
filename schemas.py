from pydantic import BaseModel

# Схемы пользователя
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

# Схемы задач
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(CreateTask):
    pass

class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int

    class Config:
        orm_mode = True