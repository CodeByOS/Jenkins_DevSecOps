import requests

def get_data():
    r = requests.get("https://api.github.com")
    return r.status_code