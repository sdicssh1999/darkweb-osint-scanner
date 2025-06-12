import subprocess

def start_tor_service():
    print("[*] Checking Tor service...")
    try:
        subprocess.run(["service", "tor", "start"], check=True)
        print("[+] Tor service started.")
    except Exception as e:
        print(f"[!] Failed to start Tor: {e}")

def stop_tor_service():
    print("[*] Stopping Tor service...")
    try:
        subprocess.run(["service", "tor", "stop"], check=True)
        print("[+] Tor service stopped.")
    except Exception as e:
        print(f"[!] Failed to stop Tor: {e}")
