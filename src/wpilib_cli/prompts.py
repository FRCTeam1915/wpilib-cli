import questionary


def ask_project_name():
    """Prompts the user for a project name"""
    return questionary.text(
        "📛 Enter your project name:"
    ).ask()


def ask_team_number():
    """Prompts the user for their FRC team number"""
    while True:
        team_num = questionary.text("Enter your FRC Team Number:").ask()

        if not team_num or not team_num.isdigit():
            print("❌ Please enter a valid numeric team number.")
            continue

        confirm = questionary.confirm(f"Is {team_num} correct?").ask()
        if confirm:
            return team_num


def ask_team_domain(team_number):
    """Prompts the user for their team domain, with a default based on the team number"""
    has_domain = questionary.confirm("🌐 Does your team have a domain?", default=False).ask()

    if has_domain:
        domain = questionary.text("🔤 Enter your team domain (e.g., mckinleyfirebirds.com):").ask()
        return domain.strip()
    else:
        return f"frc.team{team_number}.org"


def select_wpilib_version(versions):
    """Prompts the user to select a WPILib version"""
    return questionary.select(
        "🔧 Select WPILib version:",
        choices=versions
    ).ask()


def select_project_type():
    """Prompts the user to select the type of project to start with"""
    return questionary.select(
        "📁 What type of project would you like to start with?",
        choices=[
            "Templates",
            "Examples"
        ]
    ).ask()


def select_template(templates):
    """Prompts the user to select a project template"""
    choices = [
        questionary.Choice(
            title=f"{template['name']}",
            value=template
        )
        for template in templates
    ]


    return questionary.select(
        "📦 Select a project template:",
        choices=choices
    ).ask()


def select_example(examples):
    """Prompts the user to select a project example"""
    choices = [
        questionary.Choice(
            title=f"{example['name']}",
            value=example
        ) for example in examples
    ]

    return questionary.select(
        "📦 Select a project example: (Use arrow keys to select | Press enter to confirm)",
        choices=choices
    ).ask()


def ask_programming_language():
    """Prompts the user to select a programming language for the project"""
    return questionary.select(
        "💻 What programming language would you like to use?",
        choices=[
            "Java",
            "C++",
            "Python",
        ]
    ).ask()


def select_extensions(extensions):
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
