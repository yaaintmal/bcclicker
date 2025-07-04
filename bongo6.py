import ctypes
import time

# Konstanten für Mausereignisse
MOUSEEVENTF_MOVE = 0x0001  # Maus bewegen
MOUSEEVENTF_LEFTDOWN = 0x0002  # Linke Maustaste gedrückt
MOUSEEVENTF_LEFTUP = 0x0004  # Linke Maustaste losgelassen

COUNTS = 1000

# Funktion zum Ausführen eines Mausklicks an der aktuellen Position
def mouse_click():
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.05)  # Kleine Pause zwischen Drücken und Loslassen
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# Beispiel: Mausklick nach einer Sekunde ausführen
time.sleep(3)
for _ in range(COUNTS):
    time.sleep(0.05)
    mouse_click()
