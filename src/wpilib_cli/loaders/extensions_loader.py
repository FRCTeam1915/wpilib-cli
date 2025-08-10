from typing import List, Dict

import requests

from wpilib_cli.utils.gradle import run_gradle_command


def fetch_extensions_from_github() -> List[Dict[str, str]]:
    """
    Fetches the list of extensions from the ``wpilib-cli-backend`` repository
    :return: The json body
    """
    ext_url = "https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/extensions/extensions.json"
    res = requests.get(ext_url)
    res.raise_for_status()
    return res.json()


def add_extension_to_project(project_dir: str, ext_url: str) -> None:
    """
    Adds an extension to the project by running the vendordep command with the provided URL
    :param project_dir: The directory of the project
    :param ext_url: The URL of the extension to add
    :return: None
    """
    run_gradle_command(project_dir, ["vendordep", f"--url={ext_url}"])
