@echo off
echo [*] Installing Lernaean...
where python >nul 2>nul || (echo Install Python first & exit /b)
pip install -r requirements.txt
echo [+] Done. Run: python lernaean.py
