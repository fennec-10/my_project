from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from my_project.schemas import StatusResponse # type: ignore

router=APIRouter()

users_database = dict[str, User]()


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status='ok')

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: User):
    global users_database
    if user.login in users_database:
        raise HTTPException(status.HTTP_409_CONFLICT)
    users_database[user.login]=user

@router.get("/users/{login}")
def get_user(login: str)->UserResponse:
    if login not in users_database:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
        user = users_database[login]
    return UserResponse(name=user.name, email=user.email)


#добавит несколько баз данных для добавления домашнего животного, его айди в виде числа, кличка его например
#два метода для создания и получения

#создать метод для возвращения всех животных, которые зарегестрированые, его айди и все о нем. 
