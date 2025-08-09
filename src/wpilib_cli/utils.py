import json
import os
import platform
import subprocess
from pathlib import Path


def reverse_domain(domain, team_number):
    """Reverses the domain for Java package declaration"""
    if domain and domain.strip():
        parts = domain.lower().strip().split(".")
        return ".".join(reversed(parts))
    return f"org.team{team_number}.frc"

def domain_to_path(domain, team_number):
    """Converts a domain to a file path for Java package structure"""
    if domain and domain.strip():
        parts = domain.lower().strip().split(".")
        return os.path.join(*reversed(parts)) # TODO: handle parameters unfilled
    return os.path.join("org", f"team{team_number}", "frc")

def create_package_dirs(base_dir, domain, team_number, project_name):
    """Creates the package directories for a Java project based on the team domain and number"""
    package_path = domain_to_path(domain, team_number)
    full_path = os.path.join(base_dir, "src", "main", "java", package_path, project_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"📁 Created package directory: {full_path}")
    return full_path

def update_robot_main_class(root_project_dir, team_domain, project_name):
    """Updates the ROBOT_MAIN_CLASS in build.gradle to match the Java package structure"""
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

    print(f"✅ Updated ROBOT_MAIN_CLASS to {package_path}.Main\n")

def update_wpilib_preferences(project_dir, team_number):
    """Updates the wpilib_preferences.json file with the team number"""
    prefs_path = os.path.join(project_dir, ".wpilib", "wpilib_preferences.json")

    with open(prefs_path, "r", encoding="utf-8") as f:
        prefs = json.load(f)

    # Set the team number
    prefs["teamNumber"] = int(team_number)

    with open(prefs_path, "w", encoding="utf-8") as f:
        json.dump(prefs, f, indent=4)

    print(f"✅ Team number updated to {team_number} in wpilib_preferences.json\n")


def make_gradlew_executable(project_dir):
    gradlew_path = Path(project_dir) / "gradlew"
    system = platform.system()

    if not gradlew_path.exists():
        print(f"❌ gradlew not found in {project_dir}")
        return False

    try:
        if system in ["Linux", "Darwin"]:  # macOS and Linux
            subprocess.run(["chmod", "+x", str(gradlew_path)], check=True)
        print(f"✅ gradlew is executable for {system}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to set gradlew as executable on {system}")
        return False


def run_gradle_command(project_dir, args):
    system = platform.system()
    gradle_cmd = ["./gradlew"] if system in ["Linux", "Darwin"] else ["gradlew.bat"]

    try:
        subprocess.run(gradle_cmd + args, cwd=Path(project_dir), check=True)
    except subprocess.CalledProcessError:
        print(f"❌ Gradle command failed: {' '.join(args)}")
