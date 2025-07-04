import time
import ctypes
from ctypes import wintypes

# Definiere die benötigten Konstanten und Strukturen
VK_CODE = {
    'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44, 'E': 0x45,
    'F': 0x46, 'G': 0x47, 'H': 0x48, 'I': 0x49, 'J': 0x4A,
    'K': 0x4B, 'L': 0x4C, 'M': 0x4D, 'N': 0x4E, 'O': 0x4F,
    'P': 0x50, 'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54,
    'U': 0x55, 'V': 0x56, 'W': 0x57, 'X': 0x58, 'Y': 0x59,
    'Z': 0x5A
}

# Virtuelle Schlüsselcodes für Zahlen und Leertaste
for i in range(10):
    VK_CODE[str(i)] = 0x30 + i

VK_CODE['SPACE'] = 0x20

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("ki", KEYBDINPUT)]

    _anonymous_ = ("_input",)
    _fields_ = [("type", wintypes.DWORD),
                ("_input", _INPUT)]

def send_key(vk_code, press=True):
    flags = 0 if press else 2
    xi = INPUT()
    xi.type = 1  # INPUT_KEYBOARD
    xi.ki.wVk = vk_code
    xi.ki.dwFlags = flags
    ctypes.windll.user32.SendInput(1, ctypes.byref(xi), ctypes.sizeof(xi))
    print(f"Sent key: {vk_code}, Press: {press}")

def simulate_typing(text):
    for char in text.upper():
        if char == ' ':
            send_key(VK_CODE['SPACE'], True)
            time.sleep(0.05)
            send_key(VK_CODE['SPACE'], False)
        elif char in VK_CODE:
            send_key(VK_CODE[char], True)
            time.sleep(0.05)
            send_key(VK_CODE[char], False)

if __name__ == "__main__":
    print("Die Simulation beginnt in 5 Sekunden...")
    time.sleep(5) # Warte 5 Sekunden bevor mit dem Tippen begonnen wird

    num_words = 100
    text_to_type = "TEST " * (num_words // 4 + 1)

    print(f"Starte das Tippen von {num_words} Wörtern...")
    simulate_typing(text_to_type)
    print("Tippen abgeschlossen!")
