import subprocess, shutil, platform
from rich.console import Console

console = Console()

def has_tool(tool):
    return shutil.which(tool) is not None

def install_tool(tool):
    """Auto-install missing binaries per platform."""
    console.print(f"[yellow][*] Installing missing tool: {tool}[/yellow]")
    sysname = platform.system().lower()
    try:
        if "android" in platform.release().lower() or has_tool("pkg"):
            subprocess.run(["pkg", "install", "-y", tool], check=True)
        elif has_tool("apt"):
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
        elif has_tool("pacman"):
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", tool], check=True)
        elif has_tool("brew"):
            subprocess.run(["brew", "install", tool], check=True)
        elif "windows" in sysname:
            subprocess.run(["winget", "install", tool], check=True)
        return True
    except Exception as e:
        console.print(f"[red][!] Install failed: {e}[/red]")
        return False

def run(cmd):
    """Execute shell command, auto-install if binary missing."""
    binary = cmd.strip().split()[0]
    if not has_tool(binary) and binary not in ("cd", "echo", "ls", "dir"):
        install_tool(binary)

    console.print(f"[dim]$ {cmd}[/dim]")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "[timeout]"
    except Exception as e:
        return f"[error] {e}"
