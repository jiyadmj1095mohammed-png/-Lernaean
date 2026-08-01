import requests
from rich.console import Console
from rich.prompt import Prompt

console = Console()

PROVIDERS = {
    "1": {"name": "OpenAI", "endpoint": "https://api.openai.com/v1/models", "auth": "Bearer"},
    "2": {"name": "Anthropic Claude", "endpoint": "https://api.anthropic.com/v1/models", "auth": "x-api-key"},
    "3": {"name": "Google AI Studio (Gemini)", "endpoint": "https://generativelanguage.googleapis.com/v1beta/models", "auth": "query"},
    "4": {"name": "OpenRouter", "endpoint": "https://openrouter.ai/api/v1/models", "auth": "Bearer"},
    "5": {"name": "Groq", "endpoint": "https://api.groq.com/openai/v1/models", "auth": "Bearer"},
    "6": {"name": "DeepSeek", "endpoint": "https://api.deepseek.com/v1/models", "auth": "Bearer"},
    "7": {"name": "Mistral", "endpoint": "https://api.mistral.ai/v1/models", "auth": "Bearer"},
    "8": {"name": "xAI Grok", "endpoint": "https://api.x.ai/v1/models", "auth": "Bearer"},
}

def choose_provider():
    console.print("\n[bold cyan]Available Providers:[/bold cyan]")
    for k, v in PROVIDERS.items():
        console.print(f"  [{k}] {v['name']}")
    choice = Prompt.ask("[red]lernaean[/red] > select provider")
    return PROVIDERS.get(choice)

def get_api_key(provider_name):
    return Prompt.ask(f"[red]lernaean[/red] > paste {provider_name} API key", password=True)

def fetch_models(provider, api_key):
    """Query the provider for the actual list of models available on that key."""
    headers = {}
    url = provider["endpoint"]

    if provider["auth"] == "Bearer":
        headers["Authorization"] = f"Bearer {api_key}"
    elif provider["auth"] == "x-api-key":
        headers["x-api-key"] = api_key
        headers["anthropic-version"] = "2023-06-01"
    elif provider["auth"] == "query":
        url = f"{url}?key={api_key}"

    try:
        r = requests.get(url, headers=headers, timeout=15)
        data = r.json()
        # normalize model IDs across providers
        if "data" in data:
            return [m["id"] for m in data["data"]]
        if "models" in data:
            return [m["name"].split("/")[-1] for m in data["models"]]
        return []
    except Exception as e:
        console.print(f"[red][!] Error fetching models: {e}[/red]")
        return []

def choose_model(models):
    console.print("\n[bold cyan]Models available on your key:[/bold cyan]")
    for i, m in enumerate(models, 1):
        console.print(f"  [{i}] {m}")
    idx = int(Prompt.ask("[red]lernaean[/red] > select model number")) - 1
    return models[idx]
