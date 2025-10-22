# Twitch Bot Command Generator

A GUI application for generating bot commands for x_pilot's Twitch chat.

## Features

- **Difficulty Selection**: Choose from medium, gm, basic, or auto difficulty levels
- **Character Selection**: Select from available characters for each difficulty
- **Command Generation**: Automatically generates `!agent difficulty-character` commands
- **Copy to Clipboard**: One-click copying of generated commands
- **Modern UI**: Clean, dark-themed interface optimized for Twitch streaming

## For End Users (Simple)

**Just download and run the executable:**
1. Download `PhillipUI.exe` from the releases
3. Double-click the .exe file to run the program
4. No installation or setup required!

## For Developers

### Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Building the Executable

To create a standalone .exe file for distribution:

1. **Quick build** (Windows):
   ```bash
   build.bat
   ```

2. **Manual build**:
   ```bash
   python build_exe.py
   ```

The executable will be created in the `dist/` folder as `TwitchBotCommandGen.exe`

### Development Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Select a difficulty from the dropdown menu
3. Choose a character from the grid of available characters
4. The command will be automatically generated in the format `!agent difficulty-character`
5. Click "Copy to Clipboard" to copy the command to your clipboard
6. Paste the command into x_pilot's Twitch chat

## Available Commands

The application supports all the following agent combinations:

- **Medium**: fox, falco, marth, sheik
- **GM**: fox, falco, marth, sheik  
- **Basic**: popo, pikachu, fox, ganondorf, link, dk, yoshi, jigglypuff, marth, samus, luigi, sheik, peach, cptfalcon, falco, doc
- **Auto**: popo, jigglypuff, sheik, doc, cptfalcon, falco, dk, yoshi, fox, pikachu, marth, peach, samus, luigi, ganondorf, link

## Example

If you select "basic" difficulty and "falco" character, the generated command will be:
```
!agent basic-falco
```

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- Pillow (for image support)
- pyperclip (for clipboard functionality)
