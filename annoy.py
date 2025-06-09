import random
import pyautogui as sa
import time


# Corrected the typo in the animal list and added "ass"
animal = ('monkey', 'donkey', 'dog', 'ass')

time.sleep(8)  # Pauses for 8 seconds

for i in range(500):
    a = random.choice(animal)
    sa.write("you are a " + a)
    sa.press('enter')