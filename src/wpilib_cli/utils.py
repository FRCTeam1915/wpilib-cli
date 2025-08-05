import os

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