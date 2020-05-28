import p3Picam
import picamera
from datetime import datetime
motionState = False
picPath = "/home/pi/Desktop/smartsecurity/images/"

def captureImage(currentTime, picPath):
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.framerate = 80
        camera.capture(picPath + picName)
    print("We have taken a picture.")


def getTime():
    currentTime = datetime.now()
    return currentTime
while True:
    motionState = p3Picam.motion()
    print(motionState)
    if motionState:
        currentTime = getTime()
        captureImage(currentTime, picPath)
