from typing import List
<<<<<<< HEAD
from fastapi import APIRouter, Response, UploadFile, status, File
from fastapi.responses import JSONResponse
from sqlalchemy import table
from schemas.dog import responseDog
from models.user import modelUser
from config.querys import get_all, get_one_user, create_object, delete_user, update_user, dogs_by_user, put_file
=======
from fastapi import APIRouter, Response, status
from sqlalchemy import table
from schemas.dog import responseDog
from models.user import modelUser
from config.querys import get_all, get_one_user, create_object, delete_user, update_user, dogs_by_user
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7

from schemas.user import User, responseUser

Route=APIRouter()
table = modelUser.__table__

<<<<<<< HEAD
#Path operation que permite obtener todos los usuarios de la base de datos
=======
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.get(
    '/',
    response_model=List[responseUser],
    summary="Get all users",
<<<<<<< HEAD
=======
    description="Get information about all users in database",
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
    tags = ["users"]
    )
async def get_users():
    """
    Path operation for get all users in database
<<<<<<< HEAD
    
    this path operation dont reiceve any parameters
    
    Returns:
    
=======
    this path operation dont reiceve any parameters
    Returns:
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
        List[modelUser]: List of users
    """
    response = await get_all(table)
    return response


<<<<<<< HEAD
#Path operation que permite obtener un usuario de la base de datos
=======

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.get(
    '/{id}',
    response_model=responseUser,
    summary="Get user by id",
<<<<<<< HEAD
    tags = ["users"]
    )
async def get_user(id: int):
    """
    Path operation for get user by id
    
    Args:
    
        id: id of user
    
    Returns:
    
=======
    description="Get information about user by name",
    tags = ["users"]
    )
async def get_user(id: int):
    """Path operation for get user by id
    Args:
        id: id of user
    Returns:
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
        modelUser: user
    """
    response = await get_one_user(table, id)
    return response

<<<<<<< HEAD
#Este endpoint nos devuelve los perros adoptados por el usuario con id id
=======

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.get(
    '/dogs/{id}',
    response_model=List[responseDog],
    summary="Get dogs by user id",
<<<<<<< HEAD
    tags = ["dogs"]
)
async def get_dogs_by_user(id: int):
    """
    Path operation for get dogs adopted by user id
    
    Args:
    
        id: id of user
    
    Returns:
    
=======
    description="Get information about dogs by user id",
    tags = ["dogs"]
)
async def get_dogs_by_user(id: int):
    """Path operation for get dogs by user id
    Args:
        id: id of user
    Returns:
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
        List[modelDog]: List of dogs
    """
    response = await dogs_by_user(id)
    return response


<<<<<<< HEAD
#Este endpoint nos permite crear un nuevo usuario
=======



>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.post(
    '/',
    status_code = status.HTTP_201_CREATED,
    summary="Create user",
<<<<<<< HEAD
    tags = ["users"]
    )
async def create_user(user: User):
    """
    Path operation for create user
    
    This path operation receive a user object as JSON:
    
        name: name of user
        last_name: last name of user
        email: email of user

    
    Returns:
    
        modelUser: user created
    """
    await create_object(table, user.dict())
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "User created"})
=======
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
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7

    


<<<<<<< HEAD
#Este endpoint nos permite actualizar el usuario con id id
=======

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.put(
    '/{id}',
    status_code=status.HTTP_200_OK,
    summary="Update user",
<<<<<<< HEAD
    tags = ["users"]
    )
async def updateUser(id: int, user: User):
    """
    Path operation for update user
    
    Args:
    
        id: id of user
        user as JSON:
            name : name of user
            last_name : last name of user
            email : email of user
    
    Returns:
    
        modelUser: user updated
    """
    await update_user(table, id, user.dict())
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "User updated"})


#Este endpoint permite eliminar el usuario con id id
=======
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






>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.delete(
    '/{id}',
    status_code=status.HTTP_200_OK,
    summary="Delete user",
    description="Delete user information",
    tags = ["users"]
    )
async def deleteUser(id: int):
<<<<<<< HEAD
    """
    Path operation for delete user
    
    Args:
    
        id: id of user
    
    Returns:
    
        modelUser: user deleted
    """
    await delete_user(table, id)
    return JSONResponse({"message": "User deleted"},200)


#TODO: Pongo esto aquí para no poner una ruta para un único path operation
@Route.post(
    '/file',
    status_code=status.HTTP_200_OK,
    summary="Get file",
    tags = ["file"]
    )
async def get_file():
    """
    Path operation for get file
    
    Args:
      
        file: file to get
    
    Returns:
      
        UploadFile: file
    """
    response = await put_file()
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)
=======
    """Path operation for delete user
    Args:
        id: id of user
    Returns:
        modelUser: user deleted
    """
    await delete_user(table, id)
    return Response(status_code=status.HTTP_200_OK)
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
