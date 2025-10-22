"""
Test script to verify that images are properly bundled in the executable.
Run this to check if the CSS Icons folder and images are accessible.
"""

import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        print(f"Running as PyInstaller executable, base path: {base_path}")
    except Exception:
        base_path = os.path.abspath(".")
        print(f"Running as Python script, base path: {base_path}")
    return os.path.join(base_path, relative_path)

def test_image_loading():
    """Test if images can be loaded"""
    print("Testing image loading...")
    
    # Test CSS Icons folder
    css_icons_path = resource_path("CSS Icons")
    print(f"CSS Icons path: {css_icons_path}")
    print(f"CSS Icons exists: {os.path.exists(css_icons_path)}")
    
    if os.path.exists(css_icons_path):
        print("Contents of CSS Icons folder:")
        try:
            files = os.listdir(css_icons_path)
            for file in files[:5]:  # Show first 5 files
                print(f"  - {file}")
            if len(files) > 5:
                print(f"  ... and {len(files) - 5} more files")
        except Exception as e:
            print(f"Error listing files: {e}")
    
    # Test specific image
    test_image = resource_path(os.path.join("CSS Icons", "Fox_Standard_CSS Icon_HD.png"))
    print(f"Test image path: {test_image}")
    print(f"Test image exists: {os.path.exists(test_image)}")
    
    # Test PIL loading
    try:
        from PIL import Image
        if os.path.exists(test_image):
            img = Image.open(test_image)
            print(f"Successfully loaded image: {img.size}, mode: {img.mode}")
        else:
            print("Cannot test PIL loading - image file not found")
    except Exception as e:
        print(f"Error loading image with PIL: {e}")

if __name__ == "__main__":
    test_image_loading()
    input("Press Enter to exit...")

