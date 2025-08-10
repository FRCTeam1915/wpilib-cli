from typing import List

import requests


def fetch_wpilib_versions_from_github() -> List[str]:
    """
    Fetches the list of wpilib versions from the ``wpilib-cli-backend`` repository
    :return: The json body
    """
    ver_url = "https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/main/versions.json"
    res = requests.get(ver_url)
    res.raise_for_status()
    return res.json().get("versions", [])
