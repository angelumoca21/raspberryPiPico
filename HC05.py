from machine import UART
uart = UART(0,9600)
while True:
    if uart.any()>0:
        dato = uart.read(1)
        print(dato)
        if dato == b'1':
            print("UNO")
        elif '2' in dato:
            print("DOS")