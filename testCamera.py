import picamera
from server import *

def startCamera():
    try:
        sendvideo()
    except KeyboardInterrupt:
        print ("\nEnd of program")

startCamera()