import time
import platform

sleep_time = 0.017
cpu_resting_time = 0.017

# Funktion zum Erkennen von Mausbewegungen (Plattformunabhängig)
def get_mouse_move_state():
    # Diese Funktion muss implementiert werden, um Mausbewegungen zu erkennen.
    # Da dies plattformabhängig ist, müssen wir verschiedene Ansätze verwenden.
    if platform.system() == "Windows":
        import ctypes
        return ctypes.windll.user32.GetKeyState(0x01)

    pass

# Funktion zum Ausführen eines Mausklicks (Plattformunabhängig)
def mouse_click():
    if platform.system() == "Windows":
        import ctypes
        MOUSEEVENTF_LEFTDOWN = 0x0002
        MOUSEEVENTF_LEFTUP = 0x0004

        # Mausklick simulieren: Tasten gedrückt und losgelassen
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(sleep_time)  # Kleine Pause zwischen Drücken und Loslassen
    elif platform.system() == "Linux":
        import os
        # Mausklick simulieren: Tasten gedrückt und losgelassen (mögliche Lösung unter Linux)
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
