import keyboard
import time

# Ge användaren tid att öppna det fönster eller programmet där texten ska skrivas
time.sleep(2)


def key(word):
    # Texten med ett tab-tecken
    word = str(word)

    # Skriv texten med tab-tecken
    keyboard.write(word)

    # Tryck på Enter för att avsluta
    keyboard.press_and_release("enter")



person = {
    "namn": "Alice",
    "ålder": 30,
    "yrke": "Ingenjör"
}

def example():
    key(person["namn"])  # Skriver ut "Alice"
    key(person["ålder"])  # Skriver ut 30