import io
import time
import picamera

# Create an in-memory stream
my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    # Camera warm-up time
    time.sleep(300)
    camera.capture(my_stream, 'jpeg')
