import os.path

from prompts import *
from template_downloader import download_template
from versions_loader import load_versions
from templates_loader import load_templates_from_github
from examples_loader import load_examples_from_github


def main():
    print("🚀 WPILib CLI — Project Creator\n")

    project_name = ask_project_name()
    if not project_name:
        print("⚠️ Project name is required.")
        return

    team_number = ask_team_number()
    print(f"✅ Team {team_number} confirmed.\n")

    team_domain = ask_team_domain()
    print(f"Team domain: {team_domain}\n")

    print("📥 Fetching available WPILib versions...")
    wpilib_version = select_wpilib_version(load_versions())
    print(f"✅ Selected WPILib version: {wpilib_version}\n")

    start_type = select_project_type()
    print(f"📦 Starting with: {start_type}\n")

    if start_type == "Templates":
        print("📥 Loading WPILib templates...")
        templates = load_templates_from_github(wpilib_version)
        selected = select_template(templates)
        print("\n✅ You selected:")
        print(f"👉 \033[1m{selected['name']}\033[0m")
        project_dir = os.path.join(os.getcwd(), project_name)
        download_template(selected['name'], wpilib_version, project_dir)
        print(f"\n🎉 Project created in: {project_dir}")
    elif start_type == "Examples":
        print("📥 Loading WPILib examples...")
        examples = load_examples_from_github()
        selected = select_example(examples)
        print("\n✅ You selected:")
        print(f"👉 \033[1m{selected['name']}\033[0m")


if __name__ == "__main__":
    main()