# apitw132

La api realiza varias peticiones a la api de twitter. El código principal de este proyecto está en routes/user.py.
La idea principal de la api es obtener los ultimos resultados de tweets con un filtro de cuenta y palabra clave, conectado a una base de datos local que se ejecuta en un docker.
Para acceder a la api de twitter he creado una aplicacion con fastapi y me he servido de Tweepy para realizar las conexiones, para poder realizar dicha conexion se necesita un proyecto de categoria "Elevated" en Twitter dev, posteriormente solicitaremos unas credenciales a saber: Api key, api key secret, access token, access token secret y bearer token ademas una autentificacion 0.1Auth para que nos permita la funcion Read and Write.
