import picamera
from time import sleep
from subprocess import call
#Setup the camera
with picamera.PiCamera() as camera:
    #start recording
     camera.start_recording("pythonVideo.h264")
     sleep(5)
    #stop recording
     camera.stop_recording()
# The camera is closed

     print("We are going to convert the video.")
     #Define the command
     command = "MP4Box -add pythonVideo.h264 convertedVideo.mp4"
     #Execute
     call([command], shell=True)
     #Vidoe converted.
     print("Video converted.")
