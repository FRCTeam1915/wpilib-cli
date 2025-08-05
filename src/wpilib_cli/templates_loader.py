import requests

# TODO: Maybe put all the links into a separate file?
def load_templates_from_github(wpilib_version):
    res = requests.get(f"https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/{wpilib_version}/templates/templates.json")
    res.raise_for_status()
    return res.json()
