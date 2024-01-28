# main.py -- put your code here!
from machine import Pin
import time

# Configura el pin GPIO donde está conectado el LED
pin_led = Pin(2, Pin.OUT)  # Pin 2 en el ESP32

# Función para encender el LED
def encender_led():
    pin_led.value(1)  # Establece el pin en HIGH para encender el LED

# Función para apagar el LED
def apagar_led():
    pin_led.value(0)  # Establece el pin en LOW para apagar el LED

# Ciclo principal
while True:
    encender_led()  # Enciende el LED
    time.sleep(1)   # Espera 1 segundo
    apagar_led()    # Apaga el LED
    time.sleep(1)   # Espera 1 segundo
