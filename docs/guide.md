# Guide

Para ejecutar esta api se debe lanzar el servidor de uvicorn mediante "uvicorn app:app" y a partir de ahi usar las peticiones HTTP para ir ejecutando los bloques de código.

Puedes comprobar la conexion de la base de datos local en config/db:

```
engine = create_engine('<packages>://<databaseUser>:<databasePassword>@localhost:<port>/<your database name>', 
pool_pre_ping=True(checks that database is connected))
```
