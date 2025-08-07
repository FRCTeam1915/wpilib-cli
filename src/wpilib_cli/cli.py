import argparse
import os

from wpilib_cli.package_path_rewriter import update_package_path_for_java_files
from wpilib_cli.prompts import *
from wpilib_cli.utils import domain_to_path, create_package_dirs, update_robot_main_class, reverse_domain, \
    update_wpilib_preferences
from wpilib_cli.template_downloader import download_template
from wpilib_cli.versions_loader import load_versions
from wpilib_cli.templates_loader import load_templates_from_github
from wpilib_cli.examples_loader import load_examples_from_github


def run_cli():
    print("🚀 WPILib CLI — Project Creator\n")

    project_name = ask_project_name()
    if not project_name:
        print("⚠️ Project name is required.")
        return

    team_num = ask_team_number()
    print(f"✅ Team {team_num} confirmed.\n")

    team_domain = ask_team_domain(team_num)
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
        create_package_dirs(project_dir, team_domain, team_num, project_name)
        download_template(selected['foldername'], wpilib_version, project_dir, os.path.join(domain_to_path(team_domain, team_num), project_name))
        print(f"\n🎉 Project created in: {project_dir}\n")

        print("🛠️ Rewriting WPILib preferences...\n")
        update_wpilib_preferences(project_dir, team_num)
        print("🛠️ Rewriting robot main class...\n")
        update_robot_main_class(project_dir, team_domain, project_name)
        print("🛠️ Rewriting Java package declarations...\n")
        update_package_path_for_java_files(os.path.join(project_dir, "src", "main", "java"), reverse_domain(team_domain, team_num), project_name)
    elif start_type == "Examples":
        print("📥 Loading WPILib examples...")
        examples = load_examples_from_github()
        selected = select_example(examples)
        print("\n✅ You selected:")
        print(f"👉 \033[1m{selected['name']}\033[0m")

def main():
    parser = argparse.ArgumentParser(
        prog="wpilib-cli",
        description="WPILib CLI - Command Line Interface for creating FRC projects with WPILib templates and examples."
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="WPILib CLI v1.0.0beta",
        help="Show the version of the WPILib CLI"
    )

    parser.add_argument(
        "-c", "--create",
        action="store_true",
        help="Create a new WPILib project"
    )

    args = parser.parse_args()

    if args.create:
        run_cli()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()