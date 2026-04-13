import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_cached(key):
    try:
        data = r.get(key)
        return json.loads(data) if data else None
    except Exception as e:
        print("Redis GET error:", e)
        return None

def set_cache(key, value, ttl=300):
    try:
        r.setex(key, ttl, json.dumps(value))
    except Exception as e:
        print("Redis SET error:", e)

def delete_cache(key):
    r.delete(key)