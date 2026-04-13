# db.py

from google.cloud import firestore
from utils import get_time_range
import os

# 🔥 Load service account JSON directly (no env dependency)
db = firestore.Client.from_service_account_json(
    os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")
)

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

    print(f"📦 DB FETCH: {len(results)} records for {range_type}")

    return results