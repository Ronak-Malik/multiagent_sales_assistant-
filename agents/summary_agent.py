# agents/summary_agent.py
from db import fetch_visits
from cache import get_cached, set_cache

def summary_agent(state):
    user_id = state["user_id"]
    time_range = state["time_range"]

    cache_key = f"summary:{user_id}:{time_range}"

    data = get_cached(cache_key)

    if not data:
        data = fetch_visits(user_id, time_range)
        set_cache(cache_key, data)

    # Send only filtered data to LLM
    summary_text = state["llm"].invoke(
        f"Generate a sales summary from this data:\n{data}"
    )

    return {"response": summary_text}