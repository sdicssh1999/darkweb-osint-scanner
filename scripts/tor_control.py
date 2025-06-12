import subprocess

def start_tor_service():
    print("[*] Checking Tor service...")
    try:
        subprocess.run(["service", "tor", "start"], check=True)
        print("[+] Tor service started.")
    except Exception as e:
        print(f"[!] Failed to start Tor: {e}")
