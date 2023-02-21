import redis
import os

def redis_connection() ->  redis.Redis:
    try:
        r = redis.Redis()
        return r
    except:
        return None
