# take snapshots to create a timelapse video

import time
import picamera

method = raw_input("Select timelapse in seconds or minutes (S or M):> ")

if "s" in method or "S" in method:
    seconds = int(raw_input("Enter photo interval in seconds: >: "))

elif "m" in method or "M" in method:
    minutes = int(raw_input("Enter photo internval in minutes: >: "))
    seconds = minutes * 60

else:
    print "Invalid entry"
    exit(0)

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(seconds)

