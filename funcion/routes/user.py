from fastapi import APIRouter
from config.db import conn
from models.user import tweets
from twitterapi import client
from schemas.tweet import Tweet
import datetime


user = APIRouter()


@user.get('/tweet/{tw_id}')
def get_tweet(tw_id: str):
    """
    It takes a tweet id as a string, and returns the first row of the tweets table that matches that id

    Args:
      tw_id (str): the id of the tweet
    
    Returns:
        The same tweet id than the function.
    """
    res = conn.execute(tweets.select().where(tweets.c.tw_id == tw_id)).first()
    return res


@user.get('/tweets/{cuenta}')
def get_tweet_cuenta(cuenta: str):
    """
    It returns all the tweets from a given account
    
    Args:
      cuenta (str): str
    
    Returns:
      All tweets filtered by account.
    """
    return conn.execute(tweets.select().where(tweets.c.cuenta == cuenta)).fetchall()


@user.get('/tweets/{fecha}')
def get_tweet_fecha(fecha: str):
    """
    It returns all the tweets from the database that have the same date as the one passed as an argument
    
    Args:
      fecha (str): str
    
    Returns:
      Tweets by date.
    """
    return conn.execute(tweets.select().where(tweets.c.fecha == fecha)).fetchall()


@user.get('/tweets')
def get_tweets():
    """
    It returns all the tweets in the database
    
    Returns:
        All tweets in the database.
    """
    return conn.execute(tweets.select()).fetchall()


@user.get('/{query}')
def get_res_query(query: str):
    """
    It takes a string as input and returns a list of tuples
    
    Args:
      query (str): str
    
    Returns:
      Tweets by query.
    """
    return conn.execute(tweets.select().where(tweets.c.clave == query)).fetchall()


@user.post('/tweets')
def add_tweet(tweet: Tweet):
    """
    It takes a Tweet object as an argument, creates a dictionary with the object's attributes, and
    inserts the dictionary into the tweets table
    
    Args:
      tweet (Tweet): Tweet
    
    Returns:
      Add a single tweet to the database
    """
    new_tweet = {
        'fecha': tweet.fecha, 'cuenta': tweet.cuenta, 'clave': tweet.clave, 
        'tw_id': tweet.tw_id, 'tw_content': tweet.tw_content
    }

    conn.execute(tweets.insert().values(new_tweet)) 
    return f'El tweet {tweet.tw_id} se ha guardado correctamente'


@user.post('/{query}')
def get_results(clave: str):
    """
    It takes a string as an argument, uses the Twitter API to get the last 10 tweets that contain that
    string, and then adds them to the database
    
    ```
    clave = 'from:<twitteraccount> <keyword> '
    ```

    Args:
      clave (str): the keyword you want to search for
    
    Returns:
      Confirmation string to make sure the search was done and saved it in database.
    """
    query_results = client.search_recent_tweets(query=clave, tweet_fields = ['created_at'], expansions = 'author_id', max_results = 10)
    content_to_add = []

    for f in query_results.data:
        content_dict = {}

        dates = datetime.datetime.date(f['created_at'])
        content_dict['fecha'] = str(dates)
        
        author = (f['author_id'])
        content_dict['cuenta'] = str(author)

        content_dict['clave'] = clave
        
        id = f['id']
        content_dict['tw_id'] = str(id)

        text = f['text']
        content_dict['tw_content'] = str(text)
        content_to_add.append(content_dict)
        
    conn.execute(tweets.insert(), content_to_add)

    return 'Tweets añadidos a la base de datos'


@user.delete('/tweet/{tw_id}')
def delete_tweet(id: str):
    """
    It deletes a tweet from the database
    
    Args:
      id (str): str
    
    Returns:
      The tweet with the id has been deleted
    """
    conn.execute(tweets.delete().where(tweets.c.tw_id == id))
    return f'El tweet con {id} se ha eliminado'
