import requests

URL = "https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/main/versions.json"

def load_versions():
    res = requests.get(URL)
    res.raise_for_status()
    return res.json().get("versions", [])
