import keys as k
import tweepy
import logging
import datetime

#Autentificacion en la API de Twitter
auth = tweepy.OAuthHandler(k.api_k,k.api_k_secret)
auth.set_access_token(k.access_t, k.access_t_secret)
api=tweepy.API(auth)
client= tweepy.Client(bearer_token = k.bearer_t) #para poder extraer informacion de twitter V2

try:
    api.verify_credentials()

except Exception as e:
    logging.info('Error en la asignacion de credenciales')
    raise e

logging.info('perfect')


query = 'from:elmundoes ucrania'

tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'],  expansions= 'author_id', max_results=10)
fecha,tw_id,tw_content=[],[],[]
for tx in tweets.data:
    text=tx['text']
    tw_content.append(str(text))
    
print(tw_content)