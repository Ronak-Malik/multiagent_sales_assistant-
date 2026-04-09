# agents/followup_agent.py
from db import fetch_visits
from cache import get_cached, set_cache

def followup_agent(state):
    user_id = state["user_id"]
    time_range = state["time_range"]

    cache_key = f"followup:{user_id}:{time_range}"

    data = get_cached(cache_key)

    if not data:
        data = fetch_visits(user_id, time_range)
        set_cache(cache_key, data)

    followups = [
        d for d in data if d.get("followUpDate")
    ]

    return {
        "response": f"Upcoming followups:\n{followups}"
    }