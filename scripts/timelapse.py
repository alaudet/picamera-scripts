# take snapshots to create a timelapse video

import time
import picamera
import subprocess

def snap_pics(seconds):
    try:
        with picamera.PiCamera() as camera:
            # resolutions (2592x1944) (1024x768)
            camera.resolution = (1024, 768)
            camera.start_preview()
            time.sleep(2)
            for filename in camera.capture_continuous('tlapse{counter:04d}.jpg'):
                print('Captured %s' % filename)
                time.sleep(seconds)
    
    except KeyboardInterrupt:
        print "Timelapse pictures halted"
        print "Your choices are:"
        print "1 - Start over"
        print "2 - Stop taking pictures and create your video"
        print "3 - Exit program without creating video"
        
        choice = raw_input(":> ")

        if choice == "1":
            timelapse_parameters()
        elif choice == "2":
            print "Creating Video....this may take a while"
            confirm = raw_input("Are you sure (y/n)? It may be quicker to copy the files to a more powerful computer. :> ")
            if "y" in confirm or "Y" in confirm:
                time.sleep(2)
                cmdline = "avconv -r 10 -i tlapse%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4"
                avconv = cmdline.split(' ')
                subprocess.call(avconv)
                print "Video Complete"
                exit(0)
            else:
                print "Copy all jpg's to a more powerful computer to create"
                print "your timelapse video using Avconv. Goodbye"
        else:
            print "Program ended. Goodbye"
            exit(0)



def timelapse_parameters():
    method = raw_input("Select timelapse in seconds or minutes (S or M):> ")

    if "s" in method or "S" in method:
        seconds = int(raw_input("Enter photo interval in seconds: >: "))
        snap_pics(seconds)
    elif "m" in method or "M" in method:
        minutes = int(raw_input("Enter photo internval in minutes: >: "))
        seconds = minutes * 60
        snap_pics(seconds)
    else:
        print "Invalid entry - Try again"
        timelapse_parameters()

print "The following script will take a series of pictures and then give you the option"
print "of creating a timelapse video."
print "You may stop taking pictures at any time by pressing CTRL-C."

raw_input("Press any key to get started")
timelapse_parameters()
