"""
Build script to create a standalone executable for the Twitch Bot Command Generator.
Run this script to create a single .exe file that users can run without Python installed.
"""

import subprocess
import sys
import os

def build_executable():
    """Build the standalone executable using PyInstaller."""
    
    print("Building standalone executable...")
    print("This may take a few minutes...")
    
    # PyInstaller command to create a single executable file
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create a single executable file
        "--windowed",                   # Hide console window (GUI app)
        "--name=TwitchBotCommandGen",   # Name of the executable
        "--icon=icon.ico",              # Icon file (if exists)
        "--add-data=README.md;.",       # Include README in the bundle
        "--add-data=CSS Icons;CSS Icons",  # Include character icons
        "--add-data=test_exe_images.py;.",  # Include test script
        "--clean",                      # Clean cache before building
        "main.py"                       # Main script file
    ]
    
    # Remove icon parameter if icon file doesn't exist
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build successful!")
        print(f"Executable created: dist/TwitchBotCommandGen.exe")
        print("\nYou can now distribute the .exe file to users.")
        print("Users can simply double-click the .exe to run the program.")
        
    except subprocess.CalledProcessError as e:
        print("Build failed!")
        print(f"Error: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error output: {e.stderr}")
        return False
    
    except FileNotFoundError:
        print("PyInstaller not found!")
        print("Please install PyInstaller first:")
        print("pip install pyinstaller")
        return False
    
    return True

if __name__ == "__main__":
    print("Twitch Bot Command Generator - Executable Builder")
    print("=" * 50)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build the executable
    success = build_executable()
    
    if success:
        print("\nBuild completed successfully!")
        print("The executable is ready for distribution.")
    else:
        print("\nBuild failed. Please check the error messages above.")
    
    input("\nPress Enter to exit...")
