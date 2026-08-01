#!/bin/bash
echo "[*] Installing Lernaean..."

if command -v pkg &> /dev/null; then
    pkg update -y && pkg install -y python git nmap
elif command -v apt &> /dev/null; then
    sudo apt update && sudo apt install -y python3 python3-pip git nmap
elif command -v pacman &> /dev/null; then
    sudo pacman -Syu --noconfirm python python-pip git nmap
fi

pip install -r requirements.txt
chmod +x lernaean.py
echo "[+] Done. Run: python lernaean.py"
