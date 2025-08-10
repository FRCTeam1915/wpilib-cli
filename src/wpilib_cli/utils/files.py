import os.path
from typing import Optional


def reverse_domain(domain: Optional[str], team_num: str) -> str:
    """
    Reverses the domain for java package declaration
    :param domain: The team domain e.g. "mckinleyfirebirds.com" or None
    :param team_num: The team number
    :return: Reversed domain string e.g. "com.mckinleyfirebirds"
    """
    if domain and domain.strip():
        parts = domain.lower().strip().split(".")
        return ".".join(reversed(parts))
    return f"org.team{team_num}.frc"


def convert_domain_to_path(domain: Optional[str], team_num: str) -> str:
    """
    Converts a domain string into a path for java packages
    :param domain: The team domain e.g. "mckinleyfirebirds.com" or None
    :param team_num: The team number
    :return: Path in string
    """
    if domain and domain.strip():
        parts = domain.lower().strip().split(".")
        # We could do cast() to make this shut up but whatever - Hao
        return os.path.join(*reversed(parts))
    return os.path.join("org", f"team{team_num}", "frc")


def create_package_dirs(base_dir: str, domain: Optional[str], team_num: str, project_name: str) -> str:
    """
    Creates the package directory structure for a java project
    :param base_dir: The base directory where the project will be created
    :param domain: The team domain e.g. "mckinleyfirebirds.com" or None
    :param team_num: The team number
    :param project_name: The name of the project
    :return: The full path to the created package directory
    """
    package_path = convert_domain_to_path(domain, team_num)
    full_path = os.path.join(base_dir, "src", "main", "java", package_path, project_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"📁 Created package directory: {full_path}")
    return full_path
