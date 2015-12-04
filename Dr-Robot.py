import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

life1 = 17
life2 = 27
life3 = 22
buzzer = 10
tool = 9

GPIO.setup(life1, GPIO.OUT)
GPIO.setup(life2, GPIO.OUT)
GPIO.setup(life3, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(tool, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

def life_counter(lives):
    if lives == 3:
        GPIO.output(17,1)
        GPIO.output(27,1)
        GPIO.output(22,1)
    elif lives == 2:
        GPIO.output(17,1)
        GPIO.output(27,1)
        GPIO.output(22,0)
    elif lives == 1:
        GPIO.output(17,1)
        GPIO.output(27,0)
        GPIO.output(22,0)
    elif lives == 0:
        GPIO.output(17,0)
        GPIO.output(27,0)
        GPIO.output(22,0)

lives = 3
life_counter(lives)

while True:
    time.sleep(0.01)
    for i in range(2):
        GPIO.output(buzzer, 1)
        time.sleep(0.5)
        GPIO.output(buzzer,0)
        time.sleep(0.5)
    while lives > 0:
        time.sleep(0.01)
        GPIO.wait_for_edge(tool, GPIO.FALLING)
        for i in range(3):
            GPIO.output(buzzer, 1)
            time.sleep(0.2)
            GPIO.output(buzzer, 0)
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
