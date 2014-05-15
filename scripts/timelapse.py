# take snapshots to create a timelapse video

import time
import picamera

print "How many minutes would you like your photo interval to be?"
minutes = int(raw_input(">: "))
seconds = minutes * 60

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(seconds)

