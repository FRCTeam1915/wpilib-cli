from typing import List, Dict, Set

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


def add_extension_to_project(project_dir: str, extension_name: str, extensions: List[Dict[str, str]], added_extensions: Set[str] = None) -> None:
    """
    Adds a vendor extension to the project by running the `vendordep` Gradle task
    :param project_dir: The directory of the project
    :param extension_name: The name of the extension to add
    :param extensions: The list of available extensions
    :param added_extensions: A set of already added extensions to avoid duplicates
    :return: None
    """

    if added_extensions is None:
        added_extensions = set()

    if extension_name in added_extensions:
        return

    extension = next((e for e in extensions if e["name"] == extension_name), None)
    if not extension:
        return

    for dependency in extension.get("dependencies", []):
        add_extension_to_project(project_dir, dependency, extensions, added_extensions)

    print(f"🔌 Adding extension to the project: {extension['name']}")
    run_gradle_command(project_dir, ["vendordep", f"--url={extension['json_url']}"])
    run_gradle_command(project_dir, ["build"])
    added_extensions.add(extension_name)
