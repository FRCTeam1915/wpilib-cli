import os

import requests


def download_template_from_github(folder_name: str, version: str, language: str, dest_dir: str, package_path: str) -> None:
    """
    Downloads the template files and saves them to the destination directory
    :param language: The programming language
    :param folder_name: The name of the template folder to download
    :param version: The WPILib version to use
    :param dest_dir: The destination directory where the template files will be saved
    :param package_path: The package path to use for Java files
    :return: None
    """
    manifest_url = (f"https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/{version}/{language}"
                    f"/templates/{folder_name}/manifest.json")
    print("📄 Fetching manifest.json...")

    manifest_res = requests.get(manifest_url)
    if manifest_res.status_code != 200:
        raise requests.HTTPError(
            f"Failed to fetch manifest.json for {folder_name} (status code {manifest_res.status_code})")

    manifest = manifest_res.json()
    build_files = manifest.get("build_files", [])
    code_files = manifest.get("code_files", [])

    # Download build files to the root project directory
    for build_file_path in build_files:
        file_url = (f"https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/{version}/{language}"
                    f"/templates/{folder_name}/{build_file_path}")
        local_path = os.path.join(dest_dir, build_file_path)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        print(f"⬇️ Downloading build file {build_file_path}...")
        response = requests.get(file_url)
        if response.status_code != 200:
            raise requests.HTTPError(f"Failed to download build file {build_file_path} (status code {response.status_code})")

        with open(local_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved build file to {local_path}")

    # Download code files into src/main/java/{package_path}
    code_dir = os.path.join(dest_dir, "src", "main", "java", package_path)
    os.makedirs(code_dir, exist_ok=True)

    for code_file_path in code_files:
        file_url = (f"https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/{version}/{language}"
                    f"/templates/{folder_name}/{code_file_path}")
        local_path = os.path.join(code_dir, code_file_path)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        print(f"⬇️ Downloading code file {code_file_path}...")
        response = requests.get(file_url)
        if response.status_code != 200:
            raise requests.HTTPError(f"Failed to download code file {code_file_path} (status code {response.status_code})")

        with open(local_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved code file to {local_path}")
