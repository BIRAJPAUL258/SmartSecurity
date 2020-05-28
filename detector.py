from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()
filename = "intruder.h264"

while True:
    pir.wait_for_motion()
    print("Motion Detected!")
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()
