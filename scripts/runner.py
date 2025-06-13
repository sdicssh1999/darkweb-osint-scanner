import os
import subprocess
from scripts.utils import TOOL_ENTRY_POINTS

def run_tool(tool_name, base_path="tools/", output_dir="data/", keywords=[]):
    tool_path = os.path.join(base_path, tool_name)
    entry_point = TOOL_ENTRY_POINTS.get(tool_name)

    if entry_point is None:
        print(f"[-] {tool_name}: No known Python entry file. Manual review needed.")
        return

    full_path = os.path.join(tool_path, entry_point)
    if not os.path.isfile(full_path):
        print(f"[-] {tool_name}: Entry file {entry_point} not found.")
        return

    print(f"[+] Running {tool_name}...")
    try:
        cmd = ["python3", full_path] + keywords
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        output_file = os.path.join(output_dir, f"{tool_name}_output.txt")
        with open(output_file, "w") as f:
            f.write(result.stdout)
        print(f"[+] Output saved: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running {tool_name}: {e}")

