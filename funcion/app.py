from fastapi import FastAPI
from routes.user import user

#Creacion de la api
app=FastAPI(
title='APITW132',
version= '0.0.1',
openapi_tags=[{
'name': 'Apitw132',
'description': 'Esta API utiliza Tweepy y fastapi para realizar busqueda de tweets con palabras clave y lo registra en una base de datos relacional SQL'
}]
)

app.include_router(user)