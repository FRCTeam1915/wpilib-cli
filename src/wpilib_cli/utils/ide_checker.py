import os.path
import platform
import shutil
from pathlib import Path
from typing import List


def is_vscode_installed() -> bool:
    """
    Checks if Visual Studio Code is installed on the system
    :return: True if VS Code is installed, False otherwise
    """
    if shutil.which("code"):
        return True

    # Alternative checks for VS Code installation
    system = platform.system()

    paths: List[str] = []
    if system == "Windows":
        paths = [
            os.path.expandvars(r"%LocalAppData%\Programs\Microsoft VS Code\Code.exe"),
            r"C:\Program Files\Microsoft VS Code\Code.exe",
        ]
    elif system == "Darwin":
        paths = ["/Applications/Visual Studio Code.app"]
    else:
        paths = [
            "/usr/bin/code",
            "/usr/share/code",
            "/snap/bin/code",
        ]

    return any(Path(path).exists() for path in paths)


def is_intellij_installed() -> bool:
    """
    Checks if IntelliJ IDEA is installed on the system
    :return: True if IntelliJ IDEA is installed, False otherwise
    """
    if shutil.which("idea"):
        return True

    system = platform.system()

    possible_paths: List[Path] = []
    if system == "Windows":
        toolbox_dir = Path(os.path.expandvars(r"%LocalAppData%\Programs\JetBrains Toolbox\apps\IDEA-U\ch-0"))
        if toolbox_dir.exists():
            for child in toolbox_dir.iterdir():
                exe = child / "bin" / "idea64.exe"
                if exe.exists():
                    return True

        jetbrains_dir = Path(r"C:\Program Files\JetBrains")
        if jetbrains_dir.exists():
            for child in jetbrains_dir.iterdir():
                if child.is_dir() and child.name.startswith("IntelliJ IDEA"):
                    exe = child / "bin" / "idea64.exe"
                    if exe.exists():
                        return True

    elif system == "Darwin":
        possible_paths = [
            Path("/Applications/IntelliJ IDEA.app"),
            Path(os.path.expanduser("~/Applications/JetBrains Toolbox/IntelliJ IDEA.app")),
        ]
    else:
        possible_paths = [
            Path("/usr/share/intellij-idea/bin/idea.sh"),
            Path("/opt/intellij-idea/bin/idea.sh"),
            Path(os.path.expanduser("~/jetbrains/idea/bin/idea.sh")),
        ]

    return any(path.exists() for path in possible_paths)


# You are a loser if you use Eclipse - Hao
def is_eclipse_installed() -> bool:
    """
    Checks if Eclipse is installed on the system
    :return: True if Eclipse is installed, False otherwise
    """
    system = platform.system()

    if system == "Windows":
        possible_paths = [
            Path(r"C:\Program Files\Eclipse\eclipse.exe"),
            Path(r"C:\Program Files (x86)\Eclipse\eclipse.exe"),
        ]
        return any(path.exists() for path in possible_paths)

    elif system == "Darwin":
        possible_paths = [
            Path("/Applications/Eclipse.app"),
            Path.home() / "Applications/Eclipse.app",
        ]
        return any(path.exists() for path in possible_paths)

    else:
        possible_paths = [
            Path("/usr/bin/eclipse"),
            Path("/usr/local/bin/eclipse"),
            Path("/opt/eclipse/eclipse"),
        ]
        return any(path.exists() for path in possible_paths)


def is_vim_installed() -> bool:
    """
    Checks if Vim is installed on the system
    :return: True if Vim is installed, False otherwise
    """
    return shutil.which("vim") is not None


def is_neovim_installed() -> bool:
    """
    Checks if Neovim is installed on the system
    :return: True if Neovim is installed, False otherwise
    """
    return shutil.which("nvim") is not None


def is_emacs_installed() -> bool:
    """
    Checks if Emacs is installed on the system
    :return: True if Emacs is installed, False otherwise
    """
    return shutil.which("emacs") is not None
