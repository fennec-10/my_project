from fastapi import APIRouter, HTTPExpception, status
from pydantic_core.core_schema import int_schema

from my_project.schemas import StatusResponse, User, UserResponse
from my_project.schemas import Pet, PetResponse

router = APIRouter()

users_database = dict[str, User]
petsid_database: dict[int, Pet] = dict[int, Pet]()

@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: User):
    if user.login in users_database:
        raise HTTPExpception(status.HTTP_409_CONFLICT)
    users_database[user.login] = user

@router.get("/users/{login}")
def get_user(login: str)->UserResponse:
    if login not in users_database:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
        user = users_database[login]
    return UserResponse(name=user.name, email=user.email)

#добавит несколько баз данных для добавления домашнего животного, его айди в виде числа, кличка его например
#два метода для создания и получения

#создать метод для возвращения всех животных, которые зарегестрированые, его айди и все о нем. 

@router.get("/pets")
def get_pets() -> list[PetResponse]:
    return [ PetResponse(name=pet.name, nickname=pet.nickname) for pet in petid_database.values()]

@router.post("/create_petid", status_code=status.HTTP_201_CREATED)
def create_petid(pet: Pet) ->:
    if pet.id in petid_database:
        raise HTTPExpception(status.HTTP_409_CONFLICT)
    petid_database[pet.id] = pet

@router.get("/petid/{id}")
def get_petid(id: int)->PetResponse:
    if login not in petid_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        pet = petid_database[id]
    return PetResponse(name=pet.name, nicknaim=pet.nickname)
