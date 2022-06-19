from typing import List
from fastapi import APIRouter, Response, status
from sqlalchemy import table
from schemas.dog import responseDog
from models.user import modelUser
from config.querys import get_all, get_one_user, create_object, delete_user, update_user, dogs_by_user

from schemas.user import User, responseUser

Route=APIRouter()
table = modelUser.__table__

@Route.get(
    '/',
    response_model=List[responseUser],
    summary="Get all users",
    description="Get information about all users in database",
    tags = ["users"]
    )
async def get_users():
    """
    Path operation for get all users in database
    this path operation dont reiceve any parameters
    Returns:
        List[modelUser]: List of users
    """
    response = await get_all(table)
    return response



@Route.get(
    '/{id}',
    response_model=responseUser,
    summary="Get user by id",
    description="Get information about user by name",
    tags = ["users"]
    )
async def get_user(id: int):
    """Path operation for get user by id
    Args:
        id: id of user
    Returns:
        modelUser: user
    """
    response = await get_one_user(table, id)
    return response


@Route.get(
    '/dogs/{id}',
    response_model=List[responseDog],
    summary="Get dogs by user id",
    description="Get information about dogs by user id",
    tags = ["dogs"]
)
async def get_dogs_by_user(id: int):
    """Path operation for get dogs by user id
    Args:
        id: id of user
    Returns:
        List[modelDog]: List of dogs
    """
    response = await dogs_by_user(id)
    return response





@Route.post(
    '/',
    status_code = status.HTTP_201_CREATED,
    summary="Create user",
    description="Create a new user",
    tags = ["users"]
    )
async def create_user(user: User):
    """Path operation for create user
    Args:
        user: user to create
    Returns:
        modelUser: user created
    """
    await create_object(table, user.dict())
    return Response(status_code=status.HTTP_201_CREATED)

    



@Route.put(
    '/{id}',
    status_code=status.HTTP_200_OK,
    summary="Update user",
    description="Update user information",
    tags = ["users"]
    )
async def updateUser(id: int, user: User):
    """Path operation for update user
    Args:
        id: id of user
        user: user to update
    Returns:
        modelUser: user updated
    """
    await update_user(table, id, user.dict())
    return Response(status_code=status.HTTP_200_OK)






@Route.delete(
    '/{id}',
    status_code=status.HTTP_200_OK,
    summary="Delete user",
    description="Delete user information",
    tags = ["users"]
    )
async def deleteUser(id: int):
    """Path operation for delete user
    Args:
        id: id of user
    Returns:
        modelUser: user deleted
    """
    await delete_user(table, id)
    return Response(status_code=status.HTTP_200_OK)
