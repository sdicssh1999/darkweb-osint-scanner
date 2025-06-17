#!/bin/bash

echo "🔧 [1/6] Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📦 [2/6] Installing Python requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🛠️ [3/6] Cloning all dark web OSINT tools..."
python3 scripts/setup_tools.py

echo "🧱 [4/6] Creating config and data directories..."
mkdir -p config data logs

if [ ! -f config/keywords.txt ]; then
  echo "# keywords will be auto-generated per scan" > config/keywords.txt
fi

echo "🎉 [5/6] Setup Complete!"
echo "To start scanning, run:"
echo "source venv/bin/activate && python3 scripts/darkwebosint.py"

echo "🚀 [6/6] Launching Tool Now..."
python3 scripts/darkwebosint.py

