#!/usr/bin/env python3
from rich.console import Console
from rich.prompt import Prompt
from core import banner, providers
from core.agent import agent_loop

console = Console()

def main():
    banner.show()
    provider = providers.choose_provider()
    if not provider: return
    api_key = providers.get_api_key(provider["name"])
    console.print("[yellow][*] Fetching available models...[/yellow]")
    models = providers.fetch_models(provider, api_key)
    if not models:
        console.print("[red][!] No models found. Check your key.[/red]")
        return
    model = providers.choose_model(models)
    console.print(f"[bold green][+] Using {model} via {provider['name']}[/bold green]\n")

    while True:
        try:
            obj = Prompt.ask("[bold red]lernaean[/bold red]")
            if obj.lower() in ("exit","quit"): break
            agent_loop(provider, api_key, model, obj)
        except KeyboardInterrupt:
            console.print("\n[dim]Ctrl+C — bye.[/dim]"); break

if __name__ == "__main__":
    main()
