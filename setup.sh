#!/bin/bash

echo "[*] Creating directory structure..."
mkdir -p tools config data scripts

echo "[*] Creating keywords file..."
cat > config/keywords.txt <<EOF
reward360
admin login
internal portal
confidential
EOF

echo "[*] Cloning all dark web OSINT tools..."
cd tools

declare -a repos=(
  "https://github.com/projectdiscovery/katana"
  "https://github.com/megadose/OnionSearch"
  "https://github.com/josh0xA/darkdump"
  "https://github.com/ahmia/ahmia-site"
  "https://github.com/Lucksi/Darkus"
  "https://github.com/s-rah/onionscan"
  "https://github.com/k4m4/onioff"
  "https://github.com/milesrichardson/docker-onion-nmap"
  "https://github.com/DedSecInside/TorBot"
  "https://github.com/MikeMeliz/TorCrawl.py"
  "https://github.com/andreyglauzer/VigilantOnion"
  "https://github.com/danieleperera/OnionIngestor"
  "https://github.com/JarryShaw/darc"
  "https://github.com/RicYaben/midnight_sea"
  "https://github.com/iudicium/pryingdeep"
  "https://github.com/fastfire/deepdarkCTI"
)

for repo in "${repos[@]}"; do
  git clone "$repo"
done

cd ..

echo "[*] Installing Python requirements..."
pip install -r requirements.txt

echo "[*] Installing Tor..."
sudo apt update
sudo apt install -y tor

echo "[✓] Setup completed successfully. You're ready to scan!"
delete setup.sh - moved setup to Python


