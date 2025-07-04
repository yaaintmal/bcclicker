import pyautogui
import time

def generate_text(num_words):
    # Erstelle eine Liste von 100 Wörtern (hier einfache Wiederholungen des Wortes "Test")
    words = ["Test"] * num_wordsTest Test Test Test
    return ' '.join(words)

def simulate_typing(text, delay=0.05):
    for char in text:
        pyautogui.press(char)
        time.sleep(delay)

if __name__ == "__main__":
    print("Die Simulation beginnt in 5 Sekunden...")
    time.sleep(5) # Warte 5 Sekunden bevor mit dem Tippen begonnen wird

    num_words = 100
    text_to_type = generate_text(num_words)

    print(f"Starte das Tippen von {num_words} Wörtern...")
    simulate_typing(text_to_type)
    print("Tippen abgeschlossen!")
