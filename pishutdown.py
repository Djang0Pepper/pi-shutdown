

#!/usr/bin/python
# shutdown/reboot(/power on) Raspberry Pi with pushbutton

#pi-shutdown
#===========
#Shutdown/reboot(/power on) Raspberry Pi with pushbutton
# Usage:
#Connect pushbutton to GPIO pin 5 and ground then run:
#```
#sudo python pishutdown.py
#```
#When button is pressed for less than 3 seconds, Pi reboots. If pressed for more than 3 seconds it shuts down.
#While shut down, if button is connected to GPIO pin 5, then pressing the button powers on Pi.

import RPi.GPIO as GPIO
from subprocess import call
from datetime import datetime
import time

# pushbutton connected to this GPIO pin, using pin 5 also has the benefit of
# waking / powering up Raspberry Pi when button is pressed
shutdownPin = 21
LED = 26


# if button pressed for at least this long then shut down. if less then reboot.
shutdownMinSeconds = 3

# button debounce time in seconds
debounceSeconds = 0.01

#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(shutdownPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

buttonPressedTime = None

def buttonStateChanged(pin):
    global buttonPressedTime

    if not (GPIO.input(pin)):
        # button is down
        if buttonPressedTime is None:
            buttonPressedTime = datetime.now()
    else:
        # button is up
        if buttonPressedTime is not None:
            elapsed = (datetime.now() - buttonPressedTime).total_seconds()
            buttonPressedTime = None
            if elapsed >= shutdownMinSeconds:
                # button pressed for more than specified time, shutdown
                call(['shutdown', '-h', 'now'], shell=False)
                GPIO.output(LED, GPIO.LOW) #On l’éteint
            elif elapsed >= debounceSeconds:
                # button pressed for a shorter time, reboot
                call(['shutdown', '-r', 'now'], shell=False)
                GPIO.output(LED, GPIO.HIGH) #On l’allume


# subscribe to button presses
GPIO.add_event_detect(shutdownPin, GPIO.BOTH, callback=buttonStateChanged)

while True:
    # sleep to reduce unnecessary CPU usage
    GPIO.output(LED, GPIO.LOW) #On l’éteint
    time.sleep(3)
    GPIO.output(LED, GPIO.HIGH) #On l'allume
    time.sleep(2)
