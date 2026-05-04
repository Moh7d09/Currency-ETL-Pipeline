import sqlite3

def save_data(records):
    conn = sqlite3.connect("data/currency.db")
    cursor = conn.cursor()
    # cursor.execute("DELETE FROM rates")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rates (
        timestamp TEXT,
        base TEXT,
        target TEXT,
        rate REAL
    )
    """)

    for record in records:
        target = record["target"]
        new_rate = record["rate"]

        # نجيب آخر سعر لنفس العملة
        cursor.execute("""
        SELECT rate FROM rates
        WHERE target = ?
        ORDER BY timestamp DESC
        LIMIT 1
        """, (target,))

        last = cursor.fetchone()

        # لو ما في بيانات أو السعر تغيّر
        if last is None or last[0] != new_rate:
            cursor.execute(
                "INSERT INTO rates VALUES (?, ?, ?, ?)",
                (
                    str(record["timestamp"]),
                    record["base"],
                    record["target"],
                    record["rate"]
                )
            )

    conn.commit()
    conn.close()