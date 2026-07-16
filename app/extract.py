import requests

URL = "https://jsonplaceholder.typicode.com/users"

def get_customers():
    response = requests.get(URL)
    response.raise_for_status()


    return response.json()
