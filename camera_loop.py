# NOTE:  I needed to change permissions on /dev/vchiq to make this work...
# Also needed to chmod 666 temp.jpg

# used to slow down our main loop
import time 

from picamera import PiCamera

###################################
# Main loop 
###################################
print "start"
camera = PiCamera()
print "camera"
camera.capture('temp.jpg')
print ("jpg")

try:
  print("Press CTRL-C to stop")
  while True:
    camera.capture('temp.jpg')
    time.sleep(.2)

except KeyboardInterrupt:
  exit(0)
