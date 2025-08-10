import requests


def fetch_extensions():
    url = "https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/extensions/extensions.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
