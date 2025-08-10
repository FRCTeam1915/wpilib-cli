import platform
import subprocess
from pathlib import Path


def make_gradlew_executable(project_dir: str) -> bool:
    """
    Ensure that ``gradlew`` is executable
    :param project_dir: The directory where gradlew is located
    :return: True if gradlew is executable, False otherwise
    """
    gradlew_path = Path(project_dir) / "gradlew"
    system = platform.system()

    if not gradlew_path.exists():
        print(f"❌ gradlew not found in {project_dir}")
        return False

    try:
        if system in ["Linux", "Darwin"]:
            subprocess.run(["chmod", "+x", str(gradlew_path)], check=True)
        print(f"✅ gradlew is executable for {system}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to set gradlew as executable on {system}")
        return False


def run_gradle_command(project_dir: str, args: list[str]) -> None:
    """
    Runs a Gradle command in the specified project directory
    :param project_dir: The directory where gradlew is located
    :param args: The command
    :return: None
    """
    system = platform.system()
    gradle_cmd = ["./gradlew"] if system in ["Linux", "Darwin"] else ["gradlew.bat"]

    try:
        subprocess.run(gradle_cmd + args, cwd=Path(project_dir), check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to execute {' '.join(gradle_cmd + args)}: {e}")
