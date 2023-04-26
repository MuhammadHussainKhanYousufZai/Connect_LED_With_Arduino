from machine import Pin
from time import sleep
led = Pin(14,Pin.OUT)

for i in range(10):#Use to turn off the Bulb:
    led.value(0)
    sleep(0.5)#Use to turn On the Bulb
    led.value(1)
    sleep(0.5)
