from typing import Optional, List, Dict

import questionary


def ask_project_name() -> str:
    """
    Prompts the user for a project name
    :return: The project name provided by the user
    """
    while True:
        project_name = questionary.text("📛 Enter your project name:").ask()
        if project_name and project_name.strip():
            return project_name.strip()
        print("❌ Project name cannot be empty. Please enter a valid name.")


def ask_team_number() -> str:
    """
    Prompts the user for their FRC team number
    :return: The team number provided by the user
    """
    while True:
        team_num = questionary.text("Enter your FRC Team Number:").ask()
        if not team_num or not team_num.isdigit():
            print("❌ Please enter a valid numeric team number.")
            continue

        confirm = questionary.confirm(f"Is {team_num} correct?").ask()
        if confirm:
            return team_num


def ask_team_domain(team_number: str) -> str:
    """
    Prompts the user for their team domain
    :param team_number: The FRC team number
    :return: The team domain or a default domain if none is provided
    """
    has_domain = questionary.confirm("🌐 Does your team have a domain?", default=False).ask()
    if has_domain:
        domain = questionary.text("🔤 Enter your team domain (e.g., mckinleyfirebirds.com):").ask()
        if domain:
            return domain.strip()
    # The default domain
    return f"frc.team{team_number}.org"


def select_wpilib_version(available_versions: List[str]) -> Optional[str]:
    """
    Prompts the user to select a WPILib version from a list of available versions
    :param available_versions:
    :return: The selected WPILib version
    """
    return questionary.select(
        "🔧 Select WPILib version:",
        choices=available_versions
    ).ask()


def ask_programming_language() -> Optional[str]:
    """
    Prompts the user to select a programming language for their project
    :return: The programming language selected by the user
    """
    return questionary.select(
        "💻 What programming language would you like to use?",
        choices=[
            "Java",
            # "C++",
            # "Python",
        ],
    ).ask()


def select_project_type() -> Optional[str]:
    """
    Prompts the user to choose either a template or an example
    :return: The selected project type
    """
    return questionary.select(
        "📂 What type of project would you like to start with?",
        choices=[
            "Templates",
            "Examples"
        ],
    ).ask()


def select_template(templates: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    """
    Prompts the user to select a project template from a list of available templates
    :param templates: The list of available templates
    :return: The Project template selected by the user
    """
    choices = [
        questionary.Choice(
            title=template['name'],
            value=template
        )
        for template in templates
    ]

    return questionary.select(
        "📦 Select a project template:",
        choices=choices
    ).ask()


def select_extensions(extensions: List[Dict[str, str]]) -> Optional[List[str]]:
    """
    Prompts the user to select vendor extensions to add to their project
    :param extensions: The list of available vendor extensions
    :return: A list of selected json urls
    """
    choices = [
        questionary.Choice(
            title=f"{ext['name']} – {ext['description']}",
            value=ext['json_url']
        )
        for ext in extensions
    ]

    return questionary.checkbox(
        "Select the vendor extensions you want to add to your project:",
        choices=choices
    ).ask()
