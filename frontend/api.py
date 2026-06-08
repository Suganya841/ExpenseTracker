import requests
from frontend.utils.api import login

BASE_URL = "http://127.0.0.1:8000"

def health_check():
    return requests.get(f"{BASE_URL}/health").json()