# apitw132

La API realiza varias peticiones a la API de Twitter. El código principal de este proyecto está en `routes/user.py`.

La idea principal de la API es **obtener los últimos resultados de tweets con un filtro de cuenta y palabra clave**, conectado a una base de datos local (MySQL) que se ejecuta en un Docker.

Para acceder a la API de Twitter se ha creado una aplicación con [FastAPI](https://fastapi.tiangolo.com/) y me he servido de [Tweepy](https://www.tweepy.org/) para realizar las conexiones. Para poder realizar dicha conexión se necesita un proyecto de categoría "Elevated" en Twitter Developer Portal, donde solicitaremos unas credenciales: 

- Api key
- Api key secret 
- Access token
- Access token secret
- Bearer token 

Además una autentificación 0.1Auth para que nos permita la función *Read and Write*.

### Ejecución

Para lanzar el proyecto se debe lanzar a través de [Uvicorn](https://www.uvicorn.org/), con el comando '`uvicorn app:app`', que nos creará un servidor local, con puerto por defecto 8000; iremos a la dirección `localhost:8000/docs` donde se podrán realizar las peticiones HTTP que hemos creado.