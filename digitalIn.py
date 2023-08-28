from machine import Pin
import time

button1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(1, Pin.IN, Pin.PULL_UP)

while True:
    if button1.value() == 1: 
        print("¡Presionaste el boton 1!")
        time.sleep(0.5)
    if button2.value() == 0:
        print("¡Presionaste el boton 2!")
        time.sleep(0.5)