@echo off
title STQA P9 - Continuous Testing Pipeline Runner
cd /d "%~dp0"
python "%~dp0simulate_pipeline.py"
pause
