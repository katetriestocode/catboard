import machine
import time

led = machine.Pin(0, machine.Pin.OUT)

print("Starting blinky...")

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
