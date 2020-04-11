#!/usr/bin/env python
# coding: utf-8

# # ・DetectThePartWhereTheScreenHasMoved

# In[4]:


import cv2

#! Start input from web camera.
cap = cv2.VideoCapture(0)
#! Variable to store previous image.
img_last = None
green = (0, 255, 0)

while True:
    #! Load the camera image.
    _, frame = cap.read()
    #! Reduce the image.
    frame = cv2.resize(frame, (500, 300))
    #! Convert to black and white image.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 0)
    img_b = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]
    #! Check the difference.
    if img_last is None:
        img_last = img_b
        continue
    frame_diff = cv2.absdiff(img_last, img_b)
    cnts = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    #! Draw the point where there was a difference.
    for pt in cnts:
        x, y, w, h = cv2.boundingRect(pt)
        if w < 30:
            continue
            cv2.rectangle(frame, (x, y), (x+w, y+h), green, 2)
    #! Save this frame.
    img_last = img_b
    #! Show on screen
    cv2.imshow("Diff Camera", frame)
    cv2.imshow("diff data", frame_diff)
    #! Press ESC or Enter to exit the loop.
    k = cv2.waitKey(1)
    if k == 27 or k == 13:
        break
#! Release the camera.
cap.release()
#! Destroy window.
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




