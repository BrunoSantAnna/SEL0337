import json
import requests
import pprint

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15

camera.start_preview()
camera.annotate_text_size = 50
camera.annotate_text = "11819507 - 11800991"
sleep(5)
camera.capture('/home/sel/Bruno_e_WIll/foto.jpg')
camera.stop_preview()
