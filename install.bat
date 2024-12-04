color 0a
msg "%username%" Downloading Python
winget install -e --id Python.Python.3.11 --scope machine
echo Bitch, Python is installed now.
echo Installing other dependencies...
pip install pygame
pause