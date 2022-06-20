<<<<<<< HEAD
from pydantic import BaseModel, Field



#Se define el modelo usuario
=======
from typing import Optional
from pydantic import BaseModel, Field

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
class User(BaseModel):
    name : str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="The name of the user",
        example="Simón"
    )
    last_name : str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="The last name of the user",
        example="García"
    )
    email : str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="The email of the user",
        example="user@mail.com"
    )
    
<<<<<<< HEAD
# Esta clase hereda de User y nos ayuda a actualizar el usuario
=======

>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7
class responseUser(User):
    id : int = Field(
        ...,
        description="The id of the user",
        example=1
    )