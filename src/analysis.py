import sqlite3

def analyze_rates():
    conn = sqlite3.connect("data/currency.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT target, rate, timestamp
    FROM rates
    ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    results = {}

    # نخزن آخر و قبل آخر سعر لكل عملة
    temp = {}

    for target, rate, timestamp in rows:
        if target not in temp:
            temp[target] = [rate]  # آخر سعر
        elif len(temp[target]) == 1:
            temp[target].append(rate)  # قبل آخر سعر

    # نحسب التغير
    for target, values in temp.items():
        if len(values) == 2:
            latest = values[0]
            previous = values[1]

            change = latest - previous
            percent = (change / previous) * 100

            results[target] = {
                "latest": latest,
                "previous": previous,
                "change": change,
                "percent": percent
            }
        else:
            results[target] = {
                "latest": values[0],
                "previous": None,
                "change": None,
                "percent": None
            }

    return results