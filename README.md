# Manual Join Macro Controller

Automatically detects Roblox Error 276 when you join Roblox on another device while a macro is running on your PC.

The controller automatically pauses your macro when the error appears and resumes it after you leave Roblox on the other device.

## Features

- **Error 276 Detection:** Detects the Roblox account conflict popup using pixel detection.
- **Automatic Pause:** Sends F3 three times to stop your macro.
- **Roblox Presence Monitoring:** Checks whether your Roblox account is still playing on the other device.
- **Automatic Resume:** Sends F1 to restart your macro after you leave Roblox.

## Requirements

- Windows 10 or Windows 11 (64-bit)
- Python 3.14 (64-bit)
- A macro program that supports customizable keyboard binds
- A Roblox account
- Internet connection
- 1920 × 1080 screen resolution (current version)

## IMPORTANT: Macro Keybinds

Your macro program MUST use these keyboard binds:

- **Start Macro: F1**
- **Stop/End Macro: F3**

These keybinds are required for the controller to work correctly.

Make sure they are configured before running the script.

## Installation

### 1. Install Python

Download **Python 3.14.x (64-bit for Windows)** from the official Python website:

https://www.python.org/downloads/

During installation:

1. Open the downloaded installer.
2. Check **Add Python to PATH**.
3. Click **Install Now**.
4. Wait for installation to finish.

### 2. Download the Controller

1. Open this GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the downloaded ZIP file.

### 3. Install Required Packages

Open Command Prompt and enter:

`py -3.14 -m pip install pyautogui`

Wait for the installation to finish.

### 4. Configure Your Roblox User ID

1. Right-click `ManualJoinMacroController.py`.
2. Open it with Notepad.
3. Find the USER SETTINGS section near the top:

   `ROBLOX_USER_ID = 123456789`

4. Replace `123456789` with your own Roblox User ID.
5. Save the file.

**How to find your Roblox User ID:**

1. Open your Roblox profile in a browser.
2. Look at the profile URL.
3. Your User ID is the number in the URL.

### 5. Configure Your Macro

Make sure your macro software uses these keybinds:

- F1 to start your macro.
- F3 to stop your macro.

The controller will not work correctly if these binds are different.

## How to Use

1. Open your macro software.
2. Start your macro.
3. Run `ManualJoinMacroController.py`.
4. Join a Roblox experience on your Xbox or another device.
5. When Error 276 appears on your PC, the controller detects it and sends F3 to stop your macro.
6. The controller monitors your Roblox presence while you play on the other device.
7. Once you leave Roblox, the controller sends F1 to restart your macro.

## Run in the Background Automatically

You can configure the controller to start automatically whenever you sign in to Windows, without opening Command Prompt.

### Setup

1. Press `Windows + R` on your keyboard.
2. Type `shell:startup` and press Enter.
3. Right-click inside the Startup folder.
4. Select **New → Shortcut**.
5. Enter the following format as the shortcut location:

   `"FULL PATH TO pythonw.exe" "FULL PATH TO ManualJoinMacroController.py"`

   Example:

   `"C:\Users\YourName\AppData\Local\Programs\Python\Python314\pythonw.exe" "C:\Users\YourName\OneDrive\Desktop\ManualJoinMacroController.py"`

6. Click Next.
7. Name the shortcut `Manual Join Macro Controller`.
8. Click Finish.

The controller will now automatically launch in the background whenever you sign in to Windows.

**Important:**
- Windows must be running.
- You must be signed in to your Windows account.
- Your PC cannot be asleep or shut down.
- Keep the Python script in the same location used by the shortcut.

## Important Notes

- The current pixel detection is configured for 1920 × 1080.
- Your Roblox User ID must be configured correctly.
- Your macro must use F1 to start and F3 to stop.
- An internet connection is required to check Roblox presence.
- The controller is designed for Windows.
- This project is not affiliated with Roblox or any macro software.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
