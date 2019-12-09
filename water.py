import RPi.GPIO as GPIO
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("물이 없는게 감지된다 목마르다 !")
    else:
        print("물이 넘쳐난다 이맛이지 ~ ")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
        
