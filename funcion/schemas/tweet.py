from pydantic import BaseModel


# Modelo base para la creacion de un tweet
class Tweet(BaseModel):
    fecha: str
    cuenta: str
    clave: str
    tw_id: str
    tw_content: str
