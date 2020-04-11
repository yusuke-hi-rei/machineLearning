import cv2
import numpy as np

#! Start input from web camera.
cap = cv2.VideoCapture(0)
while True:
    #! Load the camera image.
    _, frame = cap.read()
    #! Reduce the image.
    frame = cv2.resize(frame, (500, 300))
    #! Output image to window.
    cv2.imshow("OpenCV Web Camera", frame)
    #! Press ESC or Enter to exit the loop.
    k = cv2.waitKey(1)
    if k == 27 or k == 13:
        break
#! Release the camera.
cap.release()
#! Destroy window.
cv2.destroyAllWindows()
