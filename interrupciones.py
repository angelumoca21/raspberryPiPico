#https://docs.micropython.org/en/latest/library/machine.Pin.html
from machine import Pin
boton = Pin(2, Pin.IN, Pin.PULL_DOWN)
led = Pin(25,Pin.OUT)
led.value(0)

def interrupcion(pin):
    print("Presencia detectada")
    led.value(1)
    
boton.irq(trigger = Pin.IRQ_RISING, handler = interrupcion)