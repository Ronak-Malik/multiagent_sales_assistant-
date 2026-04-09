# utils.py
from datetime import datetime, timedelta

def get_time_range(range_type: str):
    now = datetime.utcnow()

    if range_type == "today":
        start = datetime(now.year, now.month, now.day)
        end = start + timedelta(days=1)

    elif range_type == "weekly":
        start = now - timedelta(days=7)
        end = now

    elif range_type == "monthly":
        start = now - timedelta(days=30)
        end = now

    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)