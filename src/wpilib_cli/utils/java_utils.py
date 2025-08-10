import os


def update_package_path_for_java_files(root_project_dir: str, new_package_path: str, project_name: str) -> None:
    """
    Updates java package declaration in all java files
    :param root_project_dir: Root directory in order to search for java files
    :param new_package_path: New java package path to replace the old one
    :param project_name: Name of the project
    :return: None
    """
    for folder, _, files in os.walk(root_project_dir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(folder, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    contents = f.read()

                new_contents = contents.replace(
                    "package frc.robot;", f"package {new_package_path}.{project_name};"
                )

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_contents)

                print(f"✅ Updated package path in {file_path} to {new_package_path}.{project_name}")


def update_robot_main_class(root_project_dir: str, team_domain: str, project_name: str) -> None:
    """
    Updates the ``ROBOT_MAIN_CLASS`` variable in the ``build.gradle`` file to match the new package structure
    :param root_project_dir: The root directory of the project where the ``build.gradle`` file is located
    :param team_domain: The team domain in reverse order, e.g. "mckinleyfirebirds.com" becomes "com.mckinleyfirebirds"
    :param project_name: The name of the project
    :return: None
    """
    package_parts = team_domain.lower().split(".")[::-1]
    package_parts.append(project_name)
    package_path = ".".join(package_parts)

    gradle_file_path = os.path.join(root_project_dir, "build.gradle")
    if not os.path.exists(gradle_file_path):
        print(f"⚠️ build.gradle not found at {gradle_file_path}")
        return

    with open(gradle_file_path, "r", encoding="utf-8") as file:
        contents = file.read()

    updated_contents = contents.replace(
        'def ROBOT_MAIN_CLASS = "frc.robot.Main"',
        f'def ROBOT_MAIN_CLASS = "{package_path}.Main"'
    )

    with open(gradle_file_path, "w", encoding="utf-8") as file:
        file.write(updated_contents)

    print(f"✅ Updated ROBOT_MAIN_CLASS to {package_path}.Main\n")