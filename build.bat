@echo off
echo Building Twitch Bot Command Generator Executable...
echo.

REM Install PyInstaller if not already installed
echo Installing/updating PyInstaller...
pip install pyinstaller

echo.
echo Building executable (this may take a few minutes)...
python build_exe.py

echo.
echo Build process completed!
echo Check the 'dist' folder for your executable.
pause
