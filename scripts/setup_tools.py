import os
import subprocess

TOOLS = {
    "Katana": "https://github.com/0xStrontium/Katana.git",
    "OnionSearch": "https://github.com/megadose/OnionSearch.git",
    "darkdump": "https://github.com/josh0xA/darkdump.git",
    "ahmia-site": "https://github.com/ahmia/ahmia-site.git",
    "Darkus": "https://github.com/Lucksi/Darkus.git",
    "onionscan": "https://github.com/s-rah/onionscan.git",
    "Onioff": "https://github.com/k4m4/onioff.git",
    "docker-onion-nmap": "https://github.com/milesrichardson/docker-onion-nmap.git",
    "TorBot": "https://github.com/DedSecInside/TorBot.git",
    "TorCrawl.py": "https://github.com/MikeMeliz/TorCrawl.py.git",
    "VigilantOnion": "https://github.com/andreyglauzer/VigilantOnion.git",
    "OnionIngestor": "https://github.com/danieleperera/OnionIngestor.git",
    "Darc": "https://github.com/JarryShaw/darc.git",
    "midnight_sea": "https://github.com/RicYaben/midnight_sea.git",
    "pryingdeep": "https://github.com/iudicium/pryingdeep.git",
    "deepdarkCTI": "https://github.com/fastfire/deepdarkCTI.git"
}

def install_dependencies(tool_path, tool_name):
    handled = False
    report = []

    def try_install(cmd, desc):
        try:
            subprocess.run(cmd, check=True)
            print(f"[+] Installed using {desc}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Failed to install with {desc}: {e}")
            return False

    if os.path.exists(os.path.join(tool_path, "requirements.txt")):
        handled = try_install(["pip3", "install", "-r", os.path.join(tool_path, "requirements.txt")], "requirements.txt")
    elif os.path.exists(os.path.join(tool_path, "setup.py")):
        handled = try_install(["pip3", "install", "-e", tool_path], "setup.py")
    elif os.path.exists(os.path.join(tool_path, "pyproject.toml")):
        handled = try_install(["pip3", "install", tool_path], "pyproject.toml")
    elif os.path.exists(os.path.join(tool_path, "Pipfile")):
        handled = try_install(["pip3", "install", "pipenv"], "pipenv") and \
                  try_install(["pipenv", "install"], "Pipfile via pipenv")
    else:
        for fname in os.listdir(tool_path):
            if fname.endswith((".txt", ".cfg", ".toml")):
                report.append(fname)

    return handled, report

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

        success, report = install_dependencies(tool_path, name)
        if success:
            summary.append((name, "✅ Installed dependencies"))
        else:
            if report:
                summary.append((name, f"⚠️ Needs manual install (found: {', '.join(report)})"))
            else:
                summary.append((name, "❌ No dependency file found"))

    print("\n=======================")
    print("📦 Installation Summary")
    print("=======================")
    for tool, status in summary:
        print(f"{tool.ljust(20)} : {status}")

if __name__ == "__main__":
    clone_and_setup_tools()
