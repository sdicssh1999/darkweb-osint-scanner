import os
from rich.console import Console
from rich.text import Text

TOOL_ENTRY_POINTS = {
    "Katana": None,
    "OnionSearch": "main.py",
    "darkdump": "main.py",
    "ahmia-site": None,
    "Darkus": None,
    "onionscan": None,
    "Onioff": None,
    "docker-onion-nmap": None,
    "TorBot": "main.py",
    "TorCrawl.py": None,
    "VigilantOnion": None,
    "OnionIngestor": None,
    "Darc": "demo/deploy/market/run.py",
    "midnight_sea": "workspaces/scraper/src/scraper/main.py",
    "pryingdeep": None,
    "deepdarkCTI": None
}

def print_banner():
    os.system("clear")
    console = Console()

    ascii_banner = r"""
__        __   _                            _   ____   ____   ____  
\ \      / /__| | ___ ___  _ __ ___   ___  | | |___ \ |___ \ |___ \ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |   __) |  __) |  __) |
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | |  / __/  / __/  / __/ 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_| |_____| |_____| |____|
"""
    console.print(ascii_banner, style="bold magenta")
    console.print("      🌑 World of Dark Side OSINT Toolkit", style="bold cyan")
    console.print("           Author: @Sumandas\n", style="dim white")

def list_available_tools():
    return [tool for tool in TOOL_ENTRY_POINTS]

