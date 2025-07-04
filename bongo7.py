import ctypes
import time

# Konstanten für Mausereignisse
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

sleep_time = 0.0169
cpu_resting_time = 0.0169

def get_mouse_move_state():
    # Überprüfen, ob die linke Maustaste gedrückt ist
    return ctypes.windll.user32.GetKeyState(0x01)

def mouse_click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

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
