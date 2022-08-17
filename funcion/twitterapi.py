import keys as k
import tweepy
import logging


auth = tweepy.OAuthHandler(k.api_k, k.api_k_secret)
auth.set_access_token(k.access_t, k.access_t_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token = k.bearer_t)

try:
    api.verify_credentials()

except Exception as e:
    logging.info('Error en la asignacion de credenciales')
    raise e

logging.info('perfect')
