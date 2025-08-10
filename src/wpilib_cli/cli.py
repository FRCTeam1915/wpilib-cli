import argparse
import os

from wpilib_cli.extensions_loader import fetch_extensions, add_extension
from wpilib_cli.package_path_rewriter import update_package_path_for_java_files
from wpilib_cli.prompts import *
from wpilib_cli.utils import domain_to_path, create_package_dirs, update_robot_main_class, reverse_domain, \
    update_wpilib_preferences, run_gradle_command, make_gradlew_executable
from wpilib_cli.template_downloader import download_template
from wpilib_cli.versions_loader import load_versions
from wpilib_cli.templates_loader import load_templates_from_github
from wpilib_cli.examples_loader import fetch_examples_from_github


def run_cli():
    """Runs the WPILib CLI for creating a new project"""
    print("🚀 WPILib CLI — Project Creator\n")

    project_name = ask_project_name()
    if not project_name:
        print("⚠️ Project name is required.")
        return

    team_num = ask_team_number()

    team_domain = ask_team_domain(team_num)
    print(f"Set team domain to \"{team_domain}\"\n")

    print("📥 Fetching available WPILib versions...")
    wpilib_version = select_wpilib_version(load_versions())

    # TODO: Add support for other languages
    programming_language = ask_programming_language()


    start_type = select_project_type()
    print(f"📦 Starting with: {start_type}\n")

    if start_type == "Templates":
        print("📥 Loading WPILib templates...")
        templates = load_templates_from_github(wpilib_version)
        selected = select_template(templates)
        print("\n✅ You selected:")
        print(f"👉 \033[1m{selected['name']}\033[0m")

        selected_extensions = select_extensions(fetch_extensions())

        project_dir = os.path.join(os.getcwd(), project_name)
        create_package_dirs(project_dir, team_domain, team_num, project_name)
        download_template(selected['foldername'], wpilib_version, project_dir, os.path.join(domain_to_path(team_domain, team_num), project_name))
        print(f"\n🎉 Project created in: {project_dir}\n")

        print("🛠️ Rewriting WPILib preferences...")
        update_wpilib_preferences(project_dir, team_num)
        print("🛠️ Rewriting robot main class...")
        update_robot_main_class(project_dir, team_domain, project_name)
        print("🛠️ Rewriting Java package declarations...")
        update_package_path_for_java_files(os.path.join(project_dir, "src", "main", "java"), reverse_domain(team_domain, team_num), project_name)
        print("🛠️ Making gradlew executable...")
        make_gradlew_executable(project_dir)

        for ext_url in selected_extensions:
            print(f"🔌 Adding extension to the project: {ext_url}")
            add_extension(project_dir, ext_url)

            # FIXME: This is a workaround to ensure Phoenix 5 & 6 dont cry because they're stupid
            run_gradle_command(project_dir, ["build"])

        print("\n🏗 Running gradlew build...")
        run_gradle_command(project_dir, ["build"])
    elif start_type == "Examples":
        print("📥 Fetching WPILib examples...")
        examples = fetch_examples_from_github()
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