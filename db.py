# db.py
from google.cloud import firestore
from utils import get_time_range

db = firestore.Client()

ESSENTIAL_FIELDS = [
    "visitDate",
    "meetingSummary",
    "outcomeStatus",
    "customerName",
    "customerEmotion",
    "dealProbability",
    "followUpDate",
    "nextStep"
]

def fetch_visits(user_id: str, range_type: str):
    start, end = get_time_range(range_type)

    docs = db.collection("visits") \
        .where("salesPersonId", "==", user_id) \
        .where("visitDate", ">=", start) \
        .where("visitDate", "<", end) \
        .stream()

    results = []
    for doc in docs:
        data = doc.to_dict()

        # 🔥 Extract only essential fields
        filtered = {k: data.get(k) for k in ESSENTIAL_FIELDS}
        results.append(filtered)

    return results