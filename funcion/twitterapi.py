import keys as k
import tweepy
import logging

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
content_to_add2=[]
fecha_to_add,tw_id_to_add,tw_content_to_add,query_to_add={},{},{},{}
print(tweets)

for q in range(10): #f:fecha, t:tw_id tx:tw_contexnt
    clave=[]
    clave.append(query)
    for q2 in clave:
        query_to_add['query']=q2
        content_to_add2.append(query_to_add)

print(content_to_add2)