import requests

BASE_URL = "https://expensetracker-idh7.onrender.com"

def login(username, password):
    try:
        # data= use panrathu moolama data perfect ah URL-encoded form data ah backend ku pogum
        response = requests.post(
            f"{BASE_URL}/login", 
            data={"username": username, "password": password} 
        )
        if response.status_code == 200:
            return response.json() 
        else:
            return {"error": "Invalid credentials"}
    except requests.exceptions.ConnectionError:
        return {"error": "Backend server is not running"}
