import requests

BASE_URL = "https://expensetracker-idh7.onrender.com"

def login(username, password):
    try:
        response = requests.post(
            f"{BASE_URL}/login",
            data={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}

    except Exception as e:
        return {"error": str(e)}
