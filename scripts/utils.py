import os

TOOL_ENTRY_POINTS = {
    "darkdump": "main.py",
    "OnionSearch": "main.py",
    "katana": None,
    "Darc": "demo/deploy/market/run.py",
    "DeepDarkCTI": None,
    "Darkus": None,
    "MidnightSea": "workspaces/scraper/src/scraper/main.py",
    "Onioff": None,
    "OnionIngestor": None,
    "PryingDeep": None,
    "TorBot": "main.py",
    "TorCrawl": None,
    "VigilantOnion": None,
    "onionscan": None,
    "ahmia-site": None
}

def print_banner():
    os.system("clear")
    banner = r"""
      __        __         _                                      _   _             _ 
      \ \      / /__  _ __| | _____   _____ _ __ ___   ___ _ __ | |_| |_   _  __ _| |
       \ \ /\ / / _ \| '__| |/ _ \ \ / / _ \ '_ ` _ \ / _ \ '_ \| __| | | | |/ _` | |
        \ V  V / (_) | |  | | (_) \ V /  __/ | | | | |  __/ | | | |_| | |_| | (_| | |
         \_/\_/ \___/|_|  |_|\___/ \_/ \___|_| |_| |_|\___|_| |_|\__|_|\__,_|\__,_|_|
                             Welcometothedarkworld
                              Author: @Sumandas
    """
    print(banner)

def list_available_tools():
    return [tool for tool in TOOL_ENTRY_POINTS]

