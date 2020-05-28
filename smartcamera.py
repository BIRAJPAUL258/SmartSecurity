import p3Picam
import picamera
motionState = False
while True:
    motionState = p3Picam.motion()
    print(motionState)
    if motionState:
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.capture("motionPic.jpg")
        print("Picture taken.")
