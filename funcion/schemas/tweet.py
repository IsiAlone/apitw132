from pydantic import BaseModel
from datetime import date

class Tweet(BaseModel):
    fecha: date
    cuenta: str
    clave: str
    tw_id: str
    tw_content: str