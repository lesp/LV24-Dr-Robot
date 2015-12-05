from gpiozero import LED
from gpiozero import Button
from gpiozero import Buzzer
import time

life1 = LED(17)
life2 = LED(27)
life3 = LED(22)
buzzer = Buzzer(10)
tool = Button(9)

def life_counter(lives):
    if lives == 3:
        life1.on()
        life2.on()
        life3.on()
    elif lives == 2:
        life1.on()
        life2.on()
        life3.off()
    elif lives == 1:
        life1.on()
        life2.off()
        life3.off()
    elif lives == 0:
        life1.off()
        life2.off()
        life3.off()

lives = 3
life_counter(lives)

while True:
    time.sleep(0.01)
    for i in range(2):
        buzzer.on()
        time.sleep(0.5)
        buzzer.off()
        time.sleep(0.5)
    while lives > 0:
        time.sleep(0.01)
        tool.wait_for_press()
        for i in range(3):
            buzzer.on()
            time.sleep(0.2)
            buzzer.off()
            time.sleep(0.2)
        time.sleep(0.1)
        print("You lost a life")
        lives = lives - 1
        life_counter(lives)
    if lives == 0:
        print("Game Over")
        time.sleep(3)
        lives=3
        life_counter(lives)
