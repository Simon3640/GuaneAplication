
from fastapi import APIRouter, Body, Header, Query, Response, status
from fastapi.responses import JSONResponse
from functions_jwt import validate_token
from config.querys import get_one, get_all, get_dogs_adopted, create_object, update_dog, delete_dog, get_picture
from typing import Optional, List
from models.dog import modelDog
from schemas.dog import Dog, responseDog

table = modelDog.__table__

Route = APIRouter()


@Route.get(
    "/",
    response_model=List[responseDog],
    summary="Get all dogs",
    description="Get information about all dogs in database",
    tags=["dogs"]
    )
async def get_dogs():
    """
    Path operation for get all dogs in database

    this path operation dont reiceve any parameters

    Returns:
        List[modelDog]: List of dogs

    """
    response = await get_all(table)
    return response





@Route.get(
    "/is_adopted",
    response_model=List[responseDog],
    summary="Get all dogs that are adopted",
    description="Get information about all dogs that are adopted",
    tags=["dogs"]
    )
async def dogs_adopted():
    """Path operation for get all dogs that are adopted

    returns:
        List[Dog]: List of dogs that are adopted
    """
    response = await get_dogs_adopted()
    return response

@Route.get(
    "/{name}",
    response_model=responseDog,
    summary="Get dog by name",
    description="Get information about dog by name",
    tags=["dogs"]
    )
async def get_dog(name: str):
    """Path operation for get dog by name

    Args:
        name: name of dog

    returns:
        Dog: dog information
    """
    response = await get_one(table, name)
    if response is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dog not found"})
    return response



@Route.post(
    "/{name}",
    status_code = status.HTTP_201_CREATED,
    summary="Create a dog",
    description="Create a new dog in database",
    tags=["dogs"]
    )
async def post_dog(
    name: str,
    adopted: Optional[bool] = Query(False, description="Is the dog adopted?"),
    auth : str = Header(None)
    ):
    """Path operation for create a dog
    
    Args:
        name: name of dog
        adopted: is the dog adopted?
        auth: token of user
    
    returns:
        Dog: dog information
    """
    validation_response = validate_token(auth, output=False) #Se hace esto pues solo me piden validar el ingreso del canino nuevo
    if validation_response == None:
        image = await get_picture()
        await create_object(table,{"name":name,"picture":image,"is_adopted":adopted})
        return Response(status_code=status.HTTP_201_CREATED)
    else:
        return validation_response





@Route.put(
    "/{name}",
    status_code = status.HTTP_200_OK,
    summary="Update a dog",
    description="Update a dog in database",
    tags=["dogs"]
    )
async def putDog(
    dog : Dog = Body(description="Dog to update"),
    name : str = Query(None, description="Name of dog to update"),
    ):
    """Path operation for update a dog
    
    Args:
        dog: dog to update
        name: name of dog to update
    
    returns:
        Response: response with status code 200 if dog was updated
    """
    await update_dog(table, name, dog.dict())
    return Response(status_code=status.HTTP_200_OK)




@Route.delete(
    "/{name}",
    status_code = status.HTTP_200_OK,
    summary="Delete a dog",
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