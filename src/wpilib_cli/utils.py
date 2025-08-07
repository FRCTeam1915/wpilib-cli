import os


def reverse_domain(domain, team_number):
    if domain and domain.strip():
        parts = domain.lower().strip().split(".")
        return ".".join(reversed(parts))
    return f"org.team{team_number}.frc"

def domain_to_path(domain, team_number):
    if domain and domain.strip():
        parts = domain.lower().strip().split(".")
        return os.path.join(*reversed(parts)) # TODO: handle parameters unfilled
    return os.path.join("org", f"team{team_number}", "frc")


def create_package_dirs(base_dir, domain, team_number, project_name):
    package_path = domain_to_path(domain, team_number)
    full_path = os.path.join(base_dir, "src", "main", "java", package_path, project_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"📁 Created package directory: {full_path}")
    return full_path

def update_robot_main_class(root_project_dir, team_domain, project_name):
    package_parts = team_domain.lower().split(".")[::-1]
    package_parts.append(project_name)
    package_path = ".".join(package_parts)  # Java package style

    gradle_file_path = os.path.join(root_project_dir, "build.gradle")
    if not os.path.exists(gradle_file_path):
        print(f"⚠️ build.gradle not found at {gradle_file_path}")
        return

    with open(gradle_file_path, "r") as file:
        contents = file.read()

    updated_contents = contents.replace(
        'def ROBOT_MAIN_CLASS = "frc.robot.Main"',
        f'def ROBOT_MAIN_CLASS = "{package_path}.Main"'
    )

    with open(gradle_file_path, "w") as file:
        file.write(updated_contents)

    print(f"✅ Updated ROBOT_MAIN_CLASS to {package_path}.Main")

def update_wpilib_preferences(project_dir, team_number):
    prefs_path = os.path.join(project_dir, ".wpilib", "wpilib_preferences.json")

    with open(prefs_path, "r", encoding="utf-8") as f:
        prefs = json.load(f)

    # Set the team number
    prefs["teamNumber"] = int(team_number)

    with open(prefs_path, "w", encoding="utf-8") as f:
        json.dump(prefs, f, indent=4)

    print(f"✅ Team number updated to {team_number} in wpilib_preferences.json")