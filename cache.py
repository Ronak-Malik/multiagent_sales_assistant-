# cache.py
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def get_cached(key):
    data = r.get(key)
    return json.loads(data) if data else None

def set_cache(key, value, ttl=300):
    r.setex(key, ttl, json.dumps(value))