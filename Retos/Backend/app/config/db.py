from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

<<<<<<< HEAD

#Este documento nos permite hacer la conexión a la base de datos de mysql a través de pymysql, hemos de notar que en el docker la base de datos estará en la network, es por esto que no se conecta como localhost
user_name = "user"
password = "password"
host = "db"
database_name = "dogs_db"

DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)


engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
) #Creamos el motor que permite la conexión a la base de datos


#conn = engine.connect() # de esta manerra se llama a la base de datos, es 
=======
engine = create_engine("mysql+pymysql://root:Deadmatch3640@localhost:3306/test")

conn = engine.connect()
>>>>>>> d95075ea65709eb096846bf4f0c382d9e5df37a7

Base = declarative_base()

meta_data = MetaData(engine)