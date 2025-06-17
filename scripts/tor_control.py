import subprocess

def start_tor_service():
    print("[*] Checking Tor service...")
    try:
        subprocess.run(["service", "tor", "start"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("[+] Tor service started.")
    except subprocess.CalledProcessError:
        print("[!] Failed to start Tor. Please ensure it's installed and enabled.")
    except Exception as e:
        print(f"[!] Unexpected error while starting Tor: {e}")

def stop_tor_service():
    print("[*] Stopping Tor service...")
    try:
        subprocess.run(["service", "tor", "stop"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("[+] Tor service stopped.")
    except Exception as e:
        print(f"[!] Failed to stop Tor: {e}")
