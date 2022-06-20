from fastapi import FastAPI
from dotenv import load_dotenv
from routes import user
from routes import authorize

#Project

from routes import dog
from starlette.middleware.cors import CORSMiddleware
from config.db import Base, engine



app = FastAPI()

load_dotenv()

<<<<<<< HEAD
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], expose_headers=["*"]) #PERMITIMOS QUE LA API SEA ACCESIBLE DESDE TODOS LOS DOMINIOS

Base.metadata.create_all(bind=engine) #Permite crear las tablas de la base de datos
=======
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], expose_headers=["*"])

Base.metadata.create_all(bind=engine)
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7


app.include_router(authorize.Route, prefix="/api")

app.include_router(dog.Route, prefix="/api/dogs")

app.include_router(user.Route, prefix="/api/users")



