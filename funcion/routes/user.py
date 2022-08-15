from fastapi import APIRouter
from config.db import conn
from models.user import tweets
from twitterapi import client
from schemas.tweet import Tweet
import datetime
from datetime import date


user = APIRouter()


@user.get('/tweet/{tw_id}') #devuelve un tweet con una de la base de datos id
def get_tweet(tw_id: str):
    res= conn.execute(tweets.select().where(tweets.c.tw_id == tw_id)).first()
    return res


@user.get('/tweets/{cuenta}') #devuelve todos los tweets de una cuenta
def get_tweet_cuenta(cuenta: str):
    return conn.execute(tweets.select().where(tweets.c.cuenta == cuenta)).fetchall()



@user.get('/tweets/{fecha}') #devuelve todos los tweets de una fecha
def get_tweet_fecha(fecha: date):
    return conn.execute(tweets.select().where(tweets.c.fecha == fecha)).fetchall()


@user.get('/tweets') #devuelve todos los tweets de la bd
def get_tweets(): 
    return conn.execute(tweets.select()).fetchall()

@user.get('/{query}')
def get_res_query(query: str):
    return conn.execute(tweets.select().where(tweets.c.clave == query)).fetchall()


@user.post('/tweets')
def add_tweet(tweet: Tweet):
    new_tweet = {'fecha':tweet.fecha, 'cuenta':tweet.cuenta, 'clave':tweet.clave, 'tw_id':tweet.tw_id, 'tw_content':tweet.tw_content}
    conn.execute(tweets.insert().values(new_tweet)) 
    return f'El tweet {tweet.tw_id} se ha guardado correctamente'


@user.post('/{query}')
def get_results(clave:str):
    query_results = client.search_recent_tweets(query=clave, tweet_fields=['created_at'], expansions= 'author_id', max_results=10)
    content_to_add=[]

    for f in query_results.data:
        content_dict={}

        dates=datetime.datetime.date(f['created_at'])
        content_dict['fecha']=str(dates)
        
        author=(f['author_id'])
        content_dict['cuenta']=str(author)

        content_dict['clave']=clave
        
        id=f['id']
        content_dict['tw_id']=str(id)

        text=f['text']
        content_dict['tw_content']=str(text)
        content_to_add.append(content_dict)
        
    conn.execute(tweets.insert(), content_to_add)

    #añadir a la base de datos
    return 'base de datos actualizada con nuevos mensajes'


@user.delete('/tweet/{tw_id}')
def delete_tweet(id: str):
    conn.execute(tweets.delete().where(tweets.c.tw_id ==id))
    return f'El tweet con {id} se ha eliminado'