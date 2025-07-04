import pyautogui
import random
import time

# Warten Sie kurz, um sicherzustellen, dass der Benutzer Zeit hat, sich auf den Klick vorzubereiten.
time.sleep(5)

for _ in range(10):
    # Generieren Sie eine zufällige Position auf dem Bildschirm
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)

    # Bewegen Sie die Maus zur generierten Position und klicken Sie
    # pyautogui.moveTo(x, y, duration=0.25)  # Dauer von 0.25 Sekunden für eine sanfte Bewegung
    pyautogui.click()

print("10 Mausklicks ausgeführt.")
