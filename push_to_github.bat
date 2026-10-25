@echo off
setlocal
title STQA P9 - Push to GitHub Repository
cd /d "%~dp0"

echo ==============================================================
echo    STQA Practical 9: Push to GitHub Repository
echo ==============================================================
echo Your current Git user:
git config user.name
git config user.email
echo ==============================================================
echo Default remote repo: https://github.com/Vraj3005/ContinuousTesting.git
set /p "REPO_URL=Enter your GitHub Repo URL [or press Enter for default]: "
if "%REPO_URL%"=="" set "REPO_URL=https://github.com/Vraj3005/ContinuousTesting.git"

git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main

echo Pushing main branch to %REPO_URL% ...
git push -u origin main

if %errorlevel% equ 0 (
    echo ==============================================================
    echo Successfully pushed to GitHub!
    echo Check your GitHub Actions tab to view the live CI pipeline!
    echo ==============================================================
) else (
    echo ==============================================================
    echo [NOTE] If authentication is required, make sure you created the
    echo repository on GitHub first and sign in with your GitHub credentials.
    echo ==============================================================
)
pause
