import json
import os.path


def update_wpilib_preferences(project_dir: str, team_num: str) -> None:
    """
    Updates the wpilib_preferences.json file with the team number
    :param project_dir: The directory of the created project
    :param team_num: The team number
    :return: None
    """
    prefs_path = os.path.join(project_dir, ".wpilib", "wpilib_preferences.json")

    if not os.path.exists(prefs_path):
        print(f"⚠️ wpilib_preferences.json not found at {prefs_path}")
        return

    with open(prefs_path, "r", encoding="utf-8") as f:
        prefs = json.load(f)

    prefs["teamNumber"] = int(team_num)

    with open(prefs_path, "w", encoding="utf-8") as f:
        json.dump(prefs, f, indent=4)

    print(f"✅ Team number updated to {team_num} in wpilib_preferences.json")
