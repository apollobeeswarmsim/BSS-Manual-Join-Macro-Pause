import time
import json
import threading
import urllib.request
import pyautogui

from datetime import datetime

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

# ==================================================
# USER SETTINGS - CHANGE THESE
# ==================================================

# Replace 123456789 with YOUR Roblox User ID.
ROBLOX_USER_ID = 123456789

# ==================================================
# CONTROLLER SETTINGS
# ==================================================

PRESENCE_URL = "https://presence.roblox.com/v1/presence/users"
PRESENCE_INTERVAL = 5

# Current screen configuration: 1920 x 1080
PIXEL_REGION = (958, 538, 3, 3)

# Roblox Error 276 popup background colour
TARGET_RGB = (57, 59, 61)
COLOUR_TOLERANCE = 12
REQUIRED_MATCHES = 8

lock = threading.Lock()

state = {
    "armed": True,
    "waiting_for_xbox_end": False,
    "waiting_for_popup_clear": False,
    "end_count": 0
}


def detect_popup():
    pixels = pyautogui.screenshot(region=PIXEL_REGION)

    matches = 0

    for pixel in pixels.getdata():
        if all(
            abs(pixel[i] - TARGET_RGB[i]) <= COLOUR_TOLERANCE
            for i in range(3)
        ):
            matches += 1

    return matches >= REQUIRED_MATCHES


def presence_monitor():
    while True:
        with lock:
            active = state["waiting_for_xbox_end"]

        if not active:
            time.sleep(0.5)
            continue

        try:
            data = json.dumps({
                "userIds": [ROBLOX_USER_ID]
            }).encode("utf-8")

            request = urllib.request.Request(
                PRESENCE_URL,
                data=data,
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                method="POST"
            )

            with urllib.request.urlopen(
                request, timeout=10
            ) as response:
                result = json.loads(
                    response.read().decode("utf-8")
                )

            status = result["userPresences"][0][
                "userPresenceType"
            ]

            print(
                datetime.now().strftime("%H:%M:%S"),
                "Roblox status:",
                status
            )

            send_f1 = False

            with lock:
                if not state["waiting_for_xbox_end"]:
                    continue

                if status == 2:
                    state["end_count"] = 0
                    print("Status 2: Still playing. Waiting.")

                elif status in (1, 0):
                    state["end_count"] += 1

                    print(
                        "Not playing confirmation:",
                        state["end_count"], "/ 2"
                    )

                    if state["end_count"] >= 2:
                        state["waiting_for_xbox_end"] = False
                        state["waiting_for_popup_clear"] = True
                        state["end_count"] = 0
                        send_f1 = True

                else:
                    state["end_count"] = 0

            if send_f1:
                print("Other-device Roblox session appears to have ended.")
                pyautogui.press("f1")
                print("F1 SENT!")
                print("Waiting for popup to clear.")

        except Exception as error:
            print("Presence API error:", error)

        time.sleep(PRESENCE_INTERVAL)


threading.Thread(
    target=presence_monitor,
    daemon=True
).start()

print("--------------------------------")
print("MANUAL JOIN MACRO CONTROLLER")
print("Watching for Roblox Error 276.")
print("F3 stops the macro.")
print("F1 restarts the macro.")
print("Press CTRL+C to exit.")
print("--------------------------------")

try:
    while True:
        popup_detected = detect_popup()
        send_f3 = False

        with lock:
            if state["waiting_for_popup_clear"]:
                if not popup_detected:
                    state["waiting_for_popup_clear"] = False
                    state["armed"] = True
                    print("Popup cleared. Watching again.")

            elif state["armed"] and popup_detected:
                state["armed"] = False
                state["waiting_for_xbox_end"] = True
                state["end_count"] = 0
                send_f3 = True

        if send_f3:
            print("ERROR 276 PIXEL PATTERN DETECTED!")
            pyautogui.press("f3", presses=3, interval=0.05)
            print("F3 SENT THREE TIMES!")
            print("Waiting for other-device session to end.")

except KeyboardInterrupt:
    print("\nController stopped safely.")
