import picamera

x = 30 # number of seconds to record
file_name = "small.h264" 
v = 320
h = 240

with picamera.PiCamera() as camera:
    camera.resolution = (v, h)

    print "A %i second video called %s is now recording...please wait." % (x, file_name)
	
    camera.start_recording(file_name)
    camera.wait_recording(x)
    camera.stop_recording()
