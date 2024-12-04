msg "%username%" Downloading Python
color 0a
@echo off

set PYTHON_VERSION=3.11.6
set INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
set INSTALLER_FILE=python-%PYTHON_VERSION%-amd64.exe

echo Downloading Python %PYTHON_VERSION% installer...
powershell -Command "& { (New-Object System.Net.WebClient).DownloadFile('%INSTALLER_URL%', '%INSTALLER_FILE%') }"

if not exist %INSTALLER_FILE% (
    echo Failed to download the Python installer. Please check your internet connection or URL.
    pause
    exit /b 1
)

echo Installing Python %PYTHON_VERSION%...
%INSTALLER_FILE% /quiet InstallAllUsers=1 PrependPath=1

python --version >nul 2>&1
if %ERRORLEVEL%==0 (
    echo Python %PYTHON_VERSION% installed successfully!
    python --version
) else (
    echo Python installation failed. Please check the installer log or try manually.
)

del %INSTALLER_FILE%

echo Bitch, Python is installed now.

msg "%username%" Downloading other taip-shi'

echo Installing other dependencies...

pip install pygame
pip install Pillow

echo Everything is now installed. Press anything to exit.

pause
