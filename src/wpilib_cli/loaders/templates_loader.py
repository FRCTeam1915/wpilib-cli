from typing import List, Dict

import requests


def fetch_templates_from_github(wpilib_version: str, language: str) -> List[Dict[str, str]]:
    """
    Fetches the list of templates from the ``wpilib-cli-backend`` repository for a specific WPILib version
    :param language: The programming language
    :param wpilib_version: wpilib version
    :return: List of templates
    """
    templates_url = (f"https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/{wpilib_version}"
                     f"/{language}/templates/templates.json")
    res = requests.get(templates_url)
    res.raise_for_status()
    return res.json()
