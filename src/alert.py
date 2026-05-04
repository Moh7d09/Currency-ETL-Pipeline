def check_alerts(results):
    for currency, data in results.items():

        percent = data["percent"]

        if percent is None:
            print(currency, ": no enough data")
            continue

        if percent > 0:
            print(f"{currency}  increased by {percent:.2f}%")
        elif percent < 0:
            print(f"{currency}  decreased by {percent:.2f}%")
        else:
            print(f"{currency}  no change")