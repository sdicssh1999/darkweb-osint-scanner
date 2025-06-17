# scripts/runner.py
import os
import subprocess
from utils import tool_entry_points, write_log

TOOLS_DIR = "tools"


def run_tool(tool_name, entry_script):
    tool_path = os.path.join(TOOLS_DIR, tool_name)
    try:
        if not os.path.exists(tool_path):
            print(f"[!] {tool_name} not found in tools/. Skipping.")
            return

        os.chdir(tool_path)

        if entry_script:
            print(f"[*] Running {tool_name}...")
            write_log(f"Running {tool_name} with {entry_script}")

            # Different run logic per tool
            if tool_name.lower() == "katana":
                subprocess.run(["python3", entry_script, "-t"])
            elif tool_name.lower() == "darkdump":
                subprocess.run(["python3", entry_script, "--help"])
            elif tool_name.lower() == "onionsearch":
                subprocess.run(["python3", "setup.py", "install"])
            elif tool_name.lower() == "onioff":
                subprocess.run(["python3", entry_script])
            elif tool_name.lower() == "torbot":
                subprocess.run(["python3", entry_script, "--help"])
            else:
                subprocess.run(["python3", entry_script])
        else:
            print(f"[-] No launch script defined for {tool_name}. Manual execution may be needed.")
            write_log(f"Skipped {tool_name} due to missing entry point.")

    except Exception as e:
        print(f"[!] Error running {tool_name}: {e}")
        write_log(f"Error running {tool_name}: {e}")
    finally:
        os.chdir("../../")


def run_all_tools():
    print("[*] Running selected tools...")
    for tool, entry in tool_entry_points.items():
        run_tool(tool, entry)
