import os.path

from wpilib_cli.downloaders.template_downloader import download_template_from_github
from wpilib_cli.loaders.extensions_loader import fetch_extensions_from_github, add_extension_to_project
from wpilib_cli.loaders.templates_loader import fetch_templates_from_github
from wpilib_cli.loaders.versions_loader import fetch_wpilib_versions_from_github
from wpilib_cli.prompts.project_prompts import ask_project_name, ask_team_number, select_wpilib_version, \
    ask_programming_language, select_project_type, select_template, select_extensions, ask_team_domain
from wpilib_cli.utils.files import convert_domain_to_path, create_package_dirs, reverse_domain
from wpilib_cli.utils.gradle import make_gradlew_executable, run_gradle_command
from wpilib_cli.utils.java_utils import update_robot_main_class, update_package_path_for_java_files
from wpilib_cli.utils.preferences import update_wpilib_preferences


def run_create_command() -> None:
    """
    Runs the WPILib CLI project creator command
    """
    print("🚀 WPILib CLI — Project Creator\n")

    project_name = ask_project_name()

    team_num = ask_team_number()

    team_domain = ask_team_domain(team_num)
    print(f"Set team domain to \"{team_domain}\"\n")

    print("📥 Fetching available WPILib versions...")
    wpilib_version = select_wpilib_version(fetch_wpilib_versions_from_github())

    # TODO: Add support for Python & C++
    programming_language = ask_programming_language()

    start_type = select_project_type()
    print(f"📦 Starting with: {start_type}\n")

    if start_type == "Templates":
        _create_project_from_template(project_name, team_num, team_domain, wpilib_version)
    else:
        print("Currently only 'Templates' project creation is implemented.")


def _create_project_from_template(project_name: str, team_num: str, team_domain: str, wpilib_version: str) -> None:
    """
    Creates a WPILib project from a template
    :param project_name: The name of the project to create
    :param team_num: The team number
    :param team_domain: The team domain
    :param wpilib_version: The WPILib version to use
    :return: None
    """
    print("📥 Loading WPILib templates...")
    selected_template = select_template(fetch_templates_from_github(wpilib_version))

    print("\n✅ You selected:")
    print(f"👉 \033[1m{selected_template['name']}\033[0m")

    selected_extensions: list[str] = select_extensions(fetch_extensions_from_github())

    project_dir = os.path.join(os.getcwd(), project_name)

    package_path = os.path.join(convert_domain_to_path(team_domain, team_num), project_name)

    create_package_dirs(project_dir, team_domain, team_num, project_name)

    download_template_from_github(selected_template["foldername"], wpilib_version, project_dir, package_path)
    print(f"\n🎉 Project created in: {project_dir}\n")

    print("🛠️ Rewriting WPILib preferences...")
    update_wpilib_preferences(project_dir, team_num)

    print("🛠️ Rewriting robot main class...")
    update_robot_main_class(project_dir, team_domain, project_name)

    print("🛠️ Rewriting Java package declarations...")
    update_package_path_for_java_files(
        os.path.join(project_dir, "src", "main", "java"),
        reverse_domain(team_domain, team_num),
        project_name,
    )

    print("🛠️ Making gradlew executable...")
    make_gradlew_executable(project_dir)

    for ext_url in selected_extensions:
        print(f"🔌 Adding extension to the project: {ext_url}")
        add_extension_to_project(project_dir, ext_url)

        # FIXME: Workaround for Phoenix 5 & 6
        run_gradle_command(project_dir, ["build"])

    print("\n🏗 Running gradlew build...")
    run_gradle_command(project_dir, ["build"])
