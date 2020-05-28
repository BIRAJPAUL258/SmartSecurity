import picamera
from subprocess import call
fileName = "/home/pi/Desktop/smartsecurity/newpic.jpg"
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture(fileName)
    print("We have taken a picture.")
    print("We are about to timestamp our picture.")
timestampMessage = "This Message!"
timestampCommand = "/usr/bin/convert " + fileName + " -pointsize 42 -fill red -annotate +700+500 '" + timestampMessage + "' " + fileName
call([timestampCommand], shell=True)
print("Picture has been timestamped.")
