import requests

from wpilib_cli.utils import run_gradle_command


def fetch_extensions():
    url = "https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/extensions/extensions.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def add_extension(project_dir, ext_url):
    """Adds a WPILib extension from the provided JSON URL"""
    run_gradle_command(project_dir, ["vendordep", f"--url={ext_url}"])