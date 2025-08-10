import argparse

from wpilib_cli.commands.create import run_create_command


def run_cli() -> None:
    """Run the WPILib CLI project creator."""
    run_create_command()

def main() -> None:
    """Entry point for the WPILib CLI application."""
    parser = argparse.ArgumentParser(
        prog="wpilib-cli",
        description="WPILib CLI - Command Line Interface for creating FRC projects with WPILib templates and examples."
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="WPILib CLI v1.0.0beta",
        help="Show the version of the WPILib CLI"
    )

    parser.add_argument(
        "-c", "--create",
        action="store_true",
        help="Create a new WPILib project"
    )

    args = parser.parse_args()

    if args.create:
        run_cli()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
