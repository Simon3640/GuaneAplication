# Prueba Backend Guane

Para correr la API corra el siguiente comando en el directiorio 
```sh
docker compose -d --build
```

Para entrar a la interfaz de Swagger ingrese mediante:

```sh
http://localhost:8000/docs
```

También agregué un container de flower para observar el progreso del celery worker, se puede ver en:


```sh
http://localhost:5555
```
