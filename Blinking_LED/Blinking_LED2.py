from machine import Pin
from time import sleep
led = Pin(14,Pin.OUT)

for i in range(10):
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
