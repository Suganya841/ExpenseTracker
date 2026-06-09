import requests

BASE_URL = "https://expensetracker-idh7.onrender.com"

def login(username, password):
    response = requests.post(
        f"{BASE_URL}/login",
        data={
            "username": username,
            "password": password
        }
    )
    return response.json()
