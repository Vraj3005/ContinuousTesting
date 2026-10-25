@echo off
title STQA P9 - Run Pytest
cd /d "%~dp0"
echo ==============================================================
echo   STQA Practical 9: Running Automated Pytest Suite
echo ==============================================================
python -m pytest -v
echo ==============================================================
pause
