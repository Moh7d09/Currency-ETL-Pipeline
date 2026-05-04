from datetime import datetime
from src.config import BASE_CURRENCY

def transform_data(data):
    rates = data["rates"]

    targets = ["INR", "EUR", "AED","EGP","SDG","SAR"]

    records = []

    for currency in targets:
        record = {
            "timestamp": datetime.now(),
            "base": BASE_CURRENCY,
            "target": currency,
            "rate": rates[currency]
        }
        records.append(record)

    return records