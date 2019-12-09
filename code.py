import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT, initial = GPIO.LOW)  #LED to GPIO24( merah1 )
GPIO.setup(25, GPIO.OUT, initial = GPIO.LOW)  #LED to GPIO25( kuning )
GPIO.setup(27, GPIO.OUT, initial = GPIO.HIGH) #LED to GPIO27( hijau1 )
GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW)  #LED to GPIO17( merah2 )
GPIO.setup(22, GPIO.OUT, initial = GPIO.HIGH) #LED to GPIO22( hijau2 )
x=1

try:
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
                 GPIO.output(24, GPIO.LOW)
                 GPIO.output(17, GPIO.LOW)
                 GPIO.output(25, GPIO.HIGH)
                 GPIO.output(27, GPIO.LOW)
                 GPIO.output(22, GPIO.LOW)
                 time.sleep(1)
         #else:
                 GPIO.output(24, GPIO.HIGH)
                 GPIO.output(17, GPIO.LOW)
                 GPIO.output(25, GPIO.LOW)
                 GPIO.output(27, GPIO.LOW)
                 GPIO.output(22, GPIO.HIGH)
                 print('Button Pressed...')
                 time.sleep(2)

                 GPIO.output(24, GPIO.LOW)
                 GPIO.output(17, GPIO.LOW)
                 GPIO.output(25, GPIO.HIGH)
                 GPIO.output(27, GPIO.LOW)
                 GPIO.output(22, GPIO.LOW)
                 print('Button Pressed...')
                 time.sleep(1)

                 GPIO.output(24, GPIO.LOW)
                 GPIO.output(17, GPIO.HIGH)
                 GPIO.output(25, GPIO.LOW)
                 GPIO.output(27, GPIO.HIGH)
                 GPIO.output(22, GPIO.LOW)
                 print('Button Pressed...')
                 time.sleep(2)




except:
    GPIO.cleanup()
