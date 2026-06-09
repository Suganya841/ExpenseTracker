import requests

BASE_URL = "https://expensetracker-idh7.onrender.com"

def login(username, password):
    try:
        response = requests.post(
            f"{BASE_URL}/login",
            data={
                "username": username,
                "password": password
            },
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        # better error handling
        try:
            return response.json()
        except:
            return {"error": response.text}

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
