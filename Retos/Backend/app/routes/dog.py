
from fastapi import APIRouter, Body, Header, Query, Response, status
from fastapi.responses import JSONResponse
<<<<<<< HEAD
from celery_worker import create_task
from functions_jwt import validate_token
from config.querys import get_one, get_all, get_dogs_adopted, update_dog, delete_dog, get_picture
=======
from functions_jwt import validate_token
from config.querys import get_one, get_all, get_dogs_adopted, create_object, update_dog, delete_dog, get_picture
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
from typing import Optional, List
from models.dog import modelDog
from schemas.dog import Dog, responseDog

<<<<<<< HEAD
table = modelDog.__table__ #Tabla de perros para ingresar como parámetro a las funciones de querys

Route = APIRouter()

#Path operation que permite obtener todos los perros de la base de datos
=======
table = modelDog.__table__

Route = APIRouter()


>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.get(
    "/",
    response_model=List[responseDog],
    summary="Get all dogs",
<<<<<<< HEAD
=======
    description="Get information about all dogs in database",
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
    tags=["dogs"]
    )
async def get_dogs():
    """
    Path operation for get all dogs in database

<<<<<<< HEAD
        this path operation dont reiceve any parameters

    Returns

=======
    this path operation dont reiceve any parameters

    Returns:
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
        List[modelDog]: List of dogs

    """
    response = await get_all(table)
    return response




<<<<<<< HEAD
#Este endpoint nos devuelve los perros adoptados
=======

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.get(
    "/is_adopted",
    response_model=List[responseDog],
    summary="Get all dogs that are adopted",
<<<<<<< HEAD
    tags=["dogs"]
    )
async def dogs_adopted():
    """
    Path operation for get all dogs that are adopted

    returns:

        List[Dog]: List of dogs that are adopted
    
=======
    description="Get information about all dogs that are adopted",
    tags=["dogs"]
    )
async def dogs_adopted():
    """Path operation for get all dogs that are adopted

    returns:
        List[Dog]: List of dogs that are adopted
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
    """
    response = await get_dogs_adopted()
    return response

<<<<<<< HEAD

#Este endpoint nos devuelve el PRIMER perro con nombre name
=======
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.get(
    "/{name}",
    response_model=responseDog,
    summary="Get dog by name",
<<<<<<< HEAD
    tags=["dogs"]
    )
async def get_dog(name: str):
    """
    Path operation for get dog by name

    Args:

        name: name of dog

    returns:

=======
    description="Get information about dog by name",
    tags=["dogs"]
    )
async def get_dog(name: str):
    """Path operation for get dog by name

    Args:
        name: name of dog

    returns:
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
        Dog: dog information
    """
    response = await get_one(table, name)
    if response is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dog not found"})
    return response


<<<<<<< HEAD
#Esta es la única path operation que le asigné un worker de celery, es lo que se pide en la prueba
=======

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.post(
    "/{name}",
    status_code = status.HTTP_201_CREATED,
    summary="Create a dog",
<<<<<<< HEAD
=======
    description="Create a new dog in database",
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
    tags=["dogs"]
    )
async def post_dog(
    name: str,
    adopted: Optional[bool] = Query(False, description="Is the dog adopted?"),
<<<<<<< HEAD
    auth : str = Header(None),
    s : Optional[int] = Query(0, description="Delay in seconds")
    ):
    """
    Path operation for create a dog
    
    Args:

        name: name of dog
        adopted: is the dog adopted?
        s: delay in seconds
        auth: token of user
    
    returns:

=======
    auth : str = Header(None)
    ):
    """Path operation for create a dog
    
    Args:
        name: name of dog
        adopted: is the dog adopted?
        auth: token of user
    
    returns:
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
        Dog: dog information
    """
    validation_response = validate_token(auth, output=False) #Se hace esto pues solo me piden validar el ingreso del canino nuevo
    if validation_response == None:
<<<<<<< HEAD
        
        picture = await get_picture()
        
        data = {
            "name": name,
            "is_adopted": adopted*1,
            "picture": picture
        }

        response = create_task.apply_async((data , s), countdown=s)
        response = response.get()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Dog created"})
=======
        image = await get_picture()
        await create_object(table,{"name":name,"picture":image,"is_adopted":adopted})
        return Response(status_code=status.HTTP_201_CREATED)
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
    else:
        return validation_response




<<<<<<< HEAD
#Estpath operation permite actualizar el PRIMER perro con nombre name
=======

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.put(
    "/{name}",
    status_code = status.HTTP_200_OK,
    summary="Update a dog",
<<<<<<< HEAD
=======
    description="Update a dog in database",
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
    tags=["dogs"]
    )
async def putDog(
    dog : Dog = Body(description="Dog to update"),
    name : str = Query(None, description="Name of dog to update"),
    ):
<<<<<<< HEAD
    """
    Path operation for update a dog
    
    Args:

        dog as JSON: 
            name: name of dog if have new name
            is_adopted: is the dog adopted?
            user_id: id of user
            created_date: date of creation
            picture: picture of dog
        name: name of dog to update
    
    returns:

        Response: response with status code 200 if dog was updated
    """
    await update_dog(table, name, dog.dict())
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dog updated"})



#Estpath operation permite eliminar el PRIMER perro con nombre name
=======
    """Path operation for update a dog
    
    Args:
        dog: dog to update
        name: name of dog to update
    
    returns:
        Response: response with status code 200 if dog was updated
    """
    await update_dog(table, name, dog.dict())
    return Response(status_code=status.HTTP_200_OK)




>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
@Route.delete(
    "/{name}",
    status_code = status.HTTP_200_OK,
    summary="Delete a dog",
<<<<<<< HEAD
    tags=["dogs"]
    )
async def deleteDog(name: str):
    """
    Path operation for delete a dog
    
    Args:

        name: name of dog to delete
    
    returns:

        Response: response with status code 200 if dog was deleted
    """
    await delete_dog(table, name)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dog deleted"})
=======
    description="Delete a dog in database",
    tags=["dogs"]
    )
async def deleteDog(name: str):
    """Path operation for delete a dog
    
    Args:
        name: name of dog to delete
    
    returns:
        Response: response with status code 200 if dog was deleted
    """
    await delete_dog(table, name)
    return Response(status_code=status.HTTP_200_OK)
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
