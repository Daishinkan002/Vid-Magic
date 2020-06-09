

import cv2
import pyautogui
import pyscreenshot as scrot
import numpy as np
import matplotlib.pyplot as plt


w,h = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,pyautogui.size())
#print(w,h)

#cv2.namedWindow("Main")

while(True):
    im = scrot.grab()
    frame = np.array(im)
    #print(frame,type(frame))
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Main",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    
    cv2.imshow("Main", frame)
    out.write(frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()
cv2.destroyAllWindows()

'''

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #frame = cv2.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
'''