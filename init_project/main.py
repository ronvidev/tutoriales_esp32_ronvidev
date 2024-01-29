from machine import Pin
import time

pin_led = Pin(2, Pin.OUT)

while True:
    pin_led.value(1)
    time.sleep(1) 
    pin_led.value(0)
    time.sleep(1) 
