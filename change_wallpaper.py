import platform
import sys

def set_wallpaper(image_path):
    os_name = platform.system()

    if os_name == 'Windows':
        try:
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        except ImportError:
            print("Error: Unable to import 'ctypes' library. Run 'pip install ctypes' in your shell and try again.")
            sys.exit(1)

    elif os_name == 'Darwin':
        try:
            import osascript
            script = f'''
            tell application "Finder"
                set desktop picture to POSIX file "{image_path}"
            end tell
            '''
            osascript.run(script)
        except ImportError:
            print("Error: Unable to import 'osascript' library. Run 'pip install osascript' in your shell and try again.")
            sys.exit(1)

    elif os_name == 'Linux':
        try:
            import subprocess
            command = f"sudo gsettings set org.gnome.desktop.background picture-uri file://{image_path}"
            subprocess.call(command, shell=True)
        except ImportError:
            print("Error: Unable to import 'subprocess' library. Run 'pip install subprocess' in your shell and try again.")
            sys.exit(1)

    else:
        print(f"Error: Operating system {os_name} is not supported for changing wallpaper.")
        sys.exit(1)

