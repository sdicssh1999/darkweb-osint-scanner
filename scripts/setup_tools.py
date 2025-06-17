import os
import subprocess

TOOLS = {
    "Katana": "https://github.com/0xStrontium/Katana.git",
    "OnionSearch": "https://github.com/megadose/OnionSearch.git",
    "darkdump": "https://github.com/josh0xA/darkdump.git",
    "ahmia-site": "https://github.com/ahmia/ahmia-site.git",
    "Darkus": "https://github.com/Lucksi/Darkus.git",
    "Onioff": "https://github.com/k4m4/onioff.git",
    "docker-onion-nmap": "https://github.com/milesrichardson/docker-onion-nmap.git",
    "TorBot": "https://github.com/DedSecInside/TorBot.git",
    "TorCrawl.py": "https://github.com/MikeMeliz/TorCrawl.py.git",
    "VigilantOnion": "https://github.com/andreyglauzer/VigilantOnion.git"
}

def clone_and_setup_tools(base_dir="tools"):
    os.makedirs(base_dir, exist_ok=True)
    summary = []

    for name, repo in TOOLS.items():
        print(f"\n[*] Setting up tool: {name}")
        tool_path = os.path.join(base_dir, name)

        if not os.path.exists(tool_path):
            try:
                subprocess.run(["git", "clone", repo, tool_path], check=True)
                print(f"[+] {name} cloned successfully.")
            except subprocess.CalledProcessError as e:
                print(f"[!] Failed to clone {name}: {e}")
                summary.append((name, "Clone Failed"))
                continue
        else:
            print(f"[=] {name} already exists. Skipping clone.")

        print(f"[~] Ensure you install dependencies for {name} using the main requirements.txt.")
        summary.append((name, "✅ Cloned, install requirements from root requirements.txt"))

    print("\n=======================")
    print("📦 Installation Summary")
    print("=======================")
    for tool, status in summary:
        print(f"{tool.ljust(20)} : {status}")

if __name__ == "__main__":
    clone_and_setup_tools()
