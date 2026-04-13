from db import fetch_visits
from cache import get_cached, set_cache

def followup_agent(state):
    user_id = state["user_id"]
    time_range = state.get("time_range", "weekly")

    cache_key = f"cache:followup:{user_id}:{time_range}"

    data = get_cached(cache_key)

    if data:
        print(f"⚡ CACHE HIT: {cache_key}")
    else:
        print(f"❌ CACHE MISS: {cache_key}")
        data = fetch_visits(user_id, time_range)
        set_cache(cache_key, data, ttl=300)

    followups = [
        d for d in data if d.get("followUpDate")
    ]

    return {
        "response": f"📞 Followups:\n{followups}"
    }