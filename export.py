import pandas as pd
from src.analysis import analyze_rates

def export_to_csv():
    data = analyze_rates()

    rows = []

    for currency, info in data.items():
        rows.append({
            "currency": currency,
            "latest": info["latest"],
            "previous": info["previous"] or 0,
            "percent": info["percent"] or 0
        })

    df = pd.DataFrame(rows)

    df.to_csv("data/rates.csv", index=False)

    print("Exported to CSV ✔️")


if __name__ == "__main__":
    export_to_csv()