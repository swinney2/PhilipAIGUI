@echo off
echo Testing the executable version...
echo.

REM Test the main executable
echo Running TwitchBotCommandGen.exe...
start "" "dist\TwitchBotCommandGen.exe"

echo.
echo The executable should now be running with character icons.
echo If you see gray boxes instead of character images, the icons are not loading properly.
echo.
pause

