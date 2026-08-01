from rich.console import Console
from rich.panel import Panel

console = Console()

BANNER = r"""
[bold red]
 ██╗     ███████╗██████╗ ███╗   ██╗ █████╗ ███████╗ █████╗ ███╗   ██╗
 ██║     ██╔════╝██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔══██╗████╗  ██║
 ██║     █████╗  ██████╔╝██╔██╗ ██║███████║█████╗  ███████║██╔██╗ ██║
 ██║     ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██╔══╝  ██╔══██║██║╚██╗██║
 ███████╗███████╗██║  ██║██║ ╚████║██║  ██║███████╗██║  ██║██║ ╚████║
 ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
[/bold red]
[dim red]         Cut one head, two more shall take its place.[/dim red]
"""

def show():
    console.print(BANNER)
    console.print(Panel.fit("[bold cyan]Autonomous Offensive AI Agent[/bold cyan]", border_style="red"))
