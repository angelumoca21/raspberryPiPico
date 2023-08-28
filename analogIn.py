from machine import ADC
import time
potenciometro = ADC(26)

while True:
    print("\nValor en bits: ", potenciometro.read_u16())
    time.sleep(0.5)