import json

from wpilib_cli.utils.preferences import update_wpilib_preferences


def test_update_wpilib_preferences_updates_file(tmp_path):
    project_dir = tmp_path
    wpilib_dir = project_dir / ".wpilib"
    wpilib_dir.mkdir()

    prefs_path = wpilib_dir / "wpilib_preferences.json"
    initial_data = {
        "enableCppIntellisense": False,
        "currentLanguage": "java",
        "projectYear": "2025",
        "teamNumber": -1
    }

    with prefs_path.open("w", encoding="utf-8") as f:
        json.dump(initial_data, f)

    update_wpilib_preferences(str(project_dir), "1915")

    with prefs_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["enableCppIntellisense"] is False
    assert data["currentLanguage"] == "java"
    assert data["projectYear"] == "2025"
    assert data["teamNumber"] == 1915
