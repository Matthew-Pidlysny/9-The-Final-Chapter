@echo off
echo 🚀 Starting The Falcon Press Office...

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "falcon_press_office.py" (
    echo ❌ falcon_press_office.py not found
    pause
    exit /b 1
)

echo 🎯 Launching The Falcon Press Office...
python falcon_press_office.py
pause
