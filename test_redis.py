import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Set value
r.set("test_key", "Hello Redis")

# Get value
data = r.get("test_key")

print("Value from Redis:", data)