## Pi camera setup
from picamera2 import Picamera2

 === CAMERA SETUP ===  <br>
picam2 = Picamera2()  <br>
camera_config = picam2.create_still_configuration(main={"size": (640, 480)})  <br>
picam2.configure(camera_config)  <br>
picam2.start()  <br>

## Classic USB camera setup
import cv2 #this code is using openCV <br> 

=== USB CAMERA SETUP ===  <br>
cap = cv2.VideoCapture(0)   <br>
if not cap.isOpened(): <br>
    print("Could not open USB camera.") <br>
    exit() <br>
### Use 1 if 0 doesn't work in cv2.VideoCapture(0). This can happen especially if you have multiple external cameras 