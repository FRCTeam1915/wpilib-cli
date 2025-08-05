import os
import requests

GITHUB_BASE = "https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend"
REFS_PATH = "refs/heads"

def download_template(folder_name, version, dest_dir):
    files = [
        "gradle/wrapper/gradle-wrapper.jar",
        "gradle/wrapper/gradle-wrapper.properties",
        "WPILib-License.md",
        "build.gradle",
        "settings.gradle"
    ]

    for file_path in files:
        url = f"{GITHUB_BASE}/{REFS_PATH}/{version}/templates/{folder_name}/{file_path}"
        dest_path = os.path.join(dest_dir, file_path)

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        print(f"⬇️ Downloading {file_path}...")
        response = requests.get(url)

        if response.status_code == 200:
            with open(dest_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Saved to {dest_path}")
        else:
            print(f"❌ Failed to download {file_path} ({response.status_code})")
