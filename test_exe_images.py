"""
Test script specifically for testing the executable version.
This will be bundled with the executable to test image loading.
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

def test_executable_images():
    """Test image loading in executable"""
    print("=== Testing Image Loading in Executable ===")
    
    # Test CSS Icons folder
    css_icons_path = resource_path("CSS Icons")
    print(f"CSS Icons path: {css_icons_path}")
    print(f"CSS Icons exists: {os.path.exists(css_icons_path)}")
    
    if os.path.exists(css_icons_path):
        print("Contents of CSS Icons folder:")
        try:
            files = os.listdir(css_icons_path)
            print(f"Found {len(files)} files")
            for file in files[:3]:  # Show first 3 files
                print(f"  - {file}")
        except Exception as e:
            print(f"Error listing files: {e}")
    else:
        print("CSS Icons folder not found!")
        return False
    
    # Test specific images
    test_images = [
        "Fox_Standard_CSS Icon_HD.png",
        "Marth_Standard_CSS Icon_HD.png",
        "Falco_Standard_CSS Icon_HD.png"
    ]
    
    success_count = 0
    for image_name in test_images:
        image_path = resource_path(os.path.join("CSS Icons", image_name))
        exists = os.path.exists(image_path)
        print(f"{image_name}: {'✓' if exists else '✗'}")
        if exists:
            success_count += 1
    
    print(f"\nImage loading test: {success_count}/{len(test_images)} images found")
    return success_count == len(test_images)

if __name__ == "__main__":
    success = test_executable_images()
    if success:
        print("\n✅ All images loaded successfully!")
    else:
        print("\n❌ Some images failed to load!")
    
    input("\nPress Enter to exit...")

