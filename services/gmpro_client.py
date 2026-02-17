import requests
from core.config import settings
from core.auth import get_access_token

def call_gmpro(model_body):
    token = get_access_token()

    url = f"https://routeoptimization.googleapis.com/v1/projects/{settings.PROJECT_ID}/locations/{settings.LOCATION}:optimizeTours"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Server-Timeout": str(settings.TIMEOUT)
    }

    response = requests.post(url, json=model_body, headers=headers)

    if response.status_code != 200:
        raise Exception(response.text)

    return response.json()
