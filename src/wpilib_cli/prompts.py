import questionary

def ask_project_name():
    return questionary.text(
        "📛 Enter your project name:"
    ).ask()

def ask_team_number():
    while True:
        team_num = questionary.text("Enter your FRC Team Number:").ask()

        if not team_num or not team_num.isdigit():
            print("❌ Please enter a valid numeric team number.")
            continue

        confirm = questionary.confirm(f"Is {team_num} correct?").ask()
        if confirm:
            return team_num

def ask_team_domain(team_number):
    has_domain = questionary.confirm("🌐 Does your team have a domain?", default=False).ask()

    if has_domain:
        domain = questionary.text("🔤 Enter your team domain (e.g., mckinleyfirebirds.com):").ask()
        return domain.strip()
    else:
        return f"frc.team{team_number}.org"

def select_wpilib_version(versions):
    return questionary.select(
        "🔧 Select WPILib version:",
        choices=versions
    ).ask()

def select_project_type():
    return questionary.select(
        "📁 What type of project would you like to start with?",
        choices=[
            "Templates",
            "Examples"
        ]
    ).ask()

def select_template(templates):
    choices = [
        questionary.Choice(
            title=f"{template['name']} | {template['description']}",
            value=template
        )
        for template in templates
    ]

    return questionary.select(
        "📦 Select a project template:",
        choices=choices
    ).ask()

def select_example(examples):
    choices = [
        questionary.Choice(
            title=f"{example['name']} | {example['description']}",
            value=example
        ) for example in examples
    ]

    return questionary.select(
        "📦 Select a project example: (Use arrow keys)",
        choices=choices
    ).ask()