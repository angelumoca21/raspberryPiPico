from machine import Pin, ADC, PWM
import time
potenciometro = ADC(28)
led = PWM(Pin(2))
led.freq(1000)

while True:
    led.duty_u16(potenciometro.read_u16())