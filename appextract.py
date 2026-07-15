import requests

def get_customers():
    response = requests.get(
        "https://jsonplaceholder.org/posts"
    )

    return response.json()
