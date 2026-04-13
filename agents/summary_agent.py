from db import fetch_visits
from cache import get_cached, set_cache

def extract_today(data):
    return [
        d for d in data if d.get("visitDate")
    ]

def summary_agent(state):
    user_id = state["user_id"]
    time_range = state.get("time_range", "weekly")

    cache_key = f"cache:summary:{user_id}:{time_range}"

    data = get_cached(cache_key)

    if data:
        print(f"⚡ CACHE HIT: {cache_key}")
    else:
        print(f"❌ CACHE MISS: {cache_key}")
        data = fetch_visits(user_id, time_range)
        set_cache(cache_key, data, ttl=600)

        # 🔥 Preload today cache if weekly
        if time_range == "weekly":
            today_data = extract_today(data)
            set_cache(f"cache:summary:{user_id}:today", today_data, ttl=300)

    summary_text = state["llm"].invoke(
        f"Generate a concise sales summary from this data:\n{data}"
    )

    return {"response": summary_text.content}