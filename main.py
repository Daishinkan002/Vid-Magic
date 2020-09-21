import cv2
import pyautogui
import requests
import pyscreenshot as scrot
import numpy as np
import os

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
    select = input("Are you taking it from mobile ? ")
    w,h = pyautogui.size()
    w_loc = w-400
    #h_loc = (2*h)//3
    h_loc = 0

    cap = cv2.VideoCapture(0)
    if(select == 'y' or 'Y'):
        ip = "https://192.168.43.1:8080/shot.jpg"

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi",fourcc,20.0,pyautogui.size())
    cv2.namedWindow('Cam',cv2.WINDOW_NORMAL)
    if(select == 'y' or select == 'Y'):
        while(True):
            resp = requests.get(ip, verify=False)
            
            img_arr = np.array(bytearray(resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            im = scrot.grab()
            screen = np.array(im)
            out.write(screen)
            print("Yup, cam is running")
            cv2.moveWindow('Cam', w_loc,h_loc)
            cv2.resizeWindow('Cam', 400, 300)
            os.system("wmctrl -r Cam -b add,above")
            cv2.imshow('Cam', img)
            out.write(screen)
            if cv2.waitKey(1) == ord('q'):
                break
    else:
        while cv2.waitKey(1) != 27:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            im = scrot.grab()
            screen = np.array(im)
            out.write(screen)
            print("Yup, cam is running")
            cv2.moveWindow('Cam', w_loc,h_loc)
            cv2.resizeWindow('Cam', 400, 300)
            os.system("wmctrl -r Cam -b add,above")
            cv2.imshow('Cam', frame)
            out.write(screen) 
            if cv2.waitKey(1) == ord('q'):
                break

    
    out.release
    cap.release()
    print("Done Camera")


if __name__ == "__main__":
    cam_rec()
