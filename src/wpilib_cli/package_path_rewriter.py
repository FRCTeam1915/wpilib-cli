import os


def update_package_path_for_java_files(root_project_dir, new_package_path, project_name):
    for folder, _, files in os.walk(root_project_dir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(folder, file)
                with open(file_path, "r") as f:
                    contents = f.read()

                # Replace the package declaration
                new_contents = contents.replace("package frc.robot;", f"package {new_package_path}.{project_name};")

                with open(file_path, "w") as f:
                    f.write(new_contents)

                print(f"✅ Updated package path in {file_path} to {new_package_path}.{project_name}")