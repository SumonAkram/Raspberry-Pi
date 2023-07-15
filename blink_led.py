import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the LED
led_pin = 17

# Set the pin as an output
GPIO.setup(led_pin, GPIO.OUT)

# Blink the LED
while True:
    GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
    time.sleep(1)                    # Wait for 1 second
    GPIO.output(led_pin, GPIO.LOW)   # Turn off the LED
    time.sleep(1)                    # Wait for 1 second
