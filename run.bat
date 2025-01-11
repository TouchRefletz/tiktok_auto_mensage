@echo off
pip install -r "%~dp0requirements.txt"
cd /d "%~dp0"
python main.py
exit
