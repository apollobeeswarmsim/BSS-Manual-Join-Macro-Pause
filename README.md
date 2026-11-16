# Manual Join Macro Controller

Automatically detects Roblox Error 276 when you join Roblox on another device while a macro is running on your PC.

The controller pauses your macro when the error appears and automatically resumes it after you leave Roblox on the other device.

## Features

- **Error 276 Detection:** Detects the Roblox account conflict popup using pixel detection.
- **Automatic Pause:** Sends F3 three times to stop your macro.
- **Roblox Presence Monitoring:** Checks whether your Roblox account is still playing on the other device.
- **Automatic Resume:** Sends F1 to restart your macro after you leave.

## Requirements

- Windows 10 or Windows 11
- Python 3
- A macro program that supports customizable keyboard binds
- A Roblox account
- Internet connection
- 1920 × 1080 screen resolution (current configuration)

## IMPORTANT: Macro Keybinds

Your macro program MUST use these keybinds:

- **Start Macro: F1**
- **Stop/End Macro: F3**

These keybinds are required for the controller to work correctly.

## Installation

1. Install Python from https://www.python.org/downloads/
2. Download or clone this repository.
3. Open Command Prompt and install PyAutoGUI:

   `python -m pip install pyautogui`

4. Open `ManualJoinMacroController.py` in Notepad or another text editor.
5. At the top of the script, find:

   `ROBLOX_USER_ID = 123456789`

6. Replace `123456789` with your own Roblox User ID.
7. Save the file.

**How to find your Roblox User ID:** Open your Roblox profile in a browser. Your User ID is the number in your profile URL.

## How to Use

1. Open your macro program.
2. Start your macro.
3. Run `ManualJoinMacroController.py`.
4. Join a Roblox experience on another device.
5. When Error 276 appears on your PC, the controller detects it and sends F3.
6. The controller monitors your Roblox presence.
7. Once you leave Roblox on the other device, the controller sends F1 to restart your macro.

## Run in the Background Automatically

You can configure the controller to start automatically whenever you sign in to Windows, without opening Command Prompt.

1. Press `Windows + R`.
2. Type `shell:startup` and press Enter.
3. Right-click inside the Startup folder.
4. Select **New → Shortcut**.
5. For the shortcut location, enter the paths to your Python `pythonw.exe` and `ManualJoinMacroController.py`, using this format:

   `"FULL PATH TO pythonw.exe" "FULL PATH TO ManualJoinMacroController.py"`

   For example:

   `"C:\Users\YourName\AppData\Local\Programs\Python\Python314\pythonw.exe" "C:\Users\YourName\Desktop\ManualJoinMacroController.py"`

6. Name the shortcut `Manual Join Macro Controller`.
7. Finish creating the shortcut.

The controller will now launch in the background when you sign in to Windows.

**Important:** Windows must be running and you must be signed in. The controller will not run while the PC is shut down or asleep.

## Important Notes

- The current pixel detection is configured for 1920 × 1080.
- Your Roblox User ID must be configured correctly.
- Your macro must use F1 to start and F3 to stop.
- The controller needs an internet connection to check Roblox presence.
- This project is not affiliated with Roblox or any macro software.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
