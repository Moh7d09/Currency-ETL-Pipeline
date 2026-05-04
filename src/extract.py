import requests
from src.config import BASE_CURRENCY, API_URL

def get_data():
    url = API_URL + BASE_CURRENCY

    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data")
        return None

    data = response.json()

    return data