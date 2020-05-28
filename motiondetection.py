import RPi.GPIO as GPIO
import time
import picamera
import datetime
import subprocess
import os

def getFileName():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam = picamera.PiCamera()

while True:
    time.sleep(1)
    prevState = currState
    currState = GPIO.input(sensorPin)
    if currState != prevState:
        newState = "HIGH" if currState else "LOW"
        print ("Input %s is %s" % (sensorPin, newState))
        if currState:
            fileName = getFileName()
            print ("Starting Recording")
         
            cam.start_recording(fileName)
            print (fileName)
        else:
           
            cam.stop_recording()
            print ("Stopped Recording")
