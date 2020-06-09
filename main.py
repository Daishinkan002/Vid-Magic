

import cv2
import pyautogui
import pyscreenshot as scrot
import numpy as np
import matplotlib.pyplot as plt
import threading


#w,h = pyautogui.size()
def screenrec():
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi",fourcc,20.0,pyautogui.size())

    while(True):
        im = scrot.grab()
        frame = np.array(im)
        out.write(frame)
        if cv2.waitKey(1) == ord('a'):
            break
        
    out.release()
    print("Done Scr. Recording")

def cam_rec():
    w,h = pyautogui.size()
    w_loc = (2*w)//3
    h_loc = (2*h)//3
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi",fourcc,20.0,pyautogui.size())

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        im = scrot.grab()
        screen = np.array(im)
        out.write(screen)
        print("Yup, cam is running")
        cv2.namedWindow('Cam',cv2.WINDOW_NORMAL)        # Create a named window
        cv2.moveWindow('Cam', w_loc,h_loc)
        cv2.resizeWindow('Cam', 400, 300)
        cv2.imshow('Cam', frame)
        out.write(screen) 
        if cv2.waitKey(1) == ord('q'):
            break

    out.release
    cap.release()
    print("Done Camera")



cam_rec()
