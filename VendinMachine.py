import RPi.GPIO as GPIO
import time
from lcd_i2c import LCD  # Use your I2C LCD driver

# GPIO pin setup
BUTTON_1 = 17  # Button for Product 1
BUTTON_2 = 27  # Button for Product 2
MOTOR_1 = 22   # Motor for Product 1
MOTOR_2 = 23   # Motor for Product 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(MOTOR_1, GPIO.OUT)
GPIO.setup(MOTOR_2, GPIO.OUT)

# LCD Setup
lcd = LCD()
lcd.clear()
lcd.write("Select Product")

def dispense(motor_pin):
    lcd.clear()
    lcd.write("Dispensing...")
    GPIO.output(motor_pin, GPIO.HIGH)
    time.sleep(2)  # Dispense duration
    GPIO.output(motor_pin, GPIO.LOW)
    lcd.clear()
    lcd.write("Thank you!")
    time.sleep(2)
    lcd.clear()
    lcd.write("Select Product")

try:
    while True:
        if GPIO.input(BUTTON_1) == GPIO.LOW:
            lcd.clear()
            lcd.write("Product 1 chosen")
            time.sleep(1)
            dispense(MOTOR_1)

        elif GPIO.input(BUTTON_2) == GPIO.LOW:
            lcd.clear()
            lcd.write("Product 2 chosen")
            time.sleep(1)
            dispense(MOTOR_2)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.clear()
    lcd.write("Goodbye!")
