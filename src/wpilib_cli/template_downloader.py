import os
import requests

GITHUB_BASE = "https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend"
REFS_PATH = "refs/heads"

# TODO: This function is too long and should be refactored into smaller functions
def download_template(folder_name, version, dest_dir, package_path):
    print("📄 Downloading manifest.json...")

    manifest_url = f"{GITHUB_BASE}/{REFS_PATH}/{version}/templates/{folder_name}/manifest.json"
    manifest_response = requests.get(manifest_url)

    if manifest_response.status_code != 200:
        print(f"❌ Failed to fetch manifest.json for {folder_name}")
        return

    manifest = manifest_response.json()
    build_files = manifest.get("build_files", [])
    code_files = manifest.get("code_files", [])

    # --- Download build files to the root project directory ---
    for file_path in build_files:
        url = f"{GITHUB_BASE}/{REFS_PATH}/{version}/templates/{folder_name}/{file_path}"
        local_path = os.path.join(dest_dir, file_path)

        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        print(f"⬇️ Downloading {file_path}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Saved to {local_path}")
        else:
            print(f"❌ Failed to download {file_path} ({response.status_code})")

    # --- Download code files into src/main/java/{package_path} ---
    code_dir = os.path.join(dest_dir, "src", "main", "java", package_path)

    for code_file in code_files:
        url = f"{GITHUB_BASE}/{REFS_PATH}/{version}/templates/{folder_name}/{code_file}"
        local_path = os.path.join(code_dir, code_file)

        print(f"⬇️ Downloading {code_file} to {local_path}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Saved Java file to {local_path}")
        else:
            print(f"❌ Failed to download {code_file} ({response.status_code})")