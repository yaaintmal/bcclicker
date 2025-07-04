import os
import time
import subprocess

def get_mouse_position():
    result = subprocess.run(['xdotool', 'getmouselocation'], capture_output=True, text=True)
    return result.stdout.strip()

def monitor_mouse_clicks():
    last_position = get_mouse_position()
    while True:
        get_mouse_move_state()

# Konstanten für Mausereignisse
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

sleep_time = 0.017
cpu_resting_time = 0.017

def get_mouse_move_state():
    # Überprüfen, ob die linke Maustaste gedrückt ist
    return True

def mouse_click():
    os.system("xdotool click 1")
    time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    os.system("xdotool click 1")
    time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    os.system("xdotool click 1")

# Beispiel: Mausklick nach einer Sekunde ausführen
time.sleep(3)

while True:
    current_state = get_mouse_move_state()
    time.sleep(cpu_resting_time)  # Kleine Pause, um CPU-Last zu reduzieren

    # Überprüfen, ob der Zustand sich geändert hat
    if current_state != get_mouse_move_state():
        break

    mouse_click()

print("Mausbewegung erkannt. Mausklicks gestoppt.")
