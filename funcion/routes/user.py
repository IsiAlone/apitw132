from fastapi import APIRouter
from config.db import conn
from models.user import tweets
from schemas.tweet import Tweet
from datetime import date


user = APIRouter()

query = 'from:elmundoes ucrania'

tweets_list=[]
tweets_7=client.search_recent_tweets(query=query, tweet_fields=['created_at'], expansions= 'author_id', max_results=10)
tweets_list.append(tweets_7)
for t in tweets_7.data:
    dates=t['created_at']
    datess=datetime.datetime.date(dates)
    print(datess)

@user.get('/{cuenta}&{clave}')
def get_results(date:date, cuenta:str, clave:str, resultados: int):
    tweets = client.search_recent_tweets(query=clave, tweet_fields=['created_at'],  expansions= 'author_id', max_results=resultados)
    fecha,tw_id,tw_content=[],[],[]
    for f in tweets.data: #f:fecha, t:tw_id tx:tw_contexnt
        dates=datetime.datetime.date(f['created_at'])
        fecha.append(str(dates))
    for t in tweets.data:
        id=t['id']
        tw_id.append(str(id))
    for tx in tweets.data:
        text=tx['text']
        tw_content.append(str(text))
    account=[cuenta]*resultados
    keyword=[clave]*resultados
    
    
    
        

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


@user.post('/tweets')
def add_tweet(tweet: Tweet):
    new_tweet = {'fecha':tweet.fecha, 'cuenta':tweet.cuenta, 'clave':tweet.clave, 'tw_id':tweet.tw_id, 'tw_content':tweet.tw_content}
    conn.execute(tweets.insert().values(new_tweet)) 
    return f'El tweet {tweet.tw_id} se ha guardado correctamente'


@user.delete('/tweet/{tw_id}')
def delete_tweet(id: str):
    conn.execute(tweets.delete().where(tweets.c.tw_id ==id))
    return f'El tweet con {id} se ha eliminado'
