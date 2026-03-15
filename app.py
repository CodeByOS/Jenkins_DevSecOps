import requests

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def get_data(url):
    response = requests.get(url)
    return response.status_code